# Quick Start Guide

Get up and running with OneRouter SDK in 5 minutes.

## Installation

```bash
pip install onerouter
```

## Your First Payment

### Step 1: Initialize the Client

```python
import onerouter

client = onerouter.Client(
    api_key="your_api_key_here",
    base_url="https://api.onerouter.com"
)
```

### Step 2: Create a Payment

```python
payment = client.payments.create(
    amount=1000,  # $10.00 in cents
    currency="USD",
    customer_id="customer_123",
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

print(f"Payment created: {payment['id']}")
print(f"Status: {payment['status']}")
```

### Step 3: Handle the Response

```python
if payment['status'] == 'succeeded':
    print("Payment successful!")
elif payment['status'] == 'requires_action':
    print("Payment requires additional action")
    print(f"Action URL: {payment['next_action']['url']}")
else:
    print(f"Payment failed: {payment['error']['message']}")
```

## Payment Methods

### UPI Payment (India)

```python
payment = client.payments.create(
    amount=50000,  # ₹500
    currency="INR",
    customer_id="customer_123",
    payment_method={
        "type": "upi",
        "upi": {
            "vpa": "customer@upi"
        }
    }
)
```

### Card with EMI

```python
payment = client.payments.create(
    amount=10000,
    currency="INR",
    customer_id="customer_123",
    payment_method={
        "type": "card",
        "card": {
            "number": "4242424242424242",
            "expiry_month": "12",
            "expiry_year": "2025",
            "cvv": "123"
        }
    },
    emi={
        "tenure": 6  # 6 months EMI
    }
)
```

### Wallet Payment

```python
payment = client.payments.create(
    amount=1000,
    currency="INR",
    customer_id="customer_123",
    payment_method={
        "type": "wallet",
        "wallet": {
            "provider": "paytm",
            "wallet_id": "wallet_123"
        }
    }
)
```

## Subscription with Trial

```python
subscription = client.subscriptions.create(
    plan_id="plan_monthly",
    customer_id="customer_123",
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

## Save Payment Method for Later Use

```python
# Save payment method
payment_method = client.saved_payment_methods.create(
    customer_id="customer_123",
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

# Use saved payment method
payment = client.payments.create(
    amount=1000,
    currency="USD",
    customer_id="customer_123",
    payment_method_id=payment_method['id']
)
```

## Error Handling

```python
from onerouter.exceptions import OneRouterError

try:
    payment = client.payments.create(
        amount=1000,
        currency="USD",
        customer_id="customer_123",
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
except OneRouterError as e:
    print(f"Error: {e.message}")
    print(f"Status: {e.status}")
    print(f"Code: {e.code}")
```

## Next Steps

- [Complete Documentation](README.md)
- [Payment Methods Guide](README.md#payment-methods)
- [Subscriptions Guide](README.md#subscriptions)
- [Marketplace Features](README.md#marketplace)
- [Examples](../examples/)

## Support

- **Documentation**: https://docs.onerouter.com
- **GitHub**: https://github.com/onerouter/onerouter-python
- **Email**: support@onerouter.com
