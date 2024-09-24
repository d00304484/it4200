"""
This module contains unit tests for the Flask app.
"""

from app import app
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_hello():
    """Test the '/' route to ensure it returns 'Hello World!'"""
    response = app.test_client().get('/')
    assert response.data == b"Hello World!"
