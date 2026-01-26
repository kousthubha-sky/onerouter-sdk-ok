from typing import Optional, Dict, Any

from ..http_client import HTTPClient


class PaymentLinksResource:
    """Payment link operations"""

    def __init__(self, client: HTTPClient):
        self.client = client

    async def create(
        self,
        amount: float,
        description: str,
        customer_email: Optional[str] = None,
        callback_url: Optional[str] = None,
        notes: Optional[Dict[str, str]] = None,
        environment: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a payment link

        Args:
            amount: Payment amount in currency units
            description: Payment description
            customer_email: Customer's email address
            callback_url: URL to redirect after payment completion
            notes: Additional metadata (e.g., user_id, credits, type)
            environment: Override environment for credential selection ("test" or "live")

        Returns:
            Dict containing payment link details including id and short_url
        """
        data = {
            "amount": amount,
            "description": description
        }

        if customer_email:
            data["customer_email"] = customer_email

        if callback_url:
            data["callback_url"] = callback_url

        if notes:
            data["notes"] = notes

        if environment:
            data["environment"] = environment

        return await self.client.request(
            method="POST",
            endpoint="/v1/payment-links",
            data=data
        )