'''
  Copyright 2021 Linked Ideal LLC.[https://linked-ideal.com/]
 
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
 
      http://www.apache.org/licenses/LICENSE-2.0
 
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 '''

import os 
import numpy as np
from transformers import MobileViTFeatureExtractor, MobileViTForImageClassification
from PIL import Image
import requests


class MobileVitUtils():
    model = None
    processor = None

    def __init__(self) :
        self.processor = MobileViTFeatureExtractor.from_pretrained(os.environ["TOPOSOID_IMAGE_RECOGNITION_MOBILE_VIT_MODEL"])
        self.model = MobileViTForImageClassification.from_pretrained(os.environ["TOPOSOID_IMAGE_RECOGNITION_MOBILE_VIT_MODEL"])
    
    def getFeatureVector(self, url):
        image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

        inputs = self.processor(images=image, return_tensors="pt")
        outputs = self.model(**inputs)
        logits = outputs.logits

        vector = list(map(lambda x: x.to('cpu').detach().numpy().copy(), logits))
        return vector[0]