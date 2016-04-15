
#!/usr/bin/env/python
#_*_ coding:utf-8_*_

import tweepy

class TweetCommand(object):
    """docstring for TweetCommand"""
    def __init__(self, consummer_key, consummer_secret, access_key, access_secret):
        super(TweetCommand, self).__init__()
        self.consummer_key = consummer_key
        self.consummer_secret = consummer_secret
        self.access_key = access_key
        self.access_secret = access_secret


    def proccessMessage(self, message):
        text = message['text'].encode('utf-8')
        print text

        if text.startsWith('/tweet '):
            print 'tweet'
            self.tweet_message(text.replate('/tweet ', ''))

    def tweet_message(self, message):    
        auth = tweepy.OAuthHandler(self.consummer_key, self.consummer_secret)
        auth.set_access_token(self.access_key, self.access_secret)

        api = tweepy.API(auth)

        api.update_status(message)
        