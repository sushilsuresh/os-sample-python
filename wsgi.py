from flask import Flask
import os
from datetime import datetime

application = Flask(__name__)

@application.route("/")
def hello():
    node = os.uname().nodename
    dateTimeObj = datetime.now()
    tstamp = dateTimeObj.strftime("%Y-%m-%d %H:%M:%S")
    return "Hello World! - from - " + tstamp + ' - ' + node + '\n'

if __name__ == "__main__":
    application.run()
