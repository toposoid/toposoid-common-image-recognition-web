'''
  Copyright (C) 2025  Linked Ideal LLC.[https://linked-ideal.com/]
 
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as
  published by the Free Software Foundation, version 3.
 
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.
 
  You should have received a copy of the GNU Affero General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import os 
import numpy as np
from transformers import MobileViTFeatureExtractor, MobileViTForImageClassification
from PIL import Image
from PIL import ImageFile
import requests


class MobileVitUtils():
    model = None
    processor = None

    def __init__(self) :
        self.processor = MobileViTFeatureExtractor.from_pretrained(os.environ["TOPOSOID_IMAGE_RECOGNITION_MOBILE_VIT_MODEL"])
        self.model = MobileViTForImageClassification.from_pretrained(os.environ["TOPOSOID_IMAGE_RECOGNITION_MOBILE_VIT_MODEL"])
    
    def getFeatureVector(self, url):
        ImageFile.LOAD_TRUNCATED_IMAGES = True        
        image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

        inputs = self.processor(images=image, return_tensors="pt")
        outputs = self.model(**inputs)
        logits = outputs.logits

        vector = list(map(lambda x: x.to('cpu').detach().numpy().copy(), logits))
        return vector[0]