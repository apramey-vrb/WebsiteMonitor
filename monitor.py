from exceptions import ContentMismatchException
from concurrent.futures import ThreadPoolExecutor
import requests
import helpers
import models
import time
import eel
import os
import json

def get_status(url):
    try:
        urlObject = models.urlResponse(url['link'], url['content'])
        response = requests.get(urlObject.link)            
        urlObject.response = f'{response.status_code} {response.reason}'
        if response.status_code == 200:
            pageContent = response.text
            urlObject.responseTime = response.elapsed.total_seconds()
            if not pageContent.find(urlObject.content) > 0:
                raise ContentMismatchException
            urlObject.isValidContent = pageContent.find(urlObject.content) > 0
    except ContentMismatchException:
        urlObject.response = "Content Mismatch"
    except Exception as e:
        urlObject.response = str(e)
    finally:
        return urlObject
 
def run_monitor(urls):
    with ThreadPoolExecutor(len(urls)) as executor:
        results = executor.map(get_status, urls)
        log.info('-----------------Start of the batch-----------------')
        for i, result in enumerate(results):
            url = result.link
            log.info(f'URL: {url}\t|Response: {result.response}\t|Content Match: {result.isValidContent}\t|Response Time: {result.responseTime}s |{result.toJSON()}')
        log.info('------------------End of the batch------------------')

def start_monitor():
    starttime = time.time()
    threshold = configs['threshold']
    index = 0

    if 'urls' not in configs or ('urls' in configs and len(configs['urls']) == 0) :
        print('\nPlease configure config.yaml file with URLs to proceed\n')
        exit()

    print('\n\nMonitor running,\nPress CTRL+C to interrupt the process\n')
    while True:
        run_monitor(configs['urls'])       
        print(f"Batches Processed: {index} | Time elapsed: {index * threshold} seconds", end="", flush=True)
        print("\r", end="", flush=True)
        time.sleep(threshold - ((time.time() - starttime) % threshold))
        index+=1

def load_ui():
    eel.start('index.html')

@eel.expose
def get_recent_status():
    if not os.path.isfile('.\logs\monitor.log'):
        return None

    payloads = []
    startIndex = 0
    content = list(reversed(open('.\logs\monitor.log').readlines()))
    for i, line in enumerate(content):
        if 'End of the batch' in line:
            startIndex = i+1
        elif startIndex > 0 and 'Start of the batch' in line:            
            break
        elif startIndex > 0:
            payloads.append(json.loads(line.split('|')[-1]))
        else:
            continue
        
    return payloads

if __name__ == "__main__":
    log = helpers.create_logger()
    configs = helpers.load_configs()
    eel.init('web')
    
    print("\nChoose an option : ")
    print("[1] Start Website Monitoring")
    print("[2] Load Monitoring Report")
    print("[q] Quit")

    choice = input("\nWhat would you like to do? ")

    if choice == '1':
        start_monitor()
    elif choice == '2':
        load_ui()
    elif choice.lower() == 'q' :
        print("\nThank you!")
    
   