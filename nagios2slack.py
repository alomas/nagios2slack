#!/usr/bin/env python3
import configparser
import sys
import requests

def main():
    config = configparser.ConfigParser()
    config.read('nagios2slack.cfg')
    for theline in sys.stdin:
        try:
            slack_webhook_url = config['nagios']['slack_url']
        except KeyError as e:
            slack_webhook_url = config['default']['slack_url']
        result = requests.post(slack_webhook_url, data='{"text": "' + theline.replace('\n','') + '"}')
        print('Sent to slack -> ' + theline)
main()