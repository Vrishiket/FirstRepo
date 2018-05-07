CONSUMER_KEY = '12UCbopLPIyQ3S32G0bf6kNYX'
CONSUMER_SECRET = '54KRYBa0gOUNxA0Ex1YWQqdTkyEL067MY7ed8ZC3j7kCELBLbt'
OAUTH_TOKEN = '4901534286-V4aGGswcis4xgK4VGZ5ns5lyjTJZtdDmmWRJ540'
OAUTH_SECRET = 'qR1QroqxEQW5kQTUaYNcZtPKDgkL3iYJdwudBgEsZishR'
def friends():

  TRACK_TERM = 'hello'

  api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_SECRET)

  f = api.request('statuses/filter', {'track': TRACK_TERM})

  for user in f:
    print(user['friends_count'])


def favorite():

  TRACK_TERM = 'kanye'

  api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_SECRET)

  h = api.request('statuses/filter', {'track': TRACK_TERM})

  for retweeted_item in h:
    print(retweeted_item['favorite_count'])

if __name__ == '__main__':

    try:

        friends()

        favorite()

    except KeyboardInterrupt:

        print ('\nGoodbye!')