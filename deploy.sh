#!/bin/bash

set -e

echo "=========================================="
echo "US Time Map - Deployment Script"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
STACK_NAME="us-time-map"
REGION="us-east-1"

echo -e "${BLUE}Step 1: Building SAM application...${NC}"
sam build

echo ""
echo -e "${BLUE}Step 2: Deploying SAM stack...${NC}"
if [ ! -f samconfig.toml ]; then
    echo "First time deployment - running guided deployment..."
    sam deploy --guided
else
    echo "Using existing configuration..."
    sam deploy
fi

echo ""
echo -e "${BLUE}Step 3: Getting infrastructure outputs...${NC}"

# Get bucket name
BUCKET_NAME=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --region $REGION \
    --query 'Stacks[0].Outputs[?OutputKey==`WebsiteBucketName`].OutputValue' \
    --output text)

# Get CloudFront distribution ID
DISTRIBUTION_ID=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --region $REGION \
    --query 'Stacks[0].Outputs[?OutputKey==`CloudFrontDistributionId`].OutputValue' \
    --output text)

# Get API endpoint
API_ENDPOINT=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --region $REGION \
    --query 'Stacks[0].Outputs[?OutputKey==`ApiEndpoint`].OutputValue' \
    --output text)

# Get CloudFront URL
CLOUDFRONT_URL=$(aws cloudformation describe-stacks \
    --stack-name $STACK_NAME \
    --region $REGION \
    --query 'Stacks[0].Outputs[?OutputKey==`CloudFrontURL`].OutputValue' \
    --output text)

echo "S3 Bucket: $BUCKET_NAME"
echo "CloudFront Distribution ID: $DISTRIBUTION_ID"
echo "API Endpoint: $API_ENDPOINT"

echo ""
echo -e "${BLUE}Step 4: Building React frontend...${NC}"
cd frontend
npm run build
cd ..

echo ""
echo -e "${BLUE}Step 5: Uploading frontend to S3...${NC}"
aws s3 sync frontend/build/ s3://$BUCKET_NAME --delete

echo ""
echo -e "${BLUE}Step 6: Invalidating CloudFront cache...${NC}"
INVALIDATION_ID=$(aws cloudfront create-invalidation \
    --distribution-id $DISTRIBUTION_ID \
    --paths "/*" \
    --query 'Invalidation.Id' \
    --output text)

echo "CloudFront invalidation created: $INVALIDATION_ID"

echo ""
echo -e "${GREEN}=========================================="
echo "Deployment Complete!"
echo "==========================================${NC}"
echo ""
echo -e "${YELLOW}Access your application at:${NC}"
echo "  CloudFront URL: https://$CLOUDFRONT_URL"
echo ""
echo -e "${YELLOW}API Endpoint:${NC}"
echo "  $API_ENDPOINT"
echo ""
echo -e "${YELLOW}Note:${NC} CloudFront distribution may take 15-20 minutes to fully deploy."
echo "You can check status with: aws cloudfront get-distribution --id $DISTRIBUTION_ID"
echo ""
