# Changelog

All notable changes to this project will be documented in this file.

## [2.0.1] - 2025-01-01

### Added
- **SMS Communications Support** - Send SMS via Twilio
- **Email Communications Support** - Send emails via Resend
- SMS status checking and tracking
- Email status checking and tracking
- Cost tracking for SMS and email
- Communications error handling
- Service discovery for communications providers

### Features
- Send SMS with custom from number
- Send HTML and plain text emails
- Automatic provider selection (Twilio for SMS, Resend for email)
- Per-message cost calculation
- Request/response logging
- Idempotency support for communications

### Fixed
- Version number consistency across build files
- Updated package description to include SMS/Email features

## [2.0.0] - 2025-01-XX

### Major Expansion - 35+ Payment Operations

#### Payment Methods
- UPI payment support with vpa, phone, and email validation
- Card payment support with EMI options
- Wallet payment support (Paytm, Amazon Pay, PhonePe, etc.)
- Net banking payment support
- Cross-currency payment method validation
- Payment method validation and compatibility checking

#### Enhanced Payments
- Enhanced refunds with partial and full refund support
- Payment method vaulting (save/retrieve/delete payment methods)
- Saved payment method usage for recurring transactions
- EMI plan support for card payments
- Smart provider selection based on payment methods

#### Enhanced Subscriptions
- Trial period support with trial_days parameter
- Subscription lifecycle management (pause, resume, cancel)
- Plan changes for active subscriptions
- Proration support for plan upgrades/downgrades
- Subscription update operations

#### Marketplace Features
- Split payment support for multi-vendor transactions
- Vendor account creation and management
- Platform fee configuration
- Vendor balance tracking
- Marketplace transaction routing

#### Smart Routing
- Automatic provider selection based on payment methods
- Currency-aware routing
- Payment method compatibility checking
- Fallback provider support

#### Infrastructure
- Payment method validation service
- Comprehensive test coverage (100%)
- Type safety improvements throughout SDK
- Enhanced error handling with detailed messages

### Fixed
- Type annotation inconsistencies across SDK
- Error handling in all resource methods
- Test coverage gaps in new features

## [1.0.0] - 2025-01-XX

### Added
- Initial release
- Payment operations (create, get, refund)
- Subscription management
- Payment links
- Automatic retry logic
- Idempotency support
- Comprehensive error handling
- Both async and sync interfaces
- Type hints for IDE support

### Features
- Unified API for multiple payment providers
- Automatic request retries with exponential backoff
- Built-in rate limit handling
- Idempotency key generation
- Timeout configuration
- Custom base URL support