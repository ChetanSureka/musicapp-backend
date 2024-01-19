from innertube import InnerTube
from pprint import pprint
import json

def get_video(video_id, client="WEB"):
    video_id = "dQw4w9WgXcQ"
    # Client for YouTube on iOS
    client = InnerTube(client)

    # Fetch the player data for the video
    data = client.player(video_id)

    # List of streams of the video
    streams = data["streamingData"]["adaptiveFormats"]
    
    return streams

def Search(query, client="WEB"):
    client = InnerTube(client)

    data = client.search(query=query)
    data = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"]
    count = 1
    dict_count = 1
    filtered_data = {}
    for item in data:
        item.keys()
        if len(item.keys()) == 1:
            if list(item.keys())[0] == "videoRenderer":
                video_id = item["videoRenderer"]["videoId"]
                title = item["videoRenderer"]["title"]["runs"][0]["text"].strip()
                thumbnail = item["videoRenderer"]["thumbnail"]["thumbnails"][0]["url"]
                
                filtered_data[dict_count] = {
                    "title": title,
                    "thumbnail": thumbnail,
                    "videoId": video_id
                }
                dict_count += 1
            else:
                pass
        count += 1
        
    # data = json.dumps(filtered_data, indent=4)
    # with open('searchResults.json', "w") as file:
    #     file.write(data)
    # file.close()
    
    return filtered_data

# Example usage
# search_results = search("Aathma Raama")
# pprint(search_results)

# streams = get_video(search_results[1]["videoId"])