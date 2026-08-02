# Quick Start Guide

## Setup AWS Credentials

1. **Configure AWS CLI** with your credentials:

```bash
aws configure
```

Enter:
- AWS Access Key ID
- AWS Secret Access Key
- Default region: `us-east-1`
- Default output format: `json`

## Deploy the Application

### Option 1: One-Command Deployment

```bash
./deploy.sh
```

### Option 2: Step-by-Step

```bash
# 1. Build SAM application
sam build

# 2. Deploy (first time - guided)
sam deploy --guided

# 3. Build React app
cd frontend && npm run build && cd ..

# 4. Upload to S3 (replace with your bucket name from outputs)
aws s3 sync frontend/build/ s3://us-time-map-ACCOUNT_ID --delete

# 5. Invalidate CloudFront (replace with your distribution ID)
aws cloudfront create-invalidation --distribution-id YOUR_DIST_ID --paths "/*"
```

## Development

### Run Frontend Locally

```bash
cd frontend
npm start
```

Open http://localhost:3000

### Test Lambda Locally

```bash
sam local start-api
```

Test endpoint: http://localhost:3000/times

## Update Frontend After Changes

```bash
cd frontend
npm run build
cd ..

# Upload to S3
aws s3 sync frontend/build/ s3://YOUR-BUCKET-NAME --delete

# Invalidate CloudFront cache
aws cloudfront create-invalidation --distribution-id YOUR-DIST-ID --paths "/*"
```

## Get Application URLs

```bash
aws cloudformation describe-stacks \
  --stack-name us-time-map \
  --query 'Stacks[0].Outputs'
```

## Troubleshooting

### Check CloudFront Deployment Status

```bash
aws cloudfront get-distribution --id YOUR-DIST-ID
```

### View Lambda Logs

```bash
sam logs -n TimeFunction --stack-name us-time-map --tail
```

### Test API Endpoint

```bash
curl YOUR-API-ENDPOINT
```

## Cost Estimate

- API Gateway: ~$3.50 per million requests
- Lambda: Free tier includes 1M requests/month
- S3: ~$0.023 per GB
- CloudFront: ~$0.085 per GB transferred

Estimated monthly cost for low traffic: **< $5/month**

## Security Notes

- The S3 bucket is publicly accessible (required for static website hosting)
- API endpoints have CORS enabled for public access
- No sensitive data is stored or transmitted
- Consider adding AWS WAF for additional protection in production

## Next Steps

1. Custom domain with Route53
2. HTTPS certificate with ACM
3. Authentication with Cognito
4. Monitoring with CloudWatch
5. Add more features (weather, population data, etc.)
