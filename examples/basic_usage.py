import asyncio
from onerouter import OneRouter

async def main():
    # Initialize client
    async with OneRouter(api_key="unf_test_xxx") as client:

        print("=== OneRouter SDK Example ===\n")

        # 1. Create Payment
        print("1. Creating payment order...")
        order = await client.payments.create(
            amount=500.00,
            currency="INR",
            receipt="demo_order_123"
        )
        print(f"✓ Order created: {order['transaction_id']}")
        print(f"  Amount: ₹{order['amount']}")
        print(f"  Checkout URL: {order['checkout_url']}\n")

        # 2. Get Payment Status
        print("2. Checking payment status...")
        status = await client.payments.get(order['transaction_id'])
        print(f"✓ Payment status: {status['status']}\n")

        # 3. Create Subscription
        print("3. Creating subscription...")
        subscription = await client.subscriptions.create(
            plan_id="plan_monthly_99",
            customer_notify=True
        )
        print(f"✓ Subscription created: {subscription['id']}\n")

        # 4. Create Payment Link
        print("4. Creating payment link...")
        link = await client.payment_links.create(
            amount=999.00,
            description="Premium Plan - Annual",
            customer_email="demo@example.com"
        )
        print(f"✓ Payment link: {link['short_url']}\n")

        print("=== All operations completed successfully! ===")

if __name__ == "__main__":
    asyncio.run(main())