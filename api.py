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

from fastapi import FastAPI
from model import StatusInfo
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

import os
from logging import config
config.fileConfig('logging.conf')
import logging
LOG = logging.getLogger(__name__)
import traceback
from middleware import ErrorHandlingMiddleware
from model import SingleImage, FeatureVector
from VitUtils import VitUtils
from MobileVitUtils import MobileVitUtils

#vitUtils = VitUtils()
#mobileVitUtils = MobileVitUtils()

vitUtils = MobileVitUtils() if os.environ["TOPOSOID_IMAGE_RECOGNITION_MOBILE_VIT_USE"] == "1" else VitUtils()

app = FastAPI(
    title="toposoid-common-image-recognition-web",
    version="0.5-SNAPSHOT"
)
app.add_middleware(ErrorHandlingMiddleware)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/getFeatureVector")
def getFeatureVector(input:SingleImage):
    try:   
        vector = vitUtils.getFeatureVector(input.url)
        return JSONResponse(content=jsonable_encoder(FeatureVector(vector=vector.tolist())))
    except Exception as e:
        LOG.error(traceback.format_exc())
        return JSONResponse({"status": "ERROR", "message": traceback.format_exc()})
