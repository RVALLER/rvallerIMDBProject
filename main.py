# Start to my IMDB Project
import requests
import json
import imdb
import psec

r = requests.get("https://imdb-api.com/", auth=('RVA113R', 'hwmq4lj0'))
r.status_code
print(r.status_code)


# Temp placeholder top pass Actions Test on Git
def test_placeholder():
    pass
