import yaml
import json
import logging
import os
from logging.handlers import RotatingFileHandler
import threading
import time

def load_configs():
    with open('./config.yaml') as f:
        return json.loads(json.dumps(yaml.safe_load(f)))
    
def create_logger():
    logger = logging

    if not os.path.exists('./logs'):
        os.mkdir('./logs')

    logger.basicConfig(
        handlers=[RotatingFileHandler('./logs/monitor.log', maxBytes=100000, backupCount=10)],
        level=logging.INFO,
        format="[%(asctime)s] %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')
    return logger

class RepeatEvery(threading.Thread):
    def __init__(self, interval, func, *args, **kwargs):
        threading.Thread.__init__(self)
        self.interval = interval 
        self.func = func         
        self.args = args         
        self.kwargs = kwargs     
        self.runable = True
    def run(self):
        while self.runable:
            self.func(*self.args, **self.kwargs)
            time.sleep(self.interval)
    def stop(self):
        self.runable = False