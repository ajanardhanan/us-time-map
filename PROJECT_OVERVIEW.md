# US Time Map - Project Overview

## Project Description

A serverless web application that displays an interactive map of the United States with real-time clocks showing the current time in major cities across all 50 states.

## Architecture

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   Browser   │─────▶│  CloudFront  │─────▶│     S3      │
│             │      │     (CDN)    │      │  (Website)  │
└─────────────┘      └──────────────┘      └─────────────┘
                             │
                             │ (Optional)
                             ▼
                     ┌──────────────┐      ┌─────────────┐
                     │ API Gateway  │─────▶│   Lambda    │
                     │              │      │  (Python)   │
                     └──────────────┘      └─────────────┘
```

### Components

1. **Frontend (React.js)**
   - Interactive US map using react-simple-maps
   - Real-time clock display using moment-timezone
   - Responsive grid layout for state information
   - Client-side time calculation (no backend required)

2. **Backend (AWS Lambda - Optional)**
   - Python 3.11 function
   - Provides time data via REST API
   - Uses pytz for timezone calculations
   - CORS enabled for browser access

3. **Infrastructure (AWS)**
   - **S3**: Static website hosting
   - **CloudFront**: CDN for global delivery
   - **API Gateway**: REST API endpoint
   - **Lambda**: Serverless compute
   - **IAM**: Security and permissions

## Technology Stack

### Frontend
- React 19.2.8
- react-simple-maps (US map visualization)
- d3-geo (geographic projections)
- moment-timezone (timezone handling)

### Backend
- Python 3.11
- pytz (timezone library)

### Infrastructure
- AWS SAM (Infrastructure as Code)
- AWS CloudFormation
- AWS CLI

### Development Tools
- Node.js & npm
- AWS SAM CLI
- Git

## Project Structure

```
us-time-map/
├── frontend/                    # React application
│   ├── public/                  # Static assets
│   ├── src/
│   │   ├── App.js              # Main app component
│   │   ├── USMap.js            # Map component with time display
│   │   ├── stateData.js        # State data with timezones
│   │   ├── App.css             # Styling
│   │   └── index.js            # Entry point
│   ├── package.json            # Frontend dependencies
│   └── .env.example           # Environment variables template
│
├── backend/                     # Lambda function
│   ├── lambda_function.py      # Lambda handler
│   ├── requirements.txt        # Python dependencies
│   └── test_event.json        # Test event for local testing
│
├── template.yaml               # AWS SAM template
├── deploy.sh                   # Automated deployment script
├── package.json                # Root package.json with scripts
├── .gitignore                  # Git ignore rules
│
├── README.md                   # Main documentation
├── QUICKSTART.md              # Quick start guide
├── DEPLOYMENT_CHECKLIST.md    # Deployment checklist
└── PROJECT_OVERVIEW.md        # This file
```

## Features

### Current Features
- ✅ Interactive US map with all 50 states
- ✅ Real-time clocks for each state (updates every second)
- ✅ Major city display for each state
- ✅ Hover effects to highlight states
- ✅ Responsive grid layout
- ✅ Beautiful gradient UI design
- ✅ Serverless architecture
- ✅ Global CDN delivery
- ✅ Automated deployment

### Potential Enhancements
- 🔄 Custom domain with Route53
- 🔄 HTTPS with AWS Certificate Manager
- 🔄 User authentication with Cognito
- 🔄 Save favorite states
- 🔄 Add weather information
- 🔄 Add population data
- 🔄 Time zone converter
- 🔄 Dark mode toggle
- 🔄 Mobile app version
- 🔄 Analytics dashboard

## Data

### State Information
- All 50 US states
- Major city for each state
- Accurate timezone mapping
- State abbreviations
- Geographic coordinates

### Time Zones Covered
- Eastern Time (ET)
- Central Time (CT)
- Mountain Time (MT)
- Pacific Time (PT)
- Alaska Time (AKT)
- Hawaii-Aleutian Time (HST)

## Deployment

### Prerequisites
- AWS Account
- AWS CLI configured
- SAM CLI installed
- Node.js and npm
- Python 3.11

### Quick Deploy
```bash
./deploy.sh
```

### Manual Deploy
```bash
sam build
sam deploy --guided
cd frontend && npm run build && cd ..
aws s3 sync frontend/build/ s3://YOUR-BUCKET --delete
aws cloudfront create-invalidation --distribution-id YOUR-ID --paths "/*"
```

## Cost Estimate

For low to medium traffic (< 10,000 requests/month):

| Service      | Cost          | Notes                          |
|-------------|---------------|--------------------------------|
| Lambda      | Free          | 1M requests/month free tier   |
| API Gateway | < $1/month    | $3.50 per million requests    |
| S3          | < $1/month    | $0.023 per GB storage         |
| CloudFront  | < $3/month    | $0.085 per GB transfer        |
| **Total**   | **< $5/month**| Assuming low traffic          |

## Performance

- **Initial Load**: < 2 seconds
- **Map Render**: < 500ms
- **Time Update**: Every 1 second
- **Global CDN**: Low latency worldwide
- **Lambda Cold Start**: 1-2 seconds (first request)
- **Lambda Warm**: < 100ms

## Security

- S3 bucket publicly readable (required for website)
- API has CORS enabled for browser access
- IAM roles follow least privilege
- No sensitive data stored or transmitted
- CloudFront provides DDoS protection

## Monitoring

- CloudWatch Logs for Lambda
- CloudWatch Metrics for all services
- X-Ray for distributed tracing (optional)
- CloudFront access logs
- S3 access logs

## Testing

### Frontend
```bash
cd frontend
npm test
npm start  # Local development
```

### Backend
```bash
sam local start-api
sam local invoke TimeFunction -e backend/test_event.json
```

## Support

- **Email**: anilkjanardhan@gmail.com
- **Account**: ajanardhanan
- **Documentation**: See README.md and QUICKSTART.md

## License

MIT

## Version History

- **v1.0.0** (2026-08-02)
  - Initial release
  - React frontend with US map
  - AWS Lambda backend
  - CloudFront distribution
  - Automated deployment

## Contributors

- Anil Janardhanan (anilkjanardhan@gmail.com)

## Acknowledgments

- react-simple-maps for the map component
- moment-timezone for timezone handling
- AWS SAM for serverless deployment
- create-react-app for project bootstrapping
