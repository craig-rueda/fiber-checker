# ATT Fiber Availability Checker

Simple Python script that fetches the current fiber availability
 status for the configured address.

 ## Usage
 0. Optionally setup a virtual env
 ```Bash
 virtualenv venv
 source ./venv/bin/activate
 ```

 1. Install dependencies (slacker, argparse):
 ```Bash
 pip install argparse
 pip install slacker
 ```
 2. Create a Slack bot, and grab the API key supplied [here](https://api.slack.com/bot-users)
 3. Run scraper.py
 ```Bash
 python scraper.py -c <Your config file>
 ```
 Example: 
 ```Bash
 python scraper.py -c my_config.json
 ```
 
 ## Configuration
 Configuration is done through a JSON config file whose location is passed on the cmd line.
 Below is a description of its overall structure:
 ```json
 {
   "addr_line": "123 my st.",
   "addr_zip": "12345",
   "slack_key": "<Your bot's slack API key>",
   "channel": "<The slack channel to post messages to>"
 }
 ```