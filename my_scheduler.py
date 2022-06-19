from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from telegram_bot.telebot import TeleBot

from datetime import datetime

my_timezone = "Asia/Ho_Chi_Minh"

def my_job(telebot: TeleBot):
    telebot.sendMessageToAllUser()

def schedule():
    
    scheduler = BackgroundScheduler()

    cron_trigger_test = CronTrigger.from_crontab(expr="50 23 * * *", timezone=my_timezone)
    cron_trigger_1 = CronTrigger.from_crontab(expr="0 8 * * *", timezone=my_timezone)
    cron_trigger_2 = CronTrigger.from_crontab(expr="20 17 * * *", timezone=my_timezone)
    
    job_test = scheduler.add_job(func=my_job, trigger=cron_trigger_test, args=[TeleBot()], name="job_test")
    job1 = scheduler.add_job(func=my_job, trigger=cron_trigger_1, args=[TeleBot()], name="job_1")
    job2 = scheduler.add_job(func=my_job, trigger=cron_trigger_2, args=[TeleBot()], name="job_2")

    scheduler.start()
    
    print("******** Scheduler started !")
    # try:
    #     # This is here to simulate application activity (which keeps the main thread alive).
    #     while True:
    #         time.sleep(5)
    # except (KeyboardInterrupt, SystemExit):
    #     # Not strictly necessary if daemonic mode is enabled but should be done if possible
    #     scheduler.shutdown()

    return scheduler
