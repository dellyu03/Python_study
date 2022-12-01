import googleapiclient.discovery
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

api_key = "AIzaSyAyoYkEw35e5oDJsii3_ALnrEecv3Ycksk"
channel_ids = ['UCgwXqwhj43nmgAhgBoo-sdQ', 
'UCWwgaK7x0_FR1goeSRazfsQ',
 'UCCspJ6mFfCwOV4qFjZWi2wg', 
 'UCVjS9AuBloqJJjhsy3vIfug',
 'UCE_M8A5yxnLfW0KghEeajjw']

youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey = api_key)
def get_channel_stats (youtube, channel_ids):
    all_data = []
    request = youtube.channels().list(
        part = "snippet, contentDetails, statistics",
        id = ','.join(channel_ids)
        )
    response = request.execute()
    for i in range(len(response['items'])):
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
        Subscribers = response['items'][i]['statistics']['subscriberCount'],
        Views =  response['items'][i]['statistics']['viewCount'],
        Total_videos = response['items'][i]['statistics']['videoCount'],
        playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'],
        )

        all_data.append(data)
    return all_data

def draw_channel_stats(channel_statistics):
    channel_dataFrame = pd.DataFrame(channel_statistics)
    channel_dataFrame['Subscribers'] = pd.to_numeric(channel_dataFrame['Subscribers'])
    channel_dataFrame['Views'] = pd.to_numeric(channel_dataFrame['Views'])
    channel_dataFrame['Total_videos'] = pd.to_numeric(channel_dataFrame['Total_videos'])
    print(channel_dataFrame)
    graph = sns.barplot(x = "Channel_name", y = "Subscribers", data = channel_dataFrame)
    plt.show()
    graph1 = sns.barplot(x="Channel_name", y="Views", data = channel_dataFrame)
    plt.show()
    graph2 = sns.barplot(x = "Channel_name", y = "Total_videos", data = channel_dataFrame)
    plt.show()


if __name__ == "__main__":
    res = get_channel_stats(youtube, channel_ids)
    print(json.dumps(res, indent =4))
    draw_channel_stats(res)