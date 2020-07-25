import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pprint
from time import sleep

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

pp = pprint.PrettyPrinter(indent=4)

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_653398610134-31d7rrgmlf2v9ge8jme4k83b7smq1h05.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    while(True):
        request = youtube.videos().list(
            part="snippet,statistics",
            id="SX_ViT4Ra7k"
        )
        response = request.execute()

        data = response["items"][0]
        vid_snippet = data["snippet"]
        title = vid_snippet["title"]
        views = str(data["statistics"]["viewCount"])
        print(title)
        print(views)
        sleep(30)
    

if __name__ == "__main__":
    main()
