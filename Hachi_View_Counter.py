import locale
import os
from os import environ
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pprint
from time import sleep
import tweepy

auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth)

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

pp = pprint.PrettyPrinter(indent=4)

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_653398610134-31d7rrgmlf2v9ge8jme4k83b7smq1h05.apps.googleusercontent.com.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    while(True):
        Krequest = youtube.videos().list(
            part="snippet,statistics",
            id="UFQEttrn6CQ"
        )
        Kresponse = Krequest.execute()
        Kdata = Kresponse["items"][0]
        Kviews = int(Kdata["statistics"]["viewCount"])
        Div_Kviews = f'{Kviews:,}'
        
        
        Lrequest = youtube.videos().list(
            part="snippet,statistics",
            id="SX_ViT4Ra7k"
        )
        Lresponse = Lrequest.execute()
        Ldata = Lresponse["items"][0]
        Lviews = int(Ldata["statistics"]["viewCount"])
        Div_Lviews = f'{Lviews:,}'


        Urequest = youtube.videos().list(
            part="snippet, statistics",
            id="ptnYBctoexk"
        )
        Uresponse = Urequest.execute()
        Udata = Uresponse["items"][0]
        Uviews = int(Udata["statistics"]["viewCount"])
        Div_Uviews = f'{Uviews:,}'


        Prequest = youtube.videos().list(
            part="snippet,statistics",
            id="s582L3gujnw"
        )
        Presponse = Prequest.execute()
        Pdata = Presponse["items"][0]
        Pviews = int(Pdata["statistics"]["viewCount"])
        Div_Pviews = f'{Pviews:,}'
        

        Srequest = youtube.videos().list(
            part="snippet,statistics",
            id="1s84rIhPuhk"
        )
        Sresponse = Srequest.execute()
        Sdata = Sresponse["items"][0]
        Sviews = int(Sdata["statistics"]["viewCount"])
        Div_Sviews = f'{Sviews:,}'

        
        status = api.update_status("「感電」はYouTubeで再生回数" + Div_Kviews + "回突破！" + "\n\n" + "「Kanden」 MV has reached" + " " + Div_Kviews + " " + "views on YouTube!" + "\n\n" + "「감전」 뮤비 유튜브 조회수" + " " + Div_Kviews + "회 달성!")  
        status2 = api.update_status("「Lemon」はYouTubeで再生回数" + Div_Lviews + "回突破！" + "\n\n" + "「Lemon」 MV has reached" + " " + Div_Lviews + " " + "views on YouTube!" + "\n\n" + "「Lemon」 뮤비 유튜브 조회수" + " " + Div_Lviews + "회 달성!")
        status3 = api.update_status("「馬と鹿」はYouTubeで再生回数" + Div_Uviews + "回突破！" + "\n\n" + "「Uma to Shika」 MV has reached" + " " + Div_Uviews + " " + "views on YouTube!" + "\n\n" + "「말과 사슴」 뮤비 유튜브 조회수" + " " + Div_Uviews + "회 달성!")
        status4 = api.update_status("「パプリカ」はYouTubeで再生回数" + Div_Pviews + "回突破！" + "\n\n" + "「Paprika」 MV has reached" + " " + Div_Pviews + " " + "views on YouTube!" + "\n\n" + "「파프리카」 뮤비 유튜브 조회수" + " " + Div_Pviews + "회 달성!")
        status5 = api.update_status("「海の幽霊」はYouTubeで再生回数" + " " + Div_Sviews + "回突破！" + "\n\n" + "「Spirits of the Sea」 MV has reached" + " " + Div_Sviews + " " + "views on YouTube!" + "\n\n" + "「바다의 유령」 뮤비 유튜브 조회수" + " " + Div_Sviews + "회 달성!")
        sleep(15)
    

if __name__ == "__main__":
    main()
