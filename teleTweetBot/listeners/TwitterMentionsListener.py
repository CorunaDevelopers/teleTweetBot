from tweepy import StreamListener


class TwitterMentionsListener(StreamListener):
    def on_status(self, status):
        print status.text
