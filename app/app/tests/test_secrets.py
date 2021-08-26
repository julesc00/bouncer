"""Tests for getting secrets"""
from unittest.mock import (patch, Mock)
from django.test import SimpleTestCase

from app import secrets


MOCK_GCP_PROJECT = "test-project"


@patch.dict(
    "os.environ", {
        "GOOGLE_CLOUD_PROJECT": MOCK_GCP_PROJECT,
        "GAE_APPLICATION": "yes",
    }
)
@patch("app.secrets.SecretManagerServiceClient")
class SecretManagerTests(SimpleTestCase):
    """Test getting config from secret manager."""

    def test_retrieve_secret(self, mock_sm):
        """Test getting a secret from secret manager."""
        
