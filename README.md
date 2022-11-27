# Website Monitor 

## Steps to run the source code 

1. Install the dependencies using ```requirements.txt```
 ```
 pip install -r requirements.txt
 ```
2. Run the application file and get a simple console menu for starting the monitor and visualising the report
```
python monitor.py
```
3. To run the unit tests 
```
python test_monitor.py
```

## Source code comprises of below mentioned files and folders 
1. ```monitor.py``` : Main application file 
2. ```helpers.py``` : Helper methods
3. ```exceptions.py``` : Custom exceptions
4. ```models.py``` : defines ```url``` and ```urlResponse```
5. ```test_monitort.py``` : unit tests fot ```monitor.get_status()```
6. ```config.yaml``` : config file to define URLs with content and Threshold in seconds for continued execution
7. ```web``` folder : includes files responsible for latest status visualization
8. ```logs``` folder : includes ```monitor.log``` which logs all the execution data
9. ```requirements.txt``` : defines all the dependencies

## Note:
1. ```config.yaml``` file comes with default threshold of 5 seconds and a set of 3 URL links with some content. Please feel free to tweak them
```
threshold: 5
urls:
- "link": https://apra.me
  "content": "Apramey Bhat"
- "link": https://amazon.com
  "content": "I'm Feeling Lucky"
- "link": https://google.com
  "content": "I'm Feeling Lucky"
```

2. Application makes use of ```eel``` library to visualise the report in a HTML view.