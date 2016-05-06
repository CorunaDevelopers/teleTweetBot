#from tweepy import StreamListener

class TwitterMentionsListener(StreamListener):
    def on_data(self, data):
        print data
        