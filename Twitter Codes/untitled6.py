import tweepy

# Keys, tokens and secrets
consumer_key = '12UCbopLPIyQ3S32G0bf6kNYX'
consumer_secret = '54KRYBa0gOUNxA0Ex1YWQqdTkyEL067MY7ed8ZC3j7kCELBLbt'
access_token = '4901534286-V4aGGswcis4xgK4VGZ5ns5lyjTJZtdDmmWRJ540'
access_token_secret = 'qR1QroqxEQW5kQTUaYNcZtPKDgkL3iYJdwudBgEsZishR'

# Tweepy OAuthHandler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

targets = ['realdonaldtrump'] # All your targets here

for target in targets:
    user = api.get_user(target)
    print(user.name, user.followers_count,user.friends_count,user.statuses_count,user.favourites_count)