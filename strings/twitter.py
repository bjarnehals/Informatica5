tweet = input('geef een tweet: ')

index_hashtag = tweet.find('#')

while index_hashtag != -1:
    # tweet inkorten tot net voor gevonden hashtag
    tweet = tweet[index_hashtag:]
    # eerstvolgende spatie zoeken
    index_spatie = tweet.find(' ')
    print(tweet[:index_spatie])

    #zoek nieuwe hashtag
    index_hashtag = tweet.find('#')