# OneRouter SDK Examples

This directory contains example code demonstrating how to use the OneRouter SDK.

## Examples

### [basic_payment.py](basic_payment.py)
Demonstrates basic payment operations:
- Creating a payment
- Retrieving payment details
- Refunding a payment

### [subscription_management.py](subscription_management.py)
Demonstrates subscription operations:
- Creating subscriptions with trial periods
- Pausing and resuming subscriptions
- Cancelling subscriptions
- Updating subscription plans

### [payment_methods.py](payment_methods.py)
Demonstrates different payment methods:
- UPI payments
- Card payments with EMI
- Wallet payments
- Net banking

### [saved_payment_methods.py](saved_payment_methods.py)
Demonstrates saved payment methods:
- Saving payment methods for future use
- Listing saved payment methods
- Using saved payment methods for payments
- Deleting saved payment methods

### [marketplace.py](marketplace.py)
Demonstrates marketplace features:
- Creating vendor accounts
- Creating split payments
- Managing vendor balances
- Platform fee configuration

## Running the Examples

Each example file can be run independently:

```bash
python examples/basic_payment.py
python examples/subscription_management.py
```

## API Key

Before running the examples, replace `"unf_live_xxx"` with your actual OneRouter API key.

```python
client = OneRouter(
    api_key="your_actual_api_key_here",  # Replace with your API key
    base_url="https://api.onerouter.com"
)
```

## Async/Await

All SDK methods are async. Use `async/await` or the synchronous wrapper:

```python
# Async version
client = OneRouter(...)
payment = await client.payments.create(...)

# Sync version
from onerouter import OneRouterSync
client = OneRouterSync(...)
payment = client.payments.create(...)
```

## Error Handling

Always wrap SDK calls in try-except blocks:

```python
from onerouter import APIError

try:
    payment = await client.payments.create(...)
except APIError as e:
    print(f"Error: {e}")
    print(f"Status Code: {e.status_code}")
```

## Documentation

For complete API documentation, see:
- [Complete Documentation](../docs/README.md)
- [Quick Start Guide](../QUICKSTART.md)

## Support

- **Email**: support@onerouter.com
- **Documentation**: https://docs.onerouter.com
- **GitHub**: https://github.com/onerouter/onerouter-python
