from typing import Optional, Dict, Any

from ..http_client import HTTPClient


class SMSResource:
    """SMS communication operations"""

    def __init__(self, client: HTTPClient):
        self.client = client

    async def send(
        self,
        to: str,
        body: str,
        from_number: Optional[str] = None,
        provider: str = "twilio",
        idempotency_key: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send SMS message

        Args:
            to: Recipient phone number (E.164 format, e.g., +1234567890)
            body: SMS message content (1-1600 characters)
            from_number: Override default from number (optional)
            provider: Service provider (default: twilio)
            idempotency_key: Prevent duplicate requests (optional)

        Returns:
            Dict with message_id, status, service, cost

        Example:
            >>> await client.sms.send(
            ...     to="+1234567890",
            ...     body="Your OTP is 123456. Valid for 10 minutes."
            ... )
            {
                "message_id": "SM123456789",
                "status": "sent",
                "service": "twilio",
                "cost": 0.0079,
                "currency": "USD"
            }
        """
        data = {
            "to": to,
            "body": body,
            "provider": provider
        }

        if from_number:
            data["from_number"] = from_number
        if idempotency_key:
            data["idempotency_key"] = idempotency_key

        return await self.client.request(
            method="POST",
            endpoint="/v1/sms",
            data=data
        )

    async def get_status(self, message_id: str) -> Dict[str, Any]:
        """
        Get SMS delivery status

        Args:
            message_id: SMS message ID from send() response

        Returns:
            Dict with message_id, status, provider_data
        """
        return await self.client.request(
            method="GET",
            endpoint=f"/v1/sms/{message_id}"
        )
