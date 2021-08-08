import builtins
import os

from google.oauth2 import credentials
import flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload
from create_video import VideoBuilder

class YoutubeUpload():
    def __init__(self, query):
        self.query = query
        self.video_builder = VideoBuilder(self.query)
        self.scopes = ["https://www.googleapis.com/auth/youtube.upload"]
        self.client_secrets_file = "auth.json"
        self.api_service_name = "youtube"
        self.api_version = "v3"
        
    def upload_on_youtube(self):
        self.video_builder.create_video()
        print('Video Created')
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        youtube_flow = flow.InstalledAppFlow.from_client_secrets_file(
            self.client_secrets_file, self.scopes)
        credentials = youtube_flow.run_console()
        youtube = googleapiclient.discovery.build(self.api_service_name, self.api_version, credentials=credentials)
        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "categoryId": "22",
                    "description": "Bots are here..",
                    "title": self.query
                },
                "status": {
                    "privacyStatus": "private"
                }
            }, media_body= MediaFileUpload(self.query+".avi"))
        response = request.execute()
        return response