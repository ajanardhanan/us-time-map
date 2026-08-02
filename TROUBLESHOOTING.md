# Troubleshooting Guide

## Common Issues and Solutions

### Build and Deployment Issues

#### SAM Build Fails

**Problem**: `sam build` fails with dependency errors

**Solution**:
```bash
# Clean and rebuild
rm -rf .aws-sam
sam build --use-container
```

#### SAM Deploy Fails

**Problem**: `sam deploy` fails with permission errors

**Solution**:
```bash
# Verify AWS credentials
aws sts get-caller-identity

# Check IAM permissions
aws iam get-user

# Re-configure AWS CLI
aws configure
```

#### CloudFormation Stack Creation Fails

**Problem**: Stack creation fails

**Solutions**:
```bash
# Check stack events
aws cloudformation describe-stack-events --stack-name us-time-map

# View detailed error
sam logs -n TimeFunction --stack-name us-time-map

# Delete failed stack and retry
sam delete --stack-name us-time-map
sam deploy --guided
```

### Frontend Issues

#### React App Won't Start

**Problem**: `npm start` fails

**Solutions**:
```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Check Node version (should be 14+)
node --version

# Use legacy peer deps if needed
npm install --legacy-peer-deps
```

#### Map Doesn't Display

**Problem**: US map doesn't render

**Solutions**:
1. Check browser console for errors (F12)
2. Verify internet connection (map loads from CDN)
3. Check if `react-simple-maps` is installed:
   ```bash
   npm list react-simple-maps
   ```
4. Clear browser cache
5. Check for CORS errors

#### Times Don't Update

**Problem**: Clocks are frozen

**Solutions**:
1. Check browser console for errors
2. Verify moment-timezone is installed:
   ```bash
   npm list moment-timezone
   ```
3. Check if JavaScript is enabled
4. Hard refresh browser (Cmd+Shift+R or Ctrl+Shift+F5)

#### Build Fails

**Problem**: `npm run build` fails

**Solutions**:
```bash
# Check for syntax errors
npm run test

# Clear build cache
rm -rf build

# Rebuild
npm run build

# Check disk space
df -h
```

### AWS Deployment Issues

#### S3 Upload Fails

**Problem**: Cannot upload to S3

**Solutions**:
```bash
# Verify bucket exists
aws s3 ls | grep us-time-map

# Check bucket permissions
aws s3api get-bucket-policy --bucket YOUR-BUCKET

# Try with explicit credentials
aws s3 sync build/ s3://YOUR-BUCKET --delete --profile default

# Check bucket region
aws s3api get-bucket-location --bucket YOUR-BUCKET
```

#### CloudFront Not Updating

**Problem**: CloudFront shows old content

**Solutions**:
```bash
# Create invalidation
aws cloudfront create-invalidation \
  --distribution-id YOUR-ID \
  --paths "/*"

# Check invalidation status
aws cloudfront get-invalidation \
  --distribution-id YOUR-ID \
  --id INVALIDATION-ID

# Wait for completion (can take 10-15 minutes)
```

#### API Gateway 403 Errors

**Problem**: API returns 403 Forbidden

**Solutions**:
1. Check CORS configuration in template.yaml
2. Verify API Gateway deployment:
   ```bash
   aws apigateway get-rest-apis
   ```
3. Check Lambda permissions
4. Verify API endpoint URL

#### Lambda Function Errors

**Problem**: Lambda returns 500 errors

**Solutions**:
```bash
# Check Lambda logs
sam logs -n TimeFunction --stack-name us-time-map --tail

# Test locally
sam local invoke TimeFunction -e backend/test_event.json

# Check function configuration
aws lambda get-function --function-name YOUR-FUNCTION-NAME

# Update function code
sam build && sam deploy
```

### Runtime Issues

#### Slow Performance

**Problem**: Application loads slowly

**Solutions**:
1. Check CloudFront cache hit ratio
2. Enable compression in CloudFront
3. Optimize React bundle:
   ```bash
   npm run build -- --profile
   ```
4. Check CloudWatch metrics for bottlenecks

#### High AWS Costs

**Problem**: Unexpected AWS charges

**Solutions**:
```bash
# Check billing
aws ce get-cost-and-usage \
  --time-period Start=2026-07-01,End=2026-08-01 \
  --granularity MONTHLY \
  --metrics "BlendedCost"

# Review CloudWatch metrics
# Check for excessive Lambda invocations
# Review CloudFront bandwidth usage
# Consider reducing CloudFront price class
```

#### CORS Errors in Browser

**Problem**: CORS policy blocking requests

