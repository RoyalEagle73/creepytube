
from gather_images import ImageCollector
import cv2
import urllib.request
import numpy as np


class VideoBuilder():
    def __init__(self, query):
        self.image_collector = ImageCollector(query)
        self.query = query
        self.video_title = query + '.avi'
    
    def __collect_images(self):
        image_urls = self.image_collector.find_images()
        images = []
        for image_url in image_urls:
            try:
                req = urllib.request.urlopen(image_url)
                arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
                image = cv2.imdecode(arr, -1)
                if image is not None:
                    images.append(image)
            except:
                pass
        return images

    def create_video(self):
        images = self.__collect_images()
        largest_height = max([image.shape[0] for image in images])
        largest_width = max([image.shape[0] for image in images])
        size = (largest_width,largest_height)
        out = cv2.VideoWriter(self.video_title,cv2.VideoWriter_fourcc(*'DIVX'), 1, size)
        for image in images:
            out.write(cv2.resize(image,size))
        out.release()