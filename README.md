Hi there and thnx for your time! 
This small example was made several years ago according to the course on the site stepik.org.  

#### Set environment
Get python 3.7+ (with 3.6+ you'll need to fix some imports manually): 
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
