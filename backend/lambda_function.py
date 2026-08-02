import json
from datetime import datetime
import pytz

# State timezone data
STATE_TIMEZONES = {
    'AL': {'city': 'Birmingham', 'timezone': 'America/Chicago'},
    'AK': {'city': 'Anchorage', 'timezone': 'America/Anchorage'},
    'AZ': {'city': 'Phoenix', 'timezone': 'America/Phoenix'},
    'AR': {'city': 'Little Rock', 'timezone': 'America/Chicago'},
    'CA': {'city': 'Los Angeles', 'timezone': 'America/Los_Angeles'},
    'CO': {'city': 'Denver', 'timezone': 'America/Denver'},
    'CT': {'city': 'Hartford', 'timezone': 'America/New_York'},
    'DE': {'city': 'Dover', 'timezone': 'America/New_York'},
    'FL': {'city': 'Miami', 'timezone': 'America/New_York'},
    'GA': {'city': 'Atlanta', 'timezone': 'America/New_York'},
    'HI': {'city': 'Honolulu', 'timezone': 'Pacific/Honolulu'},
    'ID': {'city': 'Boise', 'timezone': 'America/Boise'},
    'IL': {'city': 'Chicago', 'timezone': 'America/Chicago'},
    'IN': {'city': 'Indianapolis', 'timezone': 'America/Indiana/Indianapolis'},
    'IA': {'city': 'Des Moines', 'timezone': 'America/Chicago'},
    'KS': {'city': 'Wichita', 'timezone': 'America/Chicago'},
    'KY': {'city': 'Louisville', 'timezone': 'America/Kentucky/Louisville'},
    'LA': {'city': 'New Orleans', 'timezone': 'America/Chicago'},
    'ME': {'city': 'Portland', 'timezone': 'America/New_York'},
    'MD': {'city': 'Baltimore', 'timezone': 'America/New_York'},
    'MA': {'city': 'Boston', 'timezone': 'America/New_York'},
    'MI': {'city': 'Detroit', 'timezone': 'America/Detroit'},
    'MN': {'city': 'Minneapolis', 'timezone': 'America/Chicago'},
    'MS': {'city': 'Jackson', 'timezone': 'America/Chicago'},
    'MO': {'city': 'Kansas City', 'timezone': 'America/Chicago'},
    'MT': {'city': 'Billings', 'timezone': 'America/Denver'},
    'NE': {'city': 'Omaha', 'timezone': 'America/Chicago'},
    'NV': {'city': 'Las Vegas', 'timezone': 'America/Los_Angeles'},
    'NH': {'city': 'Manchester', 'timezone': 'America/New_York'},
    'NJ': {'city': 'Newark', 'timezone': 'America/New_York'},
    'NM': {'city': 'Albuquerque', 'timezone': 'America/Denver'},
    'NY': {'city': 'New York City', 'timezone': 'America/New_York'},
    'NC': {'city': 'Charlotte', 'timezone': 'America/New_York'},
    'ND': {'city': 'Fargo', 'timezone': 'America/Chicago'},
    'OH': {'city': 'Columbus', 'timezone': 'America/New_York'},
    'OK': {'city': 'Oklahoma City', 'timezone': 'America/Chicago'},
    'OR': {'city': 'Portland', 'timezone': 'America/Los_Angeles'},
    'PA': {'city': 'Philadelphia', 'timezone': 'America/New_York'},
    'RI': {'city': 'Providence', 'timezone': 'America/New_York'},
    'SC': {'city': 'Charleston', 'timezone': 'America/New_York'},
    'SD': {'city': 'Sioux Falls', 'timezone': 'America/Chicago'},
    'TN': {'city': 'Nashville', 'timezone': 'America/Chicago'},
    'TX': {'city': 'Houston', 'timezone': 'America/Chicago'},
    'UT': {'city': 'Salt Lake City', 'timezone': 'America/Denver'},
    'VT': {'city': 'Burlington', 'timezone': 'America/New_York'},
    'VA': {'city': 'Richmond', 'timezone': 'America/New_York'},
    'WA': {'city': 'Seattle', 'timezone': 'America/Los_Angeles'},
    'WV': {'city': 'Charleston', 'timezone': 'America/New_York'},
    'WI': {'city': 'Milwaukee', 'timezone': 'America/Chicago'},
    'WY': {'city': 'Cheyenne', 'timezone': 'America/Denver'}
}

def lambda_handler(event, context):
    """
    Lambda function to get current times for all US states
    """
    try:
        times = {}

        for state_abbr, state_info in STATE_TIMEZONES.items():
            tz = pytz.timezone(state_info['timezone'])
            current_time = datetime.now(tz)
            times[state_abbr] = {
                'city': state_info['city'],
                'time': current_time.strftime('%I:%M:%S %p'),
                'timezone': state_info['timezone']
            }

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET, OPTIONS'
            },
            'body': json.dumps({
                'times': times,
                'timestamp': datetime.utcnow().isoformat()
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e)
            })
        }
