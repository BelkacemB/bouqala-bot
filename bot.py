import tweepy

def get_random_line(afile):
    lines = open(afile).read().splitlines()
    return random.choice(lines)

def tweet_random_line(afile):
    status = get_random_line(afile)
    api.update_status(status)

    # Search for user mentions
    for mention in api.mentions_timeline():
        print(mention.text)
        tweet_random_line("bouqala.csv")