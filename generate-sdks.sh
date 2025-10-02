#!/bin/bash
#
# Script per generare SDK da OpenAPI JSON
# Genera SDK per: TypeScript, Python, PHP, Go
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OPENAPI_FILE="$SCRIPT_DIR/webrobot-frontend-sdk/openapi.json"
OUTPUT_DIR="$SCRIPT_DIR/generated-sdks"

# Colori per output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  WebRobot SDK Generator (OpenAPI)${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"

# Verifica che esista il file OpenAPI
if [ ! -f "$OPENAPI_FILE" ]; then
    echo -e "${YELLOW}⚠️  OpenAPI file not found. Downloading from API...${NC}"
    curl -s https://api.webrobot.eu/api/openapi.json -o "$OPENAPI_FILE"
    echo -e "${GREEN}✅ OpenAPI downloaded${NC}"
fi

# Crea directory output
mkdir -p "$OUTPUT_DIR"

# Funzione per generare SDK
generate_sdk() {
    local language=$1
    local generator=$2
    local output_name=$3
    
    echo -e "\n${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}🔧 Generating ${language} SDK...${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    
    docker run --rm \
        -v "$OPENAPI_FILE":/openapi.json \
        -v "$OUTPUT_DIR":/output \
        openapitools/openapi-generator-cli generate \
        -i /openapi.json \
        -g "$generator" \
        -o "/output/$output_name" \
        --skip-validate-spec \
        --additional-properties=packageName=webrobot,packageVersion=1.0.0
    
    echo -e "${GREEN}✅ ${language} SDK generated in: $OUTPUT_DIR/$output_name${NC}"
}

# ============================================================================
# TYPESCRIPT SDK
# ============================================================================
generate_sdk "TypeScript" "typescript-fetch" "typescript-sdk"

# ============================================================================
# PYTHON SDK
# ============================================================================
generate_sdk "Python" "python" "python-sdk"

# ============================================================================
# PHP SDK
# ============================================================================
generate_sdk "PHP" "php" "php-sdk"

# ============================================================================
# GO SDK
# ============================================================================
generate_sdk "Go" "go" "go-sdk"

# ============================================================================
# SUMMARY
# ============================================================================
echo -e "\n${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}🎉 All SDKs generated successfully!${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${YELLOW}📦 Generated SDKs:${NC}"
echo -e "  • TypeScript: $OUTPUT_DIR/typescript-sdk"
echo -e "  • Python:     $OUTPUT_DIR/python-sdk"
echo -e "  • PHP:        $OUTPUT_DIR/php-sdk"
echo -e "  • Go:         $OUTPUT_DIR/go-sdk"
echo ""
echo -e "${YELLOW}📖 Documentation:${NC}"
echo -e "  Each SDK includes its own README with usage examples"
echo ""
echo -e "${YELLOW}🧪 Testing:${NC}"
echo -e "  - TypeScript: cd $OUTPUT_DIR/typescript-sdk && npm install && npm test"
echo -e "  - Python:     cd $OUTPUT_DIR/python-sdk && pip install -r requirements.txt"
echo -e "  - PHP:        cd $OUTPUT_DIR/php-sdk && composer install"
echo -e "  - Go:         cd $OUTPUT_DIR/go-sdk && go mod tidy"
echo ""

