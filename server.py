from flask import Flask, request
import traceback
# from dotenv import load_dotenv

from cache.local_cache import user_cache
from model.user_model import TeleUser
from telegram_bot.telebot import TeleBot
import my_scheduler
import atexit

# load_dotenv()

scheduler = my_scheduler.schedule()
atexit.register(lambda: scheduler.shutdown())

app = Flask(__name__)

telebot = TeleBot()


@app.route("/tele-webhook", methods=['POST'])
def tele_webhook():

    req = request.get_json()

    print(req)
    try:
        msg_key = None
        if 'message' in req:
            msg_key = 'message'
        elif 'edited_message' in req:
            msg_key = 'edited_message'

        if msg_key is not None:

            if 'entities' not in req[msg_key]:
                return ""

            entity = req[msg_key]['entities'][0]['type']
            user_id = req[msg_key]['from']['id']

            if entity == 'bot_command':
                text = str(req[msg_key]['text'])
                offset = int(req[msg_key]['entities'][0]['offset'])
                length = int(req[msg_key]['entities'][0]['length'])
                command = text[offset:offset+length]

                chat_id = req[msg_key]['chat']['id']

                if command == '/start':
                    print('start', user_id)
                    if user_id not in user_cache:
                        first_name = req[msg_key]['from']['first_name']
                        last_name = req[msg_key]['from']['last_name']
                        username = req[msg_key]['from']['username']

                        # add user to local cache
                        user = TeleUser(user_id, chat_id,
                                        first_name, last_name, username)
                        user_cache[user_id] = user
                        # send message subscribe successfully
                        telebot.sendMessage(user, None,
                                            "Xin cảm ơn bạn {} đã đăng ký nhận tin nhắn từ L20Bot !".format(first_name + ' ' + last_name))
                    # else:
                    #     telebot.sendMessage(None, chat_id, "Bạn đã đăng ký rồi mà ?")

                elif command == "/stop":
                    print('stop', user_id)                    
                    if user_id in user_cache:
                        telebot.sendMessage(
                            user=None, chat_id=chat_id, text="Đã hủy nhận tin nhắn !")
                        # remove from local cache
                        user_cache.pop(user_id)

    except:
        print("Unexpected error: ")
        traceback.print_exc()

    return "TELE Webhook"


if __name__ == "__main__":

    app.run()
