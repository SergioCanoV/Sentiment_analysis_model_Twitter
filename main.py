from sentimentTwitter import *
def main():
    api = TwitterClient()

    tweets = api.get_tweets(query = 'world cup and usa team', count = 10000)

    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))

    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    print("Neutral tweets percentage: {} %".format(100*(len(tweets) - (len(ntweets) + len(ptweets)))/len(tweets)))

    print("\n\nPositive tweets:")
    n = 1
    m = 1
    for tweet in ptweets[:4]:
        print(f"Tweet #{n}: "+tweet['text'])
        n += 1

    print("\n\nNegative tweets:")
    for tweet in ntweets[:4]:
        print(f"Tweet #{m}: "+tweet['text'])
        m += 1

if __name__ == "__main__":
    main()
