# OneRouter SDK v2.0.0 - Complete Documentation

## Table of Contents

- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
- [Payment Methods](#payment-methods)
- [Payments](#payments)
- [Subscriptions](#subscriptions)
- [Saved Payment Methods](#saved-payment-methods)
- [Marketplace](#marketplace)
- [Payment Links](#payment-links)
- [Error Handling](#error-handling)
- [Advanced Features](#advanced-features)
- [Examples](#examples)

---

## Quick Start

### Installation

```bash
pip install onerouter
```

### Basic Usage

```python
import onerouter

# Initialize client
client = onerouter.Client(
    api_key="your_api_key",
    base_url="https://api.onerouter.com"
)

# Create a payment
payment = client.payments.create(
    amount=1000,  # Amount in smallest currency unit (e.g., cents)
    currency="USD",
    customer_id="cust_123",
    payment_method={
        "type": "card",
        "card": {
            "number": "4242424242424242",
            "expiry_month": "12",
            "expiry_year": "2025",
            "cvv": "123"
        }
    }
)
```

---

## Installation

### From PyPI

```bash
pip install onerouter
```

### With Development Dependencies

```bash
pip install onerouter[dev]
```

### Verify Installation

```python
import onerouter
print(onerouter.__version__)  # 2.0.0
```

---

## Configuration

### Initialize Client

```python
import onerouter

client = onerouter.Client(
    api_key="your_api_key",  # Required
    base_url="https://api.onerouter.com",  # Required
    timeout=30,  # Optional: Request timeout in seconds (default: 30)
    max_retries=3,  # Optional: Maximum retry attempts (default: 3)
    retry_delay=1,  # Optional: Initial retry delay in seconds (default: 1)
    environment="production"  # Optional: 'development' or 'production'
)
```

### Async Client

```python
import asyncio
import onerouter

async def main():
    client = onerouter.AsyncClient(
        api_key="your_api_key",
        base_url="https://api.onerouter.com"
    )
    
    payment = await client.payments.create(
        amount=1000,
        currency="USD",
        customer_id="cust_123"
    )
    
    print(payment)

asyncio.run(main())
```

---

## Payment Methods

The SDK supports multiple payment methods with intelligent validation and routing.

### Supported Payment Methods

1. **UPI** (Unified Payments Interface)
2. **Card** (Credit/Debit cards with EMI support)
3. **Wallet** (Paytm, Amazon Pay, PhonePe, etc.)
4. **Net Banking**

### UPI Payment

```python
payment = client.payments.create(
    amount=50000,  # ₹500
    currency="INR",
    customer_id="cust_123",
    payment_method={
        "type": "upi",
        "upi": {
            "vpa": "customer@upi",  # Virtual Payment Address
            # OR
            "phone": "+919876543210",
            # OR
            "email": "customer@example.com"
        }
    }
)
```

### Card Payment

```python
payment = client.payments.create(
    amount=1000,
    currency="USD",
    customer_id="cust_123",
    payment_method={
        "type": "card",
        "card": {
            "number": "4242424242424242",
            "expiry_month": "12",
            "expiry_year": "2025",
            "cvv": "123"
        }
    }
)
```

### Card with EMI

```python
payment = client.payments.create(
    amount=10000,
    currency="INR",
    customer_id="cust_123",
    payment_method={
        "type": "card",
        "card": {
            "number": "4242424242424242",
            "expiry_month": "12",
            "expiry_year": "2025",
            "cvv": "123"
        },
        "emi": {
            "tenure": 6  # 6 months EMI
        }
    }
)
```

### Wallet Payment

```python
payment = client.payments.create(
    amount=1000,
    currency="INR",
    customer_id="cust_123",
    payment_method={
        "type": "wallet",
        "wallet": {
            "provider": "paytm",  # paytm, amazonpay, phonepe, etc.
            "wallet_id": "wallet_123"
        }
    }
)
```

### Net Banking

```python
payment = client.payments.create(
    amount=1000,
    currency="INR",
    customer_id="cust_123",
    payment_method={
        "type": "netbanking",
        "netbanking": {
            "bank": "HDFC"  # Bank code
        }
    }
)
```

---

## Payments

### Create Payment

```python
payment = client.payments.create(
    amount=1000,
    currency="USD",
    customer_id="cust_123",
    payment_method={
        "type": "card",
        "card": {
            "number": "4242424242424242",
            "expiry_month": "12",
            "expiry_year": "2025",
            "cvv": "123"
        }
    },
    metadata={
        "order_id": "order_123",
        "description": "Product purchase"
    }
)
```

### Get Payment

```python
payment = client.payments.retrieve(payment_id="pay_123")
```

### List Payments

```python
payments = client.payments.list(
    customer_id="cust_123",
    limit=10,
    skip=0
)
```

### Refund Payment

```python
# Full refund
refund = client.payments.refund(
    payment_id="pay_123",
    amount=1000
)

# Partial refund
refund = client.payments.refund(
    payment_id="pay_123",
    amount=500
)

# Enhanced refund with metadata
refund = client.payments.refund(
    payment_id="pay_123",
    amount=500,
    reason="customer_requested",
    metadata={
        "notes": "Customer requested partial refund"
    }
)
```

---

## Subscriptions

### Create Subscription with Trial

```python
subscription = client.subscriptions.create(
    plan_id="plan_monthly",
    customer_id="cust_123",
    trial_days=14,  # 14-day free trial
    payment_method={
        "type": "card",
        "card": {
            "number": "4242424242424242",
            "expiry_month": "12",
            "expiry_year": "2025",
            "cvv": "123"
        }
    }
)
```

### Get Subscription

```python
subscription = client.subscriptions.retrieve(subscription_id="sub_123")
```

### List Subscriptions

```python
subscriptions = client.subscriptions.list(
    customer_id="cust_123",
    status="active",
    limit=10
)
```

### Pause Subscription

```python
subscription = client.subscriptions.pause(
    subscription_id="sub_123",
    pause_at="cycle_end"  # or "immediate"
)
```

### Resume Subscription

```python
subscription = client.subscriptions.resume(subscription_id="sub_123")
```

### Cancel Subscription

```python
subscription = client.subscriptions.cancel(
    subscription_id="sub_123",
    cancel_at="cycle_end"  # or "immediate"
)
```

### Change Subscription Plan

```python
subscription = client.subscriptions.update(
    subscription_id="sub_123",
    plan_id="plan_yearly",
    proration_behavior="create_prorations"  # or "none", "always_invoice"
)
```

---

## Saved Payment Methods

### Save Payment Method

```python
payment_method = client.saved_payment_methods.create(
    customer_id="cust_123",
    payment_method={
        "type": "card",
        "card": {
            "number": "4242424242424242",
            "expiry_month": "12",
            "expiry_year": "2025",
            "cvv": "123"
        }
    },
    is_default=True
)
```

### Get Saved Payment Method

```python
payment_method = client.saved_payment_methods.retrieve(
    customer_id="cust_123",
    payment_method_id="pm_123"
)
```

### List Saved Payment Methods

```python
payment_methods = client.saved_payment_methods.list(
    customer_id="cust_123"
)
```

### Delete Saved Payment Method

```python
client.saved_payment_methods.delete(
    customer_id="cust_123",
    payment_method_id="pm_123"
)
```

### Use Saved Payment Method for Payment

```python
payment = client.payments.create(
    amount=1000,
    currency="USD",
    customer_id="cust_123",
    payment_method_id="pm_123"  # Use saved payment method
)
```

---

## Marketplace

### Create Vendor Account

```python
vendor = client.marketplace.create_vendor(
    name="Vendor Name",
    email="vendor@example.com",
    bank_account={
        "account_number": "1234567890",
        "ifsc": "HDFC0001234"
    },
    settlement_schedule="daily"  # or "weekly", "monthly"
)
```

### Get Vendor

```python
vendor = client.marketplace.retrieve_vendor(vendor_id="vendor_123")
```

### List Vendors

```python
vendors = client.marketplace.list_vendors(limit=10)
```

### Create Split Payment

```python
payment = client.marketplace.create_split_payment(
    amount=10000,
    currency="USD",
    customer_id="cust_123",
    splits=[
        {
            "vendor_id": "vendor_123",
            "amount": 8000,
            "type": "flat"  # or "percentage"
        },
        {
            "vendor_id": "vendor_456",
            "amount": 2000,
            "type": "flat"
        }
    ],
    platform_fee={
        "amount": 500,
        "type": "flat"
    },
    payment_method={
        "type": "card",
        "card": {
            "number": "4242424242424242",
            "expiry_month": "12",
            "expiry_year": "2025",
            "cvv": "123"
        }
    }
)
```

### Get Vendor Balance

```python
balance = client.marketplace.get_vendor_balance(vendor_id="vendor_123")
```

---

## Payment Links

### Create Payment Link

```python
payment_link = client.payment_links.create(
    amount=1000,
    currency="USD",
    description="Product Purchase",
    customer_id="cust_123",
    expires_at="2025-01-31T23:59:59Z",
    metadata={
        "order_id": "order_123"
    }
)
```

### Get Payment Link

```python
payment_link = client.payment_links.retrieve(link_id="link_123")
```

### List Payment Links

```python
payment_links = client.payment_links.list(limit=10)
```

### Deactivate Payment Link

```python
payment_link = client.payment_links.deactivate(link_id="link_123")
```

---

## Error Handling

### Try-Except Pattern

```python
from onerouter.exceptions import OneRouterError, ValidationError, AuthenticationError, PaymentError

try:
    payment = client.payments.create(
        amount=1000,
        currency="USD",
        customer_id="cust_123"
    )
except ValidationError as e:
    print(f"Validation error: {e}")
    print(f"Details: {e.errors}")
except AuthenticationError as e:
    print(f"Authentication failed: {e}")
except PaymentError as e:
    print(f"Payment failed: {e}")
    print(f"Payment ID: {e.payment_id}")
except OneRouterError as e:
    print(f"API error: {e}")
```

### Error Properties

```python
try:
    payment = client.payments.create(...)
except OneRouterError as e:
    print(f"Status: {e.status}")
    print(f"Code: {e.code}")
    print(f"Message: {e.message}")
    print(f"Details: {e.details}")
    print(f"Request ID: {e.request_id}")
```

---

## Advanced Features

### Idempotency

```python
payment = client.payments.create(
    amount=1000,
    currency="USD",
    customer_id="cust_123",
    idempotency_key="unique_key_123"
)
```

### Custom Headers

```python
payment = client.payments.create(
    amount=1000,
    currency="USD",
    customer_id="cust_123",
    headers={
        "X-Custom-Header": "value"
    }
)
```

### Webhook Signature Verification

```python
import hashlib
import hmac

def verify_webhook_signature(payload, signature, secret):
    expected_signature = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(signature, expected_signature)
```

### Rate Limiting

The SDK automatically handles rate limiting with exponential backoff.

```python
client = onerouter.Client(
    api_key="your_api_key",
    base_url="https://api.onerouter.com",
    max_retries=5,  # Increase retries for rate-limited requests
    retry_delay=2  # Initial delay
)
```

---

## Examples

### Complete Payment Flow with Saved Methods

```python
import onerouter

client = onerouter.Client(
    api_key="your_api_key",
    base_url="https://api.onerouter.com"
)

# Save payment method
payment_method = client.saved_payment_methods.create(
    customer_id="cust_123",
    payment_method={
        "type": "card",
        "card": {
            "number": "4242424242424242",
            "expiry_month": "12",
            "expiry_year": "2025",
            "cvv": "123"
        }
    },
    is_default=True
)

# Use saved payment method for first payment
payment1 = client.payments.create(
    amount=1000,
    currency="USD",
    customer_id="cust_123",
    payment_method_id=payment_method["id"]
)

# Use saved payment method for second payment
payment2 = client.payments.create(
    amount=500,
    currency="USD",
    customer_id="cust_123",
    payment_method_id=payment_method["id"]
)
```

### Subscription with Trial and Plan Change

```python
import onerouter

client = onerouter.Client(
    api_key="your_api_key",
    base_url="https://api.onerouter.com"
)

# Create subscription with trial
subscription = client.subscriptions.create(
    plan_id="plan_monthly",
    customer_id="cust_123",
    trial_days=14
)

# Pause subscription after trial
subscription = client.subscriptions.pause(
    subscription_id=subscription["id"],
    pause_at="cycle_end"
)

# Resume subscription
subscription = client.subscriptions.resume(subscription_id=subscription["id"])

# Upgrade to yearly plan
subscription = client.subscriptions.update(
    subscription_id=subscription["id"],
    plan_id="plan_yearly",
    proration_behavior="create_prorations"
)
```

### Marketplace Split Payment

```python
import onerouter

client = onerouter.Client(
    api_key="your_api_key",
    base_url="https://api.onerouter.com"
)

# Create vendors
vendor1 = client.marketplace.create_vendor(
    name="Vendor 1",
    email="vendor1@example.com",
    bank_account={...}
)

vendor2 = client.marketplace.create_vendor(
    name="Vendor 2",
    email="vendor2@example.com",
    bank_account={...}
)

# Create split payment
payment = client.marketplace.create_split_payment(
    amount=10000,
    currency="USD",
    customer_id="cust_123",
    splits=[
        {
            "vendor_id": vendor1["id"],
            "amount": 8000,
            "type": "flat"
        },
        {
            "vendor_id": vendor2["id"],
            "amount": 1500,
            "type": "flat"
        }
    ],
    platform_fee={
        "amount": 500,
        "type": "flat"
    }
)
```

### UPI Payment with Phone Number

```python
import onerouter

client = onerouter.Client(
    api_key="your_api_key",
    base_url="https://api.onerouter.com"
)

payment = client.payments.create(
    amount=50000,
    currency="INR",
    customer_id="cust_123",
    payment_method={
        "type": "upi",
        "upi": {
            "phone": "+919876543210"
        }
    }
)
```

---

## Support

- **Documentation**: https://docs.onerouter.com
- **GitHub**: https://github.com/onerouter/onerouter-python
- **Support**: support@onerouter.com

## License

MIT License - see LICENSE file for details
