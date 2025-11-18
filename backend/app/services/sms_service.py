"""
SMS Service
SMS.ru API integration for sending OTP codes

See: docs/requirements/module-01-mobile-app.md (Function 1.1.3)
     docs/backend/services/auth-service.md (SMS OTP Integration)

API Documentation: https://sms.ru/api
"""

import logging
from typing import Optional, Dict, Any
import httpx

from app.core.config import settings


logger = logging.getLogger(__name__)


class SMSService:
    """
    SMS.ru API client for sending OTP codes

    Configuration:
        - API Key: settings.SMS_RU_API_KEY
        - Base URL: https://sms.ru/sms/send

    SMS.ru API Response Format:
        Success:
            {
                "status": "OK",
                "status_code": 100,
                "sms": {
                    "79991234567": {
                        "status": "OK",
                        "status_code": 100,
                        "sms_id": "123456-789"
                    }
                },
                "balance": 1234.56
            }

        Error:
            {
                "status": "ERROR",
                "status_code": 200,  # Error code (see docs)
                "status_text": "Error description"
            }

    Status Codes:
        100 - Message sent successfully
        200 - Invalid API key
        201 - Insufficient balance
        202 - Invalid recipient
        203 - No message text
        204 - Invalid sender name
        205 - Message too long
        206 - Exceeded daily limit
        207 - Phone number forbidden
        208 - Wrong time for sending

    Rate Limiting:
        - Max 5 OTP codes per phone per hour (enforced in auth service)
        - Max 100 SMS per day per API key (SMS.ru limit)
    """

    BASE_URL = "https://sms.ru/sms/send"

    @staticmethod
    async def send_otp(phone: str, code: str) -> Dict[str, Any]:
        """
        Send OTP code via SMS

        Args:
            phone: Phone number in format +7XXXXXXXXXX or 79XXXXXXXXXX
            code: 6-digit OTP code

        Returns:
            Dict with status and SMS ID:
            {
                "success": bool,
                "sms_id": str | None,
                "status_code": int,
                "status_text": str,
                "balance": float | None
            }

        Raises:
            httpx.HTTPError: If HTTP request fails

        Example:
            >>> result = await SMSService.send_otp("+79991234567", "123456")
            >>> if result["success"]:
            ...     print(f"SMS sent, ID: {result['sms_id']}")
        """

        # Validate API key
        if not settings.SMS_RU_API_KEY:
            logger.error("SMS_RU_API_KEY not configured")
            return {
                "success": False,
                "sms_id": None,
                "status_code": 0,
                "status_text": "SMS service not configured (missing API key)",
                "balance": None
            }

        # Normalize phone number (remove + if present)
        normalized_phone = phone.replace("+", "")

        # Validate phone format (must be 11 digits starting with 7)
        if not normalized_phone.isdigit() or len(normalized_phone) != 11 or not normalized_phone.startswith("7"):
            logger.error(f"Invalid phone format: {phone}")
            return {
                "success": False,
                "sms_id": None,
                "status_code": 202,
                "status_text": "Invalid phone number format",
                "balance": None
            }

        # Prepare SMS message
        message = f"Ваш код подтверждения: {code}\n\nСвой Круг"

        # Prepare request parameters
        params = {
            "api_id": settings.SMS_RU_API_KEY,
            "to": normalized_phone,
            "msg": message,
            "json": 1,  # Request JSON response
        }

        try:
            # Send HTTP request to SMS.ru API
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(self.BASE_URL, params=params)
                response.raise_for_status()

                # Parse JSON response
                data = response.json()

                # Check overall status
                if data.get("status") == "OK" and data.get("status_code") == 100:
                    # Extract SMS ID from response
                    sms_data = data.get("sms", {}).get(normalized_phone, {})
                    sms_id = sms_data.get("sms_id")
                    balance = data.get("balance")

                    logger.info(
                        f"SMS sent successfully to {phone}, "
                        f"ID: {sms_id}, Balance: {balance}"
                    )

                    return {
                        "success": True,
                        "sms_id": sms_id,
                        "status_code": 100,
                        "status_text": "OK",
                        "balance": balance
                    }
                else:
                    # SMS.ru returned error
                    status_code = data.get("status_code", 0)
                    status_text = data.get("status_text", "Unknown error")

                    logger.error(
                        f"SMS.ru API error: {status_code} - {status_text} "
                        f"(phone: {phone})"
                    )

                    return {
                        "success": False,
                        "sms_id": None,
                        "status_code": status_code,
                        "status_text": status_text,
                        "balance": data.get("balance")
                    }

        except httpx.HTTPError as e:
            logger.exception(f"HTTP error sending SMS to {phone}: {str(e)}")
            return {
                "success": False,
                "sms_id": None,
                "status_code": 0,
                "status_text": f"HTTP error: {str(e)}",
                "balance": None
            }

        except Exception as e:
            logger.exception(f"Unexpected error sending SMS to {phone}: {str(e)}")
            return {
                "success": False,
                "sms_id": None,
                "status_code": 0,
                "status_text": f"Unexpected error: {str(e)}",
                "balance": None
            }

    @staticmethod
    async def check_balance() -> Optional[float]:
        """
        Check SMS.ru account balance

        Returns:
            Balance in rubles, or None if check failed

        Example:
            >>> balance = await SMSService.check_balance()
            >>> print(f"Current balance: {balance} RUB")
        """

        if not settings.SMS_RU_API_KEY:
            logger.error("SMS_RU_API_KEY not configured")
            return None

        url = "https://sms.ru/my/balance"
        params = {
            "api_id": settings.SMS_RU_API_KEY,
            "json": 1
        }

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(url, params=params)
                response.raise_for_status()

                data = response.json()

                if data.get("status") == "OK":
                    balance = data.get("balance")
                    logger.info(f"SMS.ru balance: {balance} RUB")
                    return balance
                else:
                    logger.error(f"SMS.ru balance check failed: {data}")
                    return None

        except Exception as e:
            logger.exception(f"Error checking SMS.ru balance: {str(e)}")
            return None

    @staticmethod
    def format_phone_for_display(phone: str) -> str:
        """
        Format phone number for display

        Args:
            phone: Phone number in format +7XXXXXXXXXX or 79XXXXXXXXXX

        Returns:
            Formatted phone: +7 999 123-45-67

        Example:
            >>> formatted = SMSService.format_phone_for_display("+79991234567")
            >>> print(formatted)  # +7 999 123-45-67
        """
        # Remove +
        normalized = phone.replace("+", "")

        # Validate length
        if len(normalized) != 11:
            return phone  # Return as-is if invalid

        # Format: +7 999 123-45-67
        return f"+{normalized[0]} {normalized[1:4]} {normalized[4:7]}-{normalized[7:9]}-{normalized[9:11]}"


