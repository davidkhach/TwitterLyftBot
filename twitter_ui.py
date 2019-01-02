import tweepy
import lyft_app

consumer_key = 'EYvMrt2AMMuHfrImgYkX1yUxD'
consumer_secret = 'HODh2fCnVqbjdQSdo0qESQDTneA65qnPp8ibxQ0yyqI4hi4uxa'
access_token = '1076023219696496640-2lCEeBPNnR7M28bhklnkH7hh0xmKgD'
access_token_secret = '4dEWidsi3TMYEMiyGPtuJB3g6YjRQvOaNF6DDkD98jxkp'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)





class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id
        while True:
            try:
                user_id = status._json['id']
                formatted_text = status._json['text'][15:]
                start_location = lyft_app.parse_response_start_location(formatted_text)
                end_location = lyft_app.parse_response_end_location(formatted_text)
                if type(start_location) != None and type(end_location) != None:
                    result = lyft_app.run_app(start_location, end_location)
                    api.update_status('@' + username + ' ' + result, in_reply_to_status_id = status_id)
            except:
                api.update_status('@' + username + ' something went wrong, please dm owner', in_reply_to_status_id = status_id)



stream = tweepy.Stream(auth = api.auth, listener = MyStreamListener())
stream.filter(track=['@Should_I_Lyft'])

