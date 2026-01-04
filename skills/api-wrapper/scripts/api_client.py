#!/usr/bin/env python3
"""
Base API client with authentication and error handling.
"""

import os
import requests
import time
from typing import Optional, Dict, Any


class APIClient:
    """Base API client with common functionality."""

    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        timeout: int = 30,
        max_retries: int = 3
    ):
        """
        Initialize API client.

        Args:
            base_url: Base URL for the API
            api_key: API key for authentication
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key or os.getenv('API_KEY')
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()

        if self.api_key:
            self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})

    def request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict] = None,
        json: Optional[Dict] = None,
        headers: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Make an HTTP request with retries and error handling.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            params: Query parameters
            json: JSON request body
            headers: Additional headers

        Returns:
            Parsed JSON response

        Raises:
            requests.HTTPError: For HTTP errors
            requests.Timeout: For timeout errors
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        for attempt in range(self.max_retries):
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    params=params,
                    json=json,
                    headers=headers,
                    timeout=self.timeout
                )
                response.raise_for_status()
                return response.json()

            except requests.Timeout:
                if attempt == self.max_retries - 1:
                    raise
                print(f"⚠️  Timeout, retrying... ({attempt + 1}/{self.max_retries})")
                time.sleep(2 ** attempt)

            except requests.HTTPError as e:
                if e.response.status_code >= 500 and attempt < self.max_retries - 1:
                    print(f"⚠️  Server error, retrying... ({attempt + 1}/{self.max_retries})")
                    time.sleep(2 ** attempt)
                else:
                    raise

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a GET request."""
        return self.request('GET', endpoint, params=params)

    def post(self, endpoint: str, json: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a POST request."""
        return self.request('POST', endpoint, json=json)

    def put(self, endpoint: str, json: Optional[Dict] = None) -> Dict[str, Any]:
        """Make a PUT request."""
        return self.request('PUT', endpoint, json=json)

    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Make a DELETE request."""
        return self.request('DELETE', endpoint)


# Example usage
if __name__ == "__main__":
    # Example: GitHub API client
    client = APIClient(
        base_url="https://api.github.com",
        api_key=os.getenv('GITHUB_TOKEN')
    )

    try:
        user = client.get('/user')
        print(f"✅ Authenticated as: {user.get('login')}")
    except Exception as e:
        print(f"❌ Error: {e}")
