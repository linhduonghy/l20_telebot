from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from telegram_bot.telebot import TeleBot

my_timezone = "Asia/Ho_Chi_Minh"

def my_job(telebot: TeleBot):
    
    telebot.sendMessageToAllUser()

def schedule():
    
    scheduler = BackgroundScheduler()

    cron_trigger_1 = CronTrigger.from_crontab(expr="51 * * * *", timezone='UTC')
    cron_trigger_2 = CronTrigger.from_crontab(expr="52 * * * *", timezone='UTC')
    
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

    
    
        
if __name__ == '__main__':
        
    pass
    # schedule()