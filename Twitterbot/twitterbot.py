import tweepy
import time

consumer_key = 'UhGZOyvUbcV2AdP6qKO0JVyO5'
consumer_secret = '4rBfUDC5GI5vfWZ7wrRGWC6z8L2IRnUHVRy552kuucr22ihucr'
access_token = '184273645-bdNU0KIie6lF5dt7befq1E0O22xCB8y2w4HfMn8Z'
access_token_secret = 'LKmvs4A7c2auo4RlVLP5ArNcij1wCIhgSQ6nOeguuWq0f'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
	try:
		while True:
			yield next()
	except tweepy.RateLimitError():
		time.sleep(300)

#generous bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	print(follower.name)
	if follower.name=='Taruna'or follower.followers_count > 1000:
		follower.follow()
		break
    
    
#narcissist bot
search_string = 'ZTM'
numberOfTweets = 5
    
for tweet in tweepy.Cursor(apisearch.search_string).items(numberOfTweets):
	try:
		tweet.favorite()
		tweet.retweet()
		print('I liked and retweeted that tweet')
	except tweepy.TweepError(e):
		print(e.reason)
	except StopIteration():
		break
