import logging
import os

MONGO_ATLAS_PW = os.environ.get("MONGO_ATLAS_PW")
MONGO_ATLAS_USER = os.environ.get("MONGO_ATLAS_USER")
MONGO_ATLAS_URI = os.environ.get("MONGO_ATLAS_URI")
MONGO_ATLAS_HOST = os.environ.get("MONGO_ATLAS_HOST")
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")
NPS_SERVICE_API_KEY = os.environ.get("NPS_SERVICE_API_KEY")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
