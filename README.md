# WebRobot API SDKs

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PHP](https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white)](https://www.php.net/)
[![Go](https://img.shields.io/badge/Go-00ADD8?logo=go&logoColor=white)](https://golang.org/)

SDK ufficiali per l'API WebRobot Jersey, generati automaticamente dall'OpenAPI specification.

## 🚀 Quick Start

### TypeScript SDK
```bash
cd typescript-sdk
npm install
```

### Python SDK
```bash
cd python-sdk
pip install -r requirements.txt
pip install -e .
```

### PHP SDK
```bash
cd php-sdk
composer install
```

### Go SDK
```bash
cd go-sdk
go mod tidy
```

## 📖 Documentation

- [TypeScript SDK Documentation](typescript-sdk/README.md)
- [Python SDK Documentation](python-sdk/README.md)
- [PHP SDK Documentation](php-sdk/README.md)
- [Go SDK Documentation](go-sdk/README.md)

## 🔗 API Reference

- **OpenAPI Specification**: https://api.webrobot.eu/api/openapi.json
- **API Base URL**: https://api.webrobot.eu
- **API Documentation**: https://api.webrobot.eu/api/docs

## 🛠️ Development

### Regenerating SDKs

To regenerate all SDKs from the latest OpenAPI specification:

```bash
# Download latest OpenAPI spec
curl -s https://api.webrobot.eu/api/openapi.json -o openapi.json

# Generate all SDKs
./generate-sdks.sh
```

### Testing

Each SDK includes comprehensive tests:

```bash
# TypeScript
cd typescript-sdk && npm test

# Python
cd python-sdk && pytest

# PHP
cd php-sdk && ./vendor/bin/phpunit

# Go
cd go-sdk && go test -v ./...
```

## 📦 Package Managers

### NPM (TypeScript)
```bash
npm install @webrobot-ltd/typescript-sdk
```

### PyPI (Python)
```bash
pip install webrobot-python-sdk
```

### Composer (PHP)
```bash
composer require webrobot-ltd/php-sdk
```

### Go Modules (Go)
```go
import "github.com/WebRobot-Ltd/sdks/go-sdk"
```

## 🔑 Authentication

All SDKs support multiple authentication methods:

- **API Key**: `X-API-Key: your-api-key`
- **Bearer Token**: `Authorization: Bearer your-token`
- **JWT Token**: `Authorization: Bearer your-jwt-token`

## 📋 API Coverage

✅ **Complete API Coverage**:
- Projects Management
- Categories Management  
- Agents Management
- Jobs Management
- Tasks Management
- Datasets Management
- AI Providers
- Python Extensions
- Strapi Tables
- Cloud Services
- Scheduler (Cronjobs)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Support

- **Email**: support@webrobot.eu
- **Issues**: [GitHub Issues](https://github.com/WebRobot-Ltd/sdks/issues)
- **Documentation**: [API Docs](https://api.webrobot.eu/api/docs)

## 🏢 WebRobot

WebRobot is a comprehensive platform for AI-powered data processing and automation.

- **Website**: https://webrobot.eu
- **API**: https://api.webrobot.eu
- **Documentation**: https://docs.webrobot.eu

---

**Generated on**: $(date)
**OpenAPI Version**: 3.0.1
**SDK Version**: 1.0.0