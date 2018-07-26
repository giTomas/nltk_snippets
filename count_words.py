# https://www.digitalocean.com/community/tutorials/how-to-work-with-language-data-in-python-3-using-the-natural-language-toolkit-nltk

from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents

# get ids
ids = twitter_samples.fileids()

# Load tokenized tweets
tweets_tokens = twitter_samples.tokenized(ids[1])

# print(tweets_tokens)

# tag tagged tweets ('word', 'token')
tweets_tagged = pos_tag_sents(tweets_tokens)

# print(tweets_tagged)

# set accumulators
JJ_count = 0
NN_count = 0

# count
for tweet in tweets_tagged:
	for pair in tweet:
		tag = pair[1]
		if tag == 'JJ':
			JJ_count += 1
		elif tag == 'NN':
			NN_count += 1

print('Total number of adjectives: {:d}'.format(JJ_count))
print('Total number of nouns: {:d}'.format(NN_count))

