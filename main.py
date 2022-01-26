# Start to my IMDB Project
# Requests good for working with api
import requests
import json
import imdb
import psec

r = requests.get("https://imdb-api.com/", auth=('RVA113R', 'hwmq4lj0'))
print(r.status_code)


# Temp placeholder top pass Actions Test on GitHub
def test_placeholder():
    pass
