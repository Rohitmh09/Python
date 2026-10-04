import os
import sys

from dotenv import load_dotenv

load_dotenv() #if not load add path in load_dotenv(floder_name/.env)

api_key = os.environ.get('api_key')
print(api_key)

openAIKey = os.environ.get('openAI')
print(openAIKey)
if not openAIKey or openAIKey == None:
    print('Open AI API key not available please check')
    sys.exit(1)
    
db_key = os.environ.get('database')
print(db_key)

