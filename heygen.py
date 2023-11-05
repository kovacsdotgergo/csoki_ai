import requests
import time

url = 'https://api.heygen.com/v1/video.generate'
api_key = 'API and the pea'

headers = {
    'X-Api-Key': api_key,
    'Content-Type': 'application/json'
}

data = {
    "background": "#ffffff",
    "clips": [
        {
            "avatar_id": "Daisy-inskirt-20220818",
            "avatar_style": "normal",
            "input_text": "Welcome to HeyGen API",
            "offset": {
                "x": 0,
                "y": 0
            },
            "scale": 1,
            "voice_id": "1bd001e7e50f421d891986aad5158bc8"
        }
    ],
    "ratio": "16:9",
    "test": True,
    "version": "v1alpha"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    # Request was successful, and you can process the response.
    video_data = response.json()
    print(video_data)
    video_id = video_data["data"]["video_id"]
    # Handle the video data as needed.
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)  # Print the response content for debugging purposes.

while True:
    response = requests.get(f'https://api.heygen.com/v1/video_status.get?video_id={video_id}', headers={'X-Api-Key': api_key})
    data = response.json()

    if data["code"] == 100 and data["data"]["status"] == "completed":
        # The response is the third option, so break out of the loop
        break

    # Sleep for a few seconds before making the next request (e.g., 5 seconds)
    time.sleep(5)

# Once you reach this point, the response is the third option
print("Video processing completed, URL:", data["data"]["video_url"])
