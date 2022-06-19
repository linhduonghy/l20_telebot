from server import app

import my_scheduler
import atexit

if __name__ == "__main__":
    
    scheduler = my_scheduler.schedule()
    atexit.register(lambda: scheduler.shutdown())

    app.run()

    