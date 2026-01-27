from typing import Optional, Dict, Any

from ..http_client import HTTPClient


class EmailResource:
    """Email communication operations"""

    def __init__(self, client: HTTPClient):
        self.client = client

    async def send(
        self,
        to: str,
        subject: str,
        html_body: Optional[str] = None,
        text_body: Optional[str] = None,
        from_email: Optional[str] = None,
        provider: str = "resend",
        idempotency_key: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send email message

        Args:
            to: Recipient email address
            subject: Email subject
            html_body: HTML email body (optional)
            text_body: Plain text email body (optional)
            from_email: Override default from email (optional)
            provider: Service provider (default: resend)
            idempotency_key: Prevent duplicate requests (optional)

        Returns:
            Dict with email_id, status, service, cost

        Example:
            >>> await client.email.send(
            ...     to="user@example.com",
            ...     subject="Welcome!",
            ...     html_body="<h1>Welcome!</h1><p>Your account is ready.</p>"
            ... )
            {
                "email_id": "EM123456789",
                "status": "sent",
                "service": "resend",
                "cost": 0.0001,
                "currency": "USD"
            }
        """
        if not html_body and not text_body:
            raise ValueError("Either html_body or text_body is required")

        data = {
            "to": to,
            "subject": subject,
            "provider": provider
        }

        if html_body:
            data["html_body"] = html_body
        if text_body:
            data["text_body"] = text_body
        if from_email:
            data["from_email"] = from_email
        if idempotency_key:
            data["idempotency_key"] = idempotency_key

        return await self.client.request(
            method="POST",
            endpoint="/v1/email",
            data=data
        )

    async def get_status(self, email_id: str) -> Dict[str, Any]:
        """
        Get email delivery status

        Args:
            email_id: Email ID from send() response

        Returns:
            Dict with email_id, status, provider_data
        """
        return await self.client.request(
            method="GET",
            endpoint=f"/v1/email/{email_id}"
        )
