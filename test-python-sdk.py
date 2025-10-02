#!/usr/bin/env python3
"""
Test script per Python SDK
Verifica che gli endpoint funzionino correttamente
"""

import sys
sys.path.insert(0, 'python-sdk')

import webrobot
from webrobot.api import default_api
from webrobot.configuration import Configuration
from webrobot.exceptions import ApiException

def test_python_sdk():
    print("🧪 Testing WebRobot Python SDK")
    print("=" * 50)
    
    # Configurazione
    configuration = Configuration(
        host='https://api.webrobot.eu'
    )
    configuration.api_key['X-API-Key'] = 'test:secret'
    
    # Test counter
    passed = 0
    failed = 0
    
    with webrobot.ApiClient(configuration) as api_client:
        api = default_api.DefaultApi(api_client)
        
        tests = [
            ("List Projects", lambda: api.get_projects()),
            ("List Categories", lambda: api.get_categories()),
            ("Create Category", lambda: api.create_category(body={'name': 'Test Category'})),
        ]
        
        for name, test_func in tests:
            try:
                print(f"\n🔍 Testing: {name}")
                result = test_func()
                print(f"✅ {name}: SUCCESS")
                print(f"   Response type: {type(result)}")
                passed += 1
            except ApiException as e:
                print(f"❌ {name}: FAILED")
                print(f"   Status: {e.status}")
                print(f"   Reason: {e.reason}")
                failed += 1
            except Exception as e:
                print(f"❌ {name}: ERROR")
                print(f"   Error: {str(e)}")
                failed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! Python SDK is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
    
    return passed, failed

if __name__ == "__main__":
    passed, failed = test_python_sdk()
    sys.exit(0 if failed == 0 else 1)

