import googleapiclient.discovery
import json


api_key = "AIzaSyAyoYkEw35e5oDJsii3_ALnrEecv3Ycksk"
playlist_id = "UUWwgaK7x0_FR1goeSRazfsQ"

youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

def get_video_ids(youtube, playlist_id):
    video_ids =[]
    request = youtube.playlistItems().list(
    part = "contentDetails",
    playlistId = playlist_id,
    maxResults = 50,
    )
    response = request.execute()

    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
        try:
            next_page_token = response["nextPageToken"]
        except:
            next_page_token = None
        more_pages = True
        while more_pages:
            if next_page_token is None:
                more_pages = False
            else:
                request = youtube.playlistitems().list(
                part = "contentDetails",
                playlistId = playlist_id,
                maxResults = 50,
                pageToken = next_page_token)
            response = request.execute()
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
                try:
                    next_page_token = response["nextPageToken"]
                except:
                    next_page_token = None

            




if __name__ == "__main__":
    res = get_video_ids(youtube, playlist_id)
    print(json.dumps(res, indent =4))