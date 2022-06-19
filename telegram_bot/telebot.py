import os
import httpx
from model.user_model import TeleUser
from cache.local_cache import user_cache


token = os.getenv('TELEBOT_TOKEN')

class TeleBot():

    raw_url = 'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

    def sendMessageToAllUser(self):                 

        print('user cache:', user_cache.keys())
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
        

    
