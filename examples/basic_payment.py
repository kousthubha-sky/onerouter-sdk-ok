"""
OneRouter SDK - Basic Payment Example

This example demonstrates how to create a basic payment using the OneRouter SDK.
"""

import asyncio
from onerouter import OneRouter, APIError

async def create_basic_payment():
    """
    Create a basic payment using the SDK
    """
    # Initialize the client
    client = OneRouter(
        api_key="unf_live_xxx",
        base_url="https://api.onerouter.com"
    )
    
    try:
        # Create a payment
        payment = await client.payments.create(
            amount=500.00,  # ₹500
            currency="INR",
            method="upi",
            receipt="order_456",
            notes={"description": "Product purchase"}
        )
        
        print("Payment created successfully!")
        print(f"Transaction ID: {payment['transaction_id']}")
        print(f"Status: {payment['status']}")
        print(f"Amount: ₹{payment['amount']}")
        print(f"Checkout URL: {payment['checkout_url']}")
        
        return payment
        
    except APIError as e:
        print(f"Error creating payment: {e}")
        print(f"Status Code: {e.status_code}")
        return None

async def retrieve_payment(transaction_id):
    """
    Retrieve a payment by transaction ID
    """
    client = OneRouter(
        api_key="unf_live_xxx",
        base_url="https://api.onerouter.com"
    )
    
    try:
        payment = await client.payments.get(transaction_id)
        print(f"Transaction ID: {payment['transaction_id']}")
        print(f"Status: {payment['status']}")
        print(f"Amount: ₹{payment['amount']}")
        return payment
    except APIError as e:
        print(f"Error retrieving payment: {e}")
        return None

async def refund_payment(payment_id):
    """
    Refund a payment
    """
    client = OneRouter(
        api_key="unf_live_xxx",
        base_url="https://api.onerouter.com"
    )
    
    try:
        # Full refund
        refund = await client.payments.refund(
            payment_id=payment_id,
            reason="customer_request"
        )
        
        print("Refund initiated successfully!")
        print(f"Refund ID: {refund.get('refund_id', 'N/A')}")
        print(f"Amount: ₹{refund.get('amount', 'N/A')}")
        
        return refund
    except APIError as e:
        print(f"Error refunding payment: {e}")
        return None

async def main():
    # Create a payment
    payment = await create_basic_payment()
    
    if payment:
        # Retrieve the payment
        await retrieve_payment(payment['transaction_id'])
        
        # Refund the payment (example)
        # await refund_payment(payment['transaction_id'])

if __name__ == "__main__":
    asyncio.run(main())
