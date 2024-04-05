import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7078356954:AAGKmIXox34cWrlDPNLoRDLA3jK82ufl60Y")

    APP_ID = int(os.environ.get("APP_ID", 23062240))

    API_HASH = os.environ.get("API_HASH", "582a897781f43febc47cde342cbe2792")
