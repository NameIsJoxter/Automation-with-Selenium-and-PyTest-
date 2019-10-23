Hi there and thnx for your time! 

#### Set environment
Get python: 
```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get install python3.7
```

Get all requirenment stuff:
```bash
$ pip install -r requirements.txt
```

#### Launch: 
```.env
$ pytest -v --tb=line -m need_review
```