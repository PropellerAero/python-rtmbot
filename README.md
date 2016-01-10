whybot
======
A Slack bot based on Slack's basic RTM pythong app that asks you Why?. It does it up to five times within five minutes.

Propeller uses this in our internal #fuckups slack channel where we keep track of and analyse our mistakes.

Inspired by Sakichi Toyota's Five Whys and [Aaron Swartz's post on the value of documenting mistakes](http://www.aaronsw.com/weblog/geremiah).

python-rtmbot
=============
A Slack bot written in python that connects via the RTM API.

Python-rtmbot is a callback based bot engine. The plugins architecture should be familiar to anyone with knowledge to the [Slack API](https://api.slack.com) and Python. The configuration file format is YAML.

Some differences to webhooks:

1. Doesn't require a webserver to receive messages
2. Can respond to direct messages from users
3. Logs in as a slack user (or bot)
4. Bot users must be invited to a channel

Dependencies
----------
* websocket-client https://pypi.python.org/pypi/websocket-client/
* python-slackclient https://github.com/slackhq/python-slackclient

Installation
-----------

1. Download the slack-whybot code

        git clone https://github.com/PropellerAero/slack-whybot
        cd slack-whybot

2. Install dependencies ([virtualenv](http://virtualenv.readthedocs.org/en/latest/) is recommended.)

        pip install -r requirements.txt

3. Configure rtmbot (https://api.slack.com/bot-users)
        
        cp doc/example-config/rtmbot.conf .
        vi rtmbot.conf
          SLACK_TOKEN: "xoxb-11111111111-222222222222222"

