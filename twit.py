import requests
from requests_oauthlib import OAuth1
import json 

#source ./env/bin/activate 


consumer_key = 'v8e3Czb8vXK9Qb9fFuSKhn5GA'
consumer_secret = '3pPx3ltv48ZaLwsVEOPb6mNcKZAf4jhPYxGZ2PqR9Q8pJPJYRF'

token = '772960627186733056-57AbeGcGVz8AG2Iol6AjDE5JPNAPiA0'
token_secret = 'kQzPbzIBbfouFEI3BiR61RLNJR11CGzWh1T8q95WeRHeX'

def main():
	search_quary = input("Enter the word to be searched : ")
	result_tweet = search(search_quary)
	for tweet in result_tweet["statuses"]: 
		print("tweet_date : " + tweet["created_at"])
		print("tweet : " + tweet["text"])
		print("retweets : " + str(tweet["retweet_count"]))
		print("likes : " + str(tweet["favorite_count"]))
		print()

		




def search(search_quary, count = 10, src = "typd", result_type = "mixed"):
	search_url = 'https://api.twitter.com/1.1/search/tweets.json?'
	auth = OAuth1(consumer_key, consumer_secret, token, token_secret)

	parameters = {
		"q" : search_quary,
		"src": src,
		"count" : count,
		"result_type" : result_type,
	}
	responce = requests.get(search_url, auth=auth, params = parameters)
	return responce.json()



if __name__ == "__main__":
	main()