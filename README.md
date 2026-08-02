# US Time Map

A serverless application that displays a US map with current time for each state's major city.

## Architecture

- **Frontend**: React.js application with interactive US map
- **Backend**: AWS Lambda function (Python) to provide time data
- **Infrastructure**: AWS SAM for deployment (API Gateway, Lambda, S3, CloudFront)

## Features

- Interactive US map visualization
- Real-time clock for all 50 states
- Responsive design
- Serverless architecture
- CloudFront CDN for global delivery

## Prerequisites

1. AWS Account (ajanardhanan / anilkjanardhan@gmail.com)
2. AWS CLI configured with credentials
3. AWS SAM CLI installed
4. Node.js and npm installed
5. Python 3.11 installed

## Installation

### Install AWS SAM CLI

```bash
# macOS
brew install aws-sam-cli

# Verify installation
sam --version
```

### Install Dependencies

```bash
# Frontend dependencies
cd frontend
npm install

# Backend dependencies (handled by SAM)
```

## Local Development

### Run Frontend Locally

```bash
cd frontend
npm start
```

The app will open at http://localhost:3000

### Test Lambda Function Locally

```bash
# From project root
sam local start-api
```

## Deployment

### Option 1: Automated Deployment Script

```bash
chmod +x deploy.sh
./deploy.sh
```

### Option 2: Manual Deployment

#### Step 1: Build the SAM Application

```bash
sam build
```

#### Step 2: Deploy Infrastructure

```bash
sam deploy --guided
```

Follow the prompts:
- Stack Name: us-time-map
- AWS Region: us-east-1 (or your preferred region)
- Confirm changes: Y
- Allow SAM CLI IAM role creation: Y
- Save arguments to configuration file: Y

#### Step 3: Build and Deploy Frontend

```bash
# Build React app
cd frontend
npm run build

# Get the S3 bucket name from SAM outputs
aws cloudformation describe-stacks \
  --stack-name us-time-map \
  --query 'Stacks[0].Outputs[?OutputKey==`WebsiteBucketName`].OutputValue' \
  --output text

# Upload to S3
aws s3 sync build/ s3://YOUR-BUCKET-NAME --delete

# Invalidate CloudFront cache (get distribution ID from outputs)
aws cloudfront create-invalidation \
  --distribution-id YOUR-DISTRIBUTION-ID \
  --paths "/*"
```

## Accessing the Application

After deployment, you'll get URLs in the SAM outputs:

1. **API Endpoint**: The Lambda function API endpoint
2. **S3 Website URL**: Direct S3 website URL
3. **CloudFront URL**: CDN URL (recommended for production)

Visit the CloudFront URL to access your application.

## Project Structure

```
us-time-map/
├── frontend/                # React application
│   ├── src/
│   │   ├── App.js          # Main app component
│   │   ├── USMap.js        # Map component
│   │   ├── stateData.js    # State timezone data
│   │   └── App.css         # Styles
│   └── package.json
├── backend/                 # Lambda function
│   ├── lambda_function.py  # Lambda handler
│   └── requirements.txt    # Python dependencies
├── template.yaml           # SAM template
├── deploy.sh              # Deployment script
└── README.md              # This file
```

## Configuration

### Update API Endpoint in Frontend (Optional)

If you want the frontend to call the Lambda API instead of calculating times client-side:

1. Get the API endpoint from SAM outputs
2. Update `frontend/src/USMap.js` to fetch from the API
3. Rebuild and redeploy frontend

## Cleanup

To remove all AWS resources:

```bash
# Delete CloudFront distribution first (manual via console or CLI)
# Then delete the stack
sam delete --stack-name us-time-map
```

## Technologies Used

- React.js
- react-simple-maps
- moment-timezone
- AWS Lambda (Python 3.11)
- AWS API Gateway
- AWS S3
- AWS CloudFront
- AWS SAM

## License

MIT

## Author

Anil Janardhanan (anilkjanardhan@gmail.com)
