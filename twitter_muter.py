import twitter


# Enter your Twitter API credentials here
api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='',
                  sleep_on_rate_limit=False)

# declaring empty list
followingList = []

# initializing cursor
cursor = -1


while cursor != 0:
    # calling API with cursor value
    friends = api.GetFriendsPaged(cursor=cursor)

    # printing the friends list from that call
    print(friends[2])

    # adding all those friends to the list
    for friend in friends[2]:
        followingList.append(friend.AsDict()["id"])

    # updating the cursor
    cursor = friends[0]

mutedList = []
cursor = -1

while cursor != 0:
    muteCall = api.GetMutesIDsPaged(cursor=cursor)
    print(muteCall)

    for mute in muteCall[2]:
        mutedList.append(mute)

    cursor = muteCall[0]

for mute in mutedList:
    print(mute)

muteCalls = 0

alreadyMuted = 0
muted = 0

# printing all the people you follow
print("Processing mutes:")
for follow in followingList:

    if follow in mutedList:
        # do nothing
        print("already muted: " + str(follow))
        alreadyMuted += 1
    else:
        try:
            api.CreateMute(user_id=follow)
            muteCalls += 1
            print("Mute calls is now " + str(muteCalls))

        except twitter.error.TwitterError:
            print("Ran out of API calls")
            print("Muted " + str(muted) + " and " + str(alreadyMuted) + " were already muted")
            print("Users left to process: " + str(len(followingList) - (alreadyMuted + muted)))
            break

        print("muting: " + str(follow))
        muted += 1

print("followingList length: " + str(len(followingList)))
print("already muted count: " + str(alreadyMuted))
print("muted count: " + str(muted))
print("total processed is: " + str(alreadyMuted + muted))
