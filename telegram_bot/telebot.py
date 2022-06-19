import os
from dotenv import load_dotenv
import httpx
from model.user_model import TeleUser
from cache.local_cache import user_cache

load_dotenv()

token = os.getenv('TELEBOT_TOKEN')
# chat_id = os.getenv('CHAT_ID')

class TeleBot():

    raw_url = 'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

    def sendMessageToAllUser(self):                 

        # print('list user size:', len(user_cache))
        for user_id in user_cache:

            user = user_cache[user_id]
            # print(user)
            url = self.raw_url.format(token=token, chat_id=user.chat_id, text="Hello from L20")

            httpx.get(url)
               

    def sendMessage(self, user: TeleUser, chat_id: str, text: str):
        
        if user is not None:
            chat_id = user.chat_id
        
        url = self.raw_url.format(token=token, chat_id=chat_id, text=text)

        httpx.get(url)
        
if __name__ == '__main__':

    pass
    # telebot = TeleBot()

    # telebot.sendMessage()

    
