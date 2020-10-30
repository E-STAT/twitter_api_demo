import tweepy


CUSTOMER_KEY = "Z8PNT6UQfnqtOdveHbX1g1Jjp"
CUSTOMER_SECRET = "PrcNsI9oqw3m5B4AZmpMruBcAm24CzPceXZ77OZfaqVkWWhOPG"
ACCESS_TOKEN = "1261442300-jSfjhkB5XKDgTUGTJXiSa9xdAyAQiALRURpFtSb"
ACCESS_TOKEN_SECRET = "pWfrcELmbykb0U2VQZ4ldPTHoz3CLqNufZ0nkZZxPkXwx"


# Authenticate to Twitter
auth = tweepy.OAuthHandler(CUSTOMER_KEY, CUSTOMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Create a tweet
# api.update_status("A deep dive after several hide and seek")

# filename = "demo_nlp.png"
# api.media_upload(filename, status = "We go again!, Testing")

#friends
# my_friends_100 = api.followers()

# for fre in my_friends_100:
#     print("Last Twitter follower is {}".format(fre.name))

# for block in api.blocks():
#     print(block.name)

#search for tweet
output = []
for tweet in api.search(q="EndSARS", lang="en", rpp=10):
    #print(f"{tweet.user.name}:{tweet.text}")
    output.append({tweet.user.name: tweet.text})

print(output)
