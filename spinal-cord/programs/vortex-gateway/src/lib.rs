use anchor_lang::prelude::*;
use anchor_lang::system_program;

// This is your Program ID (Placeholder - generated when we deploy later)
declare_id!("VortexGateway11111111111111111111111111111111");

#[program]
pub mod vortex_gateway {
    use super::*;

    // 1. Initialize the Master State (Admin only)
    pub fn initialize(ctx: Context<Initialize>, subscription_price: u64) -> Result<()> {
        let state = &mut ctx.accounts.vortex_state;
        state.admin = *ctx.accounts.admin.key;
        state.subscription_price_sol = subscription_price; 
        state.treasury = *ctx.accounts.treasury.key;
        Ok(())
    }

    // 2. User Subscribes (Pays SOL -> Gets Access Time)
    pub fn subscribe(ctx: Context<Subscribe>, duration_seconds: i64) -> Result<()> {
        let user_account = &mut ctx.accounts.user_subscription;
        let state = &ctx.accounts.vortex_state;
        
        // Calculate Cost (Fixed Rate for V1)
        let cost = state.subscription_price_sol; 

        // Transfer SOL from User to Treasury (Not the contract!)
        // This is "Sovereign" safety - funds sit in your wallet, not a script.
        let cpi_context = CpiContext::new(
            ctx.accounts.system_program.to_account_info(),
            system_program::Transfer {
                from: ctx.accounts.user.to_account_info(),
                to: ctx.accounts.treasury.to_account_info(),
            },
        );
        system_program::transfer(cpi_context, cost)?;

        // Update Subscription State (The "Access Card")
        let clock = Clock::get()?;
        let current_time = clock.unix_timestamp;

        if user_account.expiry_ts > current_time {
            // Extend existing time
            user_account.expiry_ts += duration_seconds;
        } else {
            // New subscription
            user_account.expiry_ts = current_time + duration_seconds;
        }

        msg!("Vortex Access Granted. Expiry: {}", user_account.expiry_ts);
        Ok(())
    }
}

// --- Data Structures (The Memory) ---

#[account]
pub struct VortexState {
    pub admin: Pubkey,
    pub treasury: Pubkey,
    pub subscription_price_sol: u64,
}

#[account]
pub struct UserSubscription {
    pub expiry_ts: i64, // Unix Timestamp
}

// --- Validation Contexts (The Security) ---

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = admin, space = 8 + 32 + 32 + 8)]
    pub vortex_state: Account<'info, VortexState>,
    #[account(mut)]
    pub admin: Signer<'info>,
    /// CHECK: Safe because we just store this address as the vault
    pub treasury: UncheckedAccount<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Subscribe<'info> {
    #[account(mut)]
    pub vortex_state: Account<'info, VortexState>,
    // The "Seed" mechanism acts as a deterministic lookup
    // No database needed; the blockchain IS the database.
    #[account(
        init_if_needed, 
        payer = user, 
        space = 8 + 8,
        seeds = [b"subscription", user.key().as_ref()], 
        bump
    )]
    pub user_subscription: Account<'info, UserSubscription>,
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut, address = vortex_state.treasury)]
    /// CHECK: Verified against state to ensure funds go to the right vault
    pub treasury: UncheckedAccount<'info>,
    pub system_program: Program<'info, System>,
}
