from pydantic import BaseModel



class Settings(BaseModel):
  DEF_CONF = False
  BOT_TOKEN: str = 'YOUR BOT TOKEN HERE' #input your bot token
  APP_ID: int = 1 #input app id form my.telegram.org
  APP_HASH: str = '1'#input app hash form my.telegram.orgs
  CHECK_SUBSCRIBE = True
  AUTO_DELETE = True