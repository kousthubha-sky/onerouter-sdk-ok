# OneRouter Python SDK

Official Python SDK for OneRouter - Unified API for payments, SMS, email, and more.

[![PyPI version](https://badge.fury.io/py/onerouter.svg)](https://pypi.org/project/onerouter/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Installation

```bash
pip install onerouter
```

## Quick Start

```python
from onerouter import OneRouter

client = OneRouter(api_key="unf_live_xxx")

# Create payment
order = await client.payments.create(
    amount=500.00,
    currency="INR"
)

print(f"Order ID: {order['transaction_id']}")
print(f"Checkout URL: {order['checkout_url']}")
```

## Features

- **Unified API**: Single interface for Razorpay, PayPal, Twilio, Resend
- **Async & Sync**: Support for both async/await and synchronous code
- **Automatic Retries**: Built-in retry logic with exponential backoff
- **Idempotency**: Prevent duplicate requests automatically
- **Type Hints**: Full type support for IDE autocomplete
- **Error Handling**: Comprehensive exception hierarchy

## Usage Examples

### Async Usage (Recommended)

```python
import asyncio
from onerouter import OneRouter

async def main():
    async with OneRouter(api_key="unf_live_xxx") as client:
        # Create payment
        order = await client.payments.create(
            amount=500.00,
            currency="INR",
            receipt="order_123"
        )

        # Get payment status
        status = await client.payments.get(order['transaction_id'])

        # Create refund
        refund = await client.payments.refund(
            payment_id=order['provider_order_id'],
            amount=100.00  # Partial refund
        )

asyncio.run(main())
```

### Sync Usage

```python
from onerouter import OneRouterSync

client = OneRouterSync(api_key="unf_live_xxx")

try:
    order = client.payments.create(
        amount=500.00,
        currency="INR"
    )
    print(f"Order: {order['transaction_id']}")
finally:
    client.close()
```

### Send SMS (Twilio)

```python
async with OneRouter(api_key="unf_live_xxx") as client:
    # Send SMS
    sms = await client.sms.send(
        to="+1234567890",
        body="Your verification code is 123456"
    )

    print(f"Message SID: {sms['message_id']}")
    print(f"Status: {sms['status']}")

    # Check delivery status
    status = await client.sms.get(sms['message_id'])
    print(f"Delivery status: {status['status']}")
```

### Send Email (Resend)

```python
async with OneRouter(api_key="unf_live_xxx") as client:
    # Send email
    email = await client.email.send(
        to="user@example.com",
        subject="Welcome to OneRouter!",
        html_body="<h1>Welcome!</h1><p>Thanks for signing up.</p>",
        from_email="hello@yourdomain.com"  # Optional
    )

    print(f"Email ID: {email['email_id']}")
    print(f"Status: {email['status']}")
```

### Subscriptions

```python
async with OneRouter(api_key="unf_live_xxx") as client:
    # Create subscription
    subscription = await client.subscriptions.create(
        plan_id="plan_monthly_99",
        customer_notify=True,
        total_count=12
    )

    # Get subscription
    sub_details = await client.subscriptions.get(subscription['id'])

    # Cancel subscription
    await client.subscriptions.cancel(
        subscription_id=subscription['id'],
        cancel_at_cycle_end=True
    )
```

### Payment Links

```python
async with OneRouter(api_key="unf_live_xxx") as client:
    # Create payment link
    link = await client.payment_links.create(
        amount=999.00,
        description="Premium Plan",
        customer_email="user@example.com"
    )

    print(f"Share this link: {link['short_url']}")
```

### Error Handling

```python
from onerouter import (
    OneRouter,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    APIError
)

async with OneRouter(api_key="unf_live_xxx") as client:
    try:
        order = await client.payments.create(amount=500.00)

    except AuthenticationError:
        print("Invalid API key")

    except RateLimitError as e:
        print(f"Rate limit exceeded. Retry after {e.retry_after} seconds")

    except ValidationError as e:
        print(f"Validation error: {e}")

    except APIError as e:
        print(f"API error ({e.status_code}): {e}")
```

## Configuration

```python
client = OneRouter(
    api_key="unf_live_xxx",
    base_url="https://api.onerouter.dev",  # Optional: Custom API URL
    timeout=30,                             # Optional: Request timeout (seconds)
    max_retries=3                           # Optional: Max retry attempts
)
```

## API Reference

### Payments

| Method | Description |
|--------|-------------|
| `payments.create(amount, currency, ...)` | Create a payment order |
| `payments.get(transaction_id)` | Get payment details |
| `payments.refund(payment_id, amount)` | Create refund |

### SMS

| Method | Description |
|--------|-------------|
| `sms.send(to, body)` | Send SMS message |
| `sms.get(message_id)` | Get delivery status |

### Email

| Method | Description |
|--------|-------------|
| `email.send(to, subject, html_body, ...)` | Send email |
| `email.get(email_id)` | Get email status |

### Subscriptions

| Method | Description |
|--------|-------------|
| `subscriptions.create(plan_id, ...)` | Create subscription |
| `subscriptions.get(subscription_id)` | Get subscription details |
| `subscriptions.cancel(subscription_id)` | Cancel subscription |

### Payment Links

| Method | Description |
|--------|-------------|
| `payment_links.create(amount, ...)` | Create payment link |

## Testing

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=onerouter tests/
```

## Requirements

- Python 3.8+
- httpx
- pydantic

## Support

- **Documentation**: https://docs.onerouter.dev
- **PyPI**: https://pypi.org/project/onerouter/
- **GitHub**: https://github.com/onerouter/onerouter-python
- **Email**: support@onerouter.dev

## License

MIT License - see LICENSE file for details.

## Related

- [Main Repository](../README.md)
- [JavaScript SDK](../onerouter-js/README.md)
- [Backend API](../backend/README.md)