# ===================================================================
# Mock SMS Service (for testing/development)
# ===================================================================
class MockSMSService:
    """
    Mock SMS service for testing/development

    Instead of sending real SMS, logs the code to console.
    Useful for:
    - Local development without SMS.ru API key
    - Integration tests
    - Preview environments

    Usage:
        Set SMS_RU_API_KEY to empty string to automatically use mock service
    """

    @staticmethod
    async def send_otp(phone: str, code: str) -> Dict[str, Any]:
        """
        Mock send OTP - logs to console instead of sending SMS

        Args:
            phone: Phone number
            code: OTP code

        Returns:
            Success response with mock SMS ID
        """
        logger.warning(
            f"[MOCK SMS] OTP code for {phone}: {code} "
            f"(expires in {settings.SMS_OTP_EXPIRE_MINUTES} minutes)"
        )

        # Print to console for visibility during development
        print(f"\n{'='*60}")
        print(f"📱 MOCK SMS SENT TO {phone}")
        print(f"🔐 OTP CODE: {code}")
        print(f"⏰ EXPIRES IN: {settings.SMS_OTP_EXPIRE_MINUTES} minutes")
        print(f"{'='*60}\n")

        return {
            "success": True,
            "sms_id": f"mock_{phone}_{code}",
            "status_code": 100,
            "status_text": "OK (mock)",
            "balance": 9999.99
        }

    @staticmethod
    async def check_balance() -> Optional[float]:
        """Mock balance check"""
        return 9999.99


# ===================================================================
# Factory function to get appropriate service
# ===================================================================
def get_sms_service() -> type:
    """
    Get SMS service (real or mock)

    Returns:
        SMSService class if API key configured, MockSMSService otherwise

    Usage:
        >>> service = get_sms_service()
        >>> result = await service.send_otp("+79991234567", "123456")
    """
    if settings.SMS_RU_API_KEY:
        return SMSService
    else:
        logger.info("Using MockSMSService (SMS_RU_API_KEY not configured)")
        return MockSMSService
