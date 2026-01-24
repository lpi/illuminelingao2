#!/bin/bash

# Deploy script for illuminelingao.com
# Uses Cloudflare Wrangler to deploy to Cloudflare Pages

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}🚀 Deploying illuminelingao.com to Cloudflare Pages${NC}"

# Check if wrangler is installed
if ! command -v wrangler &> /dev/null; then
    echo -e "${RED}Error: Wrangler CLI is not installed.${NC}"
    echo "Install it with: npm install -g wrangler"
    exit 1
fi

# Check if logged in to Cloudflare
if ! wrangler whoami &> /dev/null; then
    echo -e "${YELLOW}You need to login to Cloudflare first.${NC}"
    wrangler login
fi

# Build the site first
echo -e "${YELLOW}📦 Building static site...${NC}"
python3 build_site.py

# Deploy to Cloudflare Pages
echo -e "${YELLOW}☁️  Deploying to Cloudflare Pages...${NC}"
wrangler pages deploy public --project-name=illuminelingao

echo -e "${GREEN}✅ Deployment complete!${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. If this is your first deployment, go to Cloudflare Dashboard → Pages → illuminelingao"
echo "2. Click 'Custom domains' → 'Set up a custom domain'"  
echo "3. Add 'illuminelingao.com' and follow the DNS configuration instructions"
echo ""
echo "Or configure via CLI:"
echo "  wrangler pages project list"
echo "  # Custom domains must be configured in the Cloudflare Dashboard"
