import os
import random
import requests
import tweepy


# Pick a random line from the 'lines.txt' file
def get_random_line():
    file_path = 'lines.txt'  # Path to your text file

    with open(file_path, 'r') as file:
        lines = file.readlines()

    random_line = random.choice(lines).strip()
    return random_line


# Authorize Twitter with v1.1 API
def auth_v1(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


# Authorize Twitter with v2 API
def auth_v2(consumer_key, consumer_secret, access_token, access_token_secret):
    return tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret,
        return_type=requests.Response,
    )


# Tweet picked line
def tweet(line) -> requests.Response:
    # In the next 4 lines, we are getting the keys from environment variables
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

    client_v2 = auth_v2(consumer_key, consumer_secret,
                        access_token, access_token_secret)

    return client_v2.create_tweet(text=line)


def main():
    line = get_random_line()
    tweet(line)


if __name__ == '__main__':
    main()