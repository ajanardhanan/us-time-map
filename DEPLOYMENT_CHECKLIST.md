# Deployment Checklist

## Pre-Deployment

- [ ] AWS CLI installed and configured
  ```bash
  aws --version
  aws configure list
  ```

- [ ] AWS SAM CLI installed
  ```bash
  sam --version
  ```

- [ ] Node.js and npm installed
  ```bash
  node --version
  npm --version
  ```

- [ ] Python 3.11 installed
  ```bash
  python3 --version
  ```

- [ ] AWS credentials configured for account: ajanardhanan
  - Email: anilkjanardhan@gmail.com
  - Run: `aws sts get-caller-identity` to verify

## Initial Setup

- [ ] Clone or navigate to project directory
  ```bash
  cd /Users/ajanardhanan/Documents/GitHub/us-time-map
  ```

- [ ] Install frontend dependencies
  ```bash
  cd frontend && npm install && cd ..
  ```

- [ ] Test frontend locally
  ```bash
  cd frontend && npm start
  ```
  - Should open at http://localhost:3000
  - Verify map loads and times update

## Deployment Steps

### Option A: Automated Deployment (Recommended)

- [ ] Run deployment script
  ```bash
  ./deploy.sh
  ```

- [ ] Note down the outputs:
  - CloudFront URL: _________________
  - API Endpoint: _________________
  - S3 Bucket Name: _________________
  - Distribution ID: _________________

### Option B: Manual Deployment

- [ ] Build SAM application
  ```bash
  sam build
  ```

- [ ] Deploy SAM stack
  ```bash
  sam deploy --guided
  ```
  - Stack Name: `us-time-map`
  - Region: `us-east-1`
  - Confirm changes: Y
  - Allow IAM role creation: Y
  - Save to config: Y

- [ ] Build React frontend
  ```bash
  cd frontend && npm run build && cd ..
  ```

- [ ] Get S3 bucket name
  ```bash
  aws cloudformation describe-stacks \
    --stack-name us-time-map \
    --query 'Stacks[0].Outputs[?OutputKey==`WebsiteBucketName`].OutputValue' \
    --output text
  ```
  Bucket Name: _________________

- [ ] Upload frontend to S3
  ```bash
  aws s3 sync frontend/build/ s3://YOUR-BUCKET-NAME --delete
  ```

- [ ] Get CloudFront Distribution ID
  ```bash
  aws cloudformation describe-stacks \
    --stack-name us-time-map \
    --query 'Stacks[0].Outputs[?OutputKey==`CloudFrontDistributionId`].OutputValue' \
    --output text
  ```
  Distribution ID: _________________

- [ ] Invalidate CloudFront cache
  ```bash
  aws cloudfront create-invalidation \
    --distribution-id YOUR-DIST-ID \
    --paths "/*"
  ```

## Post-Deployment Verification

- [ ] Wait for CloudFront distribution to deploy (15-20 minutes)
  ```bash
  aws cloudfront get-distribution --id YOUR-DIST-ID
  ```
  - Status should be "Deployed"

- [ ] Test CloudFront URL
  - Open: https://YOUR-CLOUDFRONT-URL
  - Verify:
    - [ ] Page loads without errors
    - [ ] US map displays correctly
    - [ ] All 50 states are visible
    - [ ] Times update every second
    - [ ] State cards show correct cities
    - [ ] Hover effects work
    - [ ] Responsive design works on mobile

- [ ] Test API Endpoint (optional)
  ```bash
  curl YOUR-API-ENDPOINT
  ```
  - Should return JSON with times for all states

- [ ] Check browser console for errors
  - Open DevTools (F12)
  - Check Console tab
  - Check Network tab

## Monitoring

- [ ] Check CloudWatch Logs
  ```bash
  sam logs -n TimeFunction --stack-name us-time-map --tail
  ```

- [ ] Monitor CloudWatch metrics
  - Lambda invocations
  - API Gateway requests
  - S3 bucket access
  - CloudFront cache hit ratio

## Cost Optimization

- [ ] Review CloudWatch costs
- [ ] Consider enabling S3 lifecycle policies
- [ ] Review CloudFront price class
- [ ] Set up billing alerts

## Security

- [ ] Review S3 bucket policy
- [ ] Check CORS configuration
- [ ] Review IAM roles and permissions
- [ ] Consider adding WAF rules
- [ ] Set up CloudTrail logging

## Documentation

- [ ] Update README with actual URLs
- [ ] Document any custom configurations
- [ ] Save deployment outputs
- [ ] Create runbook for updates

## Future Enhancements

- [ ] Add custom domain with Route53
- [ ] Add SSL certificate with ACM
- [ ] Implement caching strategy
- [ ] Add monitoring and alerting
- [ ] Add CI/CD pipeline
- [ ] Implement feature flags

## Rollback Plan

If deployment fails:

```bash
# Delete CloudFront distribution (if needed)
aws cloudfront delete-distribution --id YOUR-DIST-ID --if-match ETAG

# Delete stack
sam delete --stack-name us-time-map

# Or via CloudFormation
aws cloudformation delete-stack --stack-name us-time-map
```

## Support

- GitHub Issues: https://github.com/aws/serverless-application-model
- AWS Support: https://aws.amazon.com/support
- Documentation: https://docs.aws.amazon.com/serverless-application-model

## Notes

Date: _______________
Deployed by: _______________
Stack ARN: _______________
CloudFront URL: _______________
Issues encountered: _______________
_______________________________________________
_______________________________________________
