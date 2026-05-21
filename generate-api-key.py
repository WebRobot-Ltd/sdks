#!/usr/bin/env python3
"""
Script semplice per generare API Keys per test con l'API WebRobot
Genera una coppia key_id:secret nel formato atteso dall'API Jersey
"""

import hmac
import os
import secrets
import hashlib
import sys

def generate_api_key():
    """Generate a new API key pair (key_id:secret)"""
    # Generate key_id (8 characters)
    key_id = secrets.token_urlsafe(6)
    
    # Generate secret (32 characters)
    secret = secrets.token_urlsafe(24)
    
    # Create full API key
    api_key = f"{key_id}:{secret}"
    
    # Hash the secret for storage using HMAC-SHA256 (same as dashboard)
    pepper = os.getenv('APIKEY_PEPPER', 'changeme-pepper')
    secret_hash = hmac.new(pepper.encode(), secret.encode(), hashlib.sha256).hexdigest()
    
    return key_id, secret, api_key, secret_hash

def main():
    print("🔑 Generatore API Key per WebRobot")
    print("=" * 60)
    print()
    
    # Generate API key
    key_id, secret, api_key, secret_hash = generate_api_key()
    
    print("✅ API Key generata con successo!")
    print()
    print("📋 Dettagli:")
    print(f"   Key ID:     {key_id}")
    print(f"   Secret:     {secret}")
    print(f"   API Key:    {api_key}")
    print(f"   SHA-256:    {secret_hash[:32]}...")
    print()
    print("=" * 60)
    print()
    print("📝 Utilizzo:")
    print()
    print("1. Con cURL:")
    print(f'   curl -H "X-API-Key: {api_key}" \\')
    print('        https://api.webrobot.eu/api/webrobot/api/projects')
    print()
    print("2. Con Python SDK:")
    print(f"   configuration.api_key['X-API-Key'] = '{api_key}'")
    print()
    print("3. Con TypeScript SDK:")
    print(f"   const config = {{ apiKey: '{api_key}' }}")
    print()
    print("=" * 60)
    print()
    print("⚠️  NOTA: Per utilizzare questa API key in produzione, ")
    print("   deve essere registrata nel database Strapi.")
    print()
    print("   Per testing locale, usa la dev key:")
    print("   dev-key-12345:dev-secret-67890")
    print()

if __name__ == "__main__":
    main()

