import json
import requests
import sys
from slacker import Slacker
import argparse

parser = argparse.ArgumentParser(description='Checks the configured address for availability of '
                                             'ATT Fiber and posts the result to slack')

parser.add_argument('-c', metavar='<config file path>', dest='config', help='The location of your config file',
                    required=True)

args = parser.parse_args()

# Load up the config from our JSON file...
config = {}
with open(args.config, 'r') as f:
    config = json.load(f)

slack = Slacker(config['slack_key'])

availability_url = 'https://www.att.com/services/shop/model/ecom/shop/view/unified/qualification/service' \
                   '/CheckAvailabilityRESTService/invokeCheckAvailability'
json_data = {
    'userInputZip': config['addr_zip'],
    'userInputAddressLine1': config['addr_line'],
    'mode': 'fullAddress',
    'customer_type': 'Consumer',
    'dtvMigrationFlag': False
}
headers = {'content-type': 'application/json'}
fiber_avail = False

try:
    resp = requests.post(availability_url, data = json.dumps(json_data), headers = headers)
    resp_json = json.loads(resp.text)
    fiber_avail = resp_json['profile']['isGIGAFiberAvailable']
except:
    print("Unexpected error:", sys.exc_info()[0])

msg = "Fiber isn't available yet :("
txt = ":cry: :cry: :cry: :cry: :cry:"
color = "#f44242"

if fiber_avail:
    msg = "Fiber is available!!"
    txt = ":tada:"
    color = "#33c653"

attachment = {
    "text": txt,
    "color": color
}

slack.chat.post_message(config['channel'], msg, as_user='AT&T Bot', username='attbot',
                        attachments=[attachment]
                        )