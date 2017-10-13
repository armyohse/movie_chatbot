import os
from slackclient import SlackClient


BOT_NAME = 'seyoung_movie'

slack_client = SlackClient('xoxb-254241081123-wifZfQo7KDjzCOQ6kZIeMCcp')


if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
        print("could not find bot user with the name " + BOT_NAME)
