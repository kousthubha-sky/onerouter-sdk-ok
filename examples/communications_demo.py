"""
OneRouter SDK Communications Examples

This file demonstrates how to use the OneRouter SDK to send
SMS and Email communications through a unified API.
"""

import asyncio
from onerouter import OneRouter


async def example_send_sms():
    """Example: Send SMS message"""
    client = OneRouter(api_key="your_api_key_here")

    # Send SMS
    sms = await client.sms.send(
        to="+1234567890",
        body="Your OTP is 123456. Valid for 10 minutes."
    )

    print("✅ SMS sent!")
    print(f"   Message ID: {sms['message_id']}")
    print(f"   Status: {sms['status']}")
    print(f"   Cost: ${sms['cost']:.4f}")
    print(f"   Created at: {sms['created_at']}")


async def example_send_email():
    """Example: Send HTML email"""
    client = OneRouter(api_key="your_api_key_here")

    # Send HTML email
    email = await client.email.send(
        to="user@example.com",
        subject="Welcome to Our Platform!",
        html_body="<h1>Welcome!</h1><p>Your account has been created successfully.</p>"
    )

    print("✅ Email sent!")
    print(f"   Email ID: {email['email_id']}")
    print(f"   Status: {email['status']}")
    print(f"   Cost: ${email['cost']:.4f}")
    print(f"   Created at: {email['created_at']}")


async def example_send_email_with_text():
    """Example: Send plain text email"""
    client = OneRouter(api_key="your_api_key_here")

    # Send plain text email
    email = await client.email.send(
        to="user@example.com",
        subject="Order Confirmation",
        text_body="Thank you for your order #12345!"
    )

    print("✅ Email sent!")
    print(f"   Email ID: {email['email_id']}")


async def example_get_sms_status():
    """Example: Get SMS delivery status"""
    client = OneRouter(api_key="your_api_key_here")

    # Get SMS status
    status = await client.sms.get_status("SM123456789")

    print("📨 SMS Status:")
    print(f"   Message ID: {status['message_id']}")
    print(f"   Status: {status['status']}")
    print(f"   Service: {status['service']}")


async def example_get_email_status():
    """Example: Get email delivery status"""
    client = OneRouter(api_key="your_api_key_here")

    # Get email status
    status = await client.email.get_status("EM123456789")

    print("📧 Email Status:")
    print(f"   Email ID: {status['email_id']}")
    print(f"   Status: {status['status']}")
    print(f"   Service: {status['service']}")


async def example_idempotent_sms():
    """Example: Send SMS with idempotency (prevents duplicates)"""
    import hashlib

    client = OneRouter(api_key="your_api_key_here")

    # Generate idempotency key from your order ID
    order_id = "order_12345"
    idempotency_key = hashlib.sha256(order_id.encode()).hexdigest()

    # Send SMS with idempotency
    sms = await client.sms.send(
        to="+1234567890",
        body="Your order #12345 has been shipped!",
        idempotency_key=idempotency_key
    )

    # If you send this exact request again, OneRouter returns the cached original SMS
    sms2 = await client.sms.send(
        to="+1234567890",
        body="Your order #12345 has been shipped!",
        idempotency_key=idempotency_key
    )

    print("✅ Same SMS (not sent again):", sms2['message_id'] == sms['message_id'])


async def example_payment_confirmation():
    """Example: Send payment confirmation via SMS"""
    client = OneRouter(api_key="your_api_key_here")

    # Send OTP via SMS
    await client.sms.send(
        to="+1234567890",
        body="Your payment of $99.99 was successful. Order #123456."
    )

    # Send receipt via email
    await client.email.send(
        to="user@example.com",
        subject="Payment Receipt - Order #123456",
        html_body="""
        <h1>Payment Successful</h1>
        <p>Thank you for your order!</p>
        <p><strong>Order #123456</strong></p>
        <p><strong>Amount:</strong> $99.99</p>
        <p><strong>Date:</strong> January 15, 2025</p>
        """
    )


async def example_welcome_email():
    """Example: Send welcome email with verification link"""
    client = OneRouter(api_key="your_api_key_here")

    # Send welcome email
    await client.email.send(
        to="newuser@example.com",
        subject="Welcome to Our Platform!",
        html_body="""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <h1 style="color: #333;">Welcome to Our Platform!</h1>
            <p style="color: #666;">Thank you for signing up.</p>
            <p style="color: #666;">To verify your email, click the button below:</p>
            <a href="https://yourplatform.com/verify?token=abc123"
               style="display: inline-block; padding: 12px 24px; background: #00A3FF; color: white; text-decoration: none; border-radius: 4px;">
                Verify Email
            </a>
            <p style="color: #999;">Or copy and paste this link: https://yourplatform.com/verify?token=abc123</p>
        </div>
        """
    )


async def example_error_handling():
    """Example: Handle errors properly"""
    from onerouter import OneRouterException

    client = OneRouter(api_key="your_api_key_here")

    try:
        sms = await client.sms.send(
            to="+1234567890",
            body="Hello World!"
        )
        print("✅ SMS sent!")

    except OneRouterException as e:
        if e.status_code == 400:
            print("❌ Bad request - check phone number format")
        elif e.status_code == 401:
            print("❌ Invalid API key")
        elif e.status_code == 429:
            print("❌ Rate limit exceeded - wait and retry")
        else:
            print(f"❌ Error: {e.detail}")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")


async def main():
    """Run all examples"""
    print("="*60)
    print("ONEROUTER COMMUNICATIONS SDK EXAMPLES")
    print("="*60)

    print("\n1. Send SMS")
    await example_send_sms()

    print("\n2. Send HTML Email")
    await example_send_email()

    print("\n3. Send Plain Text Email")
    await example_send_email_with_text()

    print("\n4. Get SMS Status")
    await example_get_sms_status()

    print("\n5. Get Email Status")
    await example_get_email_status()

    print("\n6. Idempotent SMS (prevents duplicates)")
    await example_idempotent_sms()

    print("\n7. Payment Confirmation (SMS + Email)")
    await example_payment_confirmation()

    print("\n8. Welcome Email with HTML")
    await example_welcome_email()

    print("\n9. Error Handling")
    await example_error_handling()

    print("\n" + "="*60)
    print("✅ All examples completed!")
    print("="*60)


if __name__ == "__main__":
    asyncio.run(main())
