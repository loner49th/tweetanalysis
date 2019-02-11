import tweepy
import datetime
import pandas as pd

def getTwitterData(keyword,outputFileName):

    #Twitter APIを使用するためのConsumerキー、アクセストークン設定
    Consumer_key = 'Consumer_key'
    Consumer_secret = 'Consumer_secret'
    Access_token = 'Access_token'
    Access_secret = 'Access_secret'

    #認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True)
    twitter_df = pd.DataFrame(columns=["time","id","screen_name","name","text","retweet_count","favorite_count"]) #dataframeの準備
    
    #カーソルを使用して10件のデータ取得
    for tweet in tweepy.Cursor(api.search, q=keyword,tweet_mode='extended').items(10):

         #使いそうな項目を取得
        time = tweet.created_at + datetime.timedelta(hours=9)
        user_id = tweet.id
        text = tweet.full_text
        screenname = tweet.user.screen_name
        name= tweet.user.name
        retweet_count=tweet.retweet_count
        favorite_count = tweet.favorite_count

        results_series = pd.Series([time,user_id,screenname,name,text,retweet_count,favorite_count],index = twitter_df.columns)
        twitter_df = twitter_df.append(results_series , ignore_index=True)


    twitter_df.to_csv(outputFileName, encoding='utf_8_sig')


if __name__ == '__main__':

    keyword = "テスト -RT"
    outputFileName="test.csv"

    getTwitterData(keyword,outputFileName)