**Solutions**:
1. Verify CORS in template.yaml
2. Check API Gateway CORS settings
3. Add these headers to Lambda response:
   ```python
   'Access-Control-Allow-Origin': '*'
   'Access-Control-Allow-Headers': 'Content-Type'
   'Access-Control-Allow-Methods': 'GET, OPTIONS'
   ```
4. Redeploy after changes

### Development Issues

#### Git Repository Issues

**Problem**: Git conflicts or issues

**Solutions**:
```bash
# Initialize git if needed
git init
git add .
git commit -m "Initial commit"

# Create .gitignore
cat >> .gitignore << EOF
.aws-sam/
node_modules/
build/
.env
EOF
```

#### Environment Variables Not Working

**Problem**: .env variables not loaded

**Solutions**:
1. Create .env file from .env.example
2. Prefix with REACT_APP_
3. Restart development server
4. Check .env is in frontend/ directory
5. Don't commit .env to git

#### Package Installation Issues

**Problem**: npm install fails

**Solutions**:
```bash
# Use legacy peer deps
npm install --legacy-peer-deps

# Clear cache
npm cache clean --force
rm -rf node_modules package-lock.json
npm install

# Update npm
npm install -g npm@latest

# Check for conflicting global packages
npm list -g --depth=0
```

## Debugging Commands

### Check Application Status

```bash
# CloudFormation stack status
aws cloudformation describe-stacks --stack-name us-time-map

# Lambda function status
aws lambda get-function --function-name YOUR-FUNCTION

# CloudFront distribution status
aws cloudfront get-distribution --id YOUR-DIST-ID

# S3 bucket contents
aws s3 ls s3://YOUR-BUCKET --recursive
```

### View Logs

```bash
# Lambda logs
sam logs -n TimeFunction --stack-name us-time-map --tail

# CloudFormation events
aws cloudformation describe-stack-events --stack-name us-time-map

# API Gateway logs (if enabled)
aws logs tail /aws/apigateway/us-time-map --follow
```

### Test Components

```bash
# Test Lambda locally
sam local invoke TimeFunction -e backend/test_event.json

# Test API locally
sam local start-api
curl http://localhost:3000/times

# Test React locally
cd frontend && npm start

# Build and test production build
cd frontend && npm run build && npx serve -s build
```

## Getting Help

### Check Documentation
- README.md - Main documentation
- QUICKSTART.md - Quick start guide
- DEPLOYMENT_CHECKLIST.md - Deployment steps
- PROJECT_OVERVIEW.md - Architecture overview

### AWS Resources
- AWS SAM Documentation: https://docs.aws.amazon.com/serverless-application-model
- CloudFormation Docs: https://docs.aws.amazon.com/cloudformation
- Lambda Docs: https://docs.aws.amazon.com/lambda

### Community Support
- AWS Forums: https://forums.aws.amazon.com
- Stack Overflow: Tag with `aws-sam`, `aws-lambda`, `react`
- GitHub Issues: For specific library issues

### Direct Support
- Email: anilkjanardhan@gmail.com
- AWS Support: https://console.aws.amazon.com/support

## Preventive Measures

1. **Use version control**: Commit working versions
2. **Test locally first**: Use `sam local` before deploying
3. **Monitor costs**: Set up billing alerts
4. **Regular backups**: Export infrastructure as code
5. **Documentation**: Keep notes of customizations
6. **Security**: Regular security audits
7. **Updates**: Keep dependencies updated
8. **Monitoring**: Enable CloudWatch alarms

## Emergency Procedures

### Complete Rollback

```bash
# Delete CloudFront distribution (if needed)
# First disable, then delete after it's disabled
aws cloudfront update-distribution --id YOUR-ID --if-match ETAG \
  --distribution-config file://disabled-config.json

# Delete stack
sam delete --stack-name us-time-map

# Clean local build artifacts
rm -rf .aws-sam frontend/build node_modules
```

### Restore from Backup

```bash
# Restore S3 content (if versioning enabled)
aws s3api list-object-versions --bucket YOUR-BUCKET

# Restore specific version
aws s3api get-object --bucket YOUR-BUCKET \
  --key index.html --version-id VERSION-ID index.html
```

## Known Issues

1. **React 19 Compatibility**: react-simple-maps requires `--legacy-peer-deps`
2. **CloudFront Propagation**: Takes 15-20 minutes for global deployment
3. **Lambda Cold Starts**: First request may take 1-2 seconds
4. **Safari Timezone**: May need polyfill for older Safari versions

## Version Compatibility

- Node.js: >= 14.x
- npm: >= 6.x
- Python: 3.11
- AWS CLI: >= 2.x
- SAM CLI: >= 1.x
- React: 19.x (with legacy peer deps)
