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
from fastapi import FastAPI, Header
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from typing import Optional
#import yaml
import traceback
from middleware import ErrorHandlingMiddleware
from ToposoidCommon.model import TransversalState, StatusInfo, SingleImage, FeatureVector
from VitUtils import VitUtils
from MobileVitUtils import MobileVitUtils


import os
#from logging import config
#config.dictConfig(yaml.load(open("logging.yml", encoding="utf-8").read(), Loader=yaml.SafeLoader))
#import logging
#LOG = logging.getLogger(__name__)
import ToposoidCommon as tc
LOG = tc.LogUtils(__name__)

#vitUtils = VitUtils()
#mobileVitUtils = MobileVitUtils()

vitUtils = MobileVitUtils() if os.environ["TOPOSOID_IMAGE_RECOGNITION_MOBILE_VIT_USE"] == "1" else VitUtils()

app = FastAPI(
    title="toposoid-common-image-recognition-web",
    version="0.6-SNAPSHOT"
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
def getFeatureVector(input:SingleImage, X_TOPOSOID_TRANSVERSAL_STATE: Optional[str] = Header(None, convert_underscores=False)):
    transversalState = TransversalState.parse_raw(X_TOPOSOID_TRANSVERSAL_STATE.replace("'", "\""))
    try:           
        vector = vitUtils.getFeatureVector(input.url)
        response = JSONResponse(content=jsonable_encoder(FeatureVector(vector=vector.tolist())))
        LOG.info("Image vector encoding completed.", transversalState)
        return response
    except Exception as e:
        LOG.error(traceback.format_exc(), transversalState)
        return JSONResponse(content=jsonable_encoder(StatusInfo(status="ERROR", message=traceback.format_exc())))
