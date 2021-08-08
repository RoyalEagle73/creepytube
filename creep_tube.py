import os
from upload_video import YoutubeUpload
from faker import Faker

class CreepTube():
    def __init__(self):
        self.word = Faker().word()
        self.uploader = YoutubeUpload(self.word)

    def run(self):
        self.uploader.upload_on_youtube()
        print('Uploaded Video - ' + self.word + '.avi')
        self.delete_video()
    
    def delete_video(self):
        os.remove(self.word + '.avi')
        print('Video Removed')

def main():
    creep_tube = CreepTube()
    creep_tube.run()

if __name__ == "__main__":
    main()