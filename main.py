# Start to my IMDB Project
import json
import sys
import requests
import numpy as np
import pandas as pd
import secret


def main():
    #Save Reference
    original_stdout = sys.stdout
    url = f"https://imdb-api.com/en/API/Top250TVs/{secret.main()}"
    results = requests.get(url)
    if results.status_code != 200:
        print("Uh-Oh")
        return
    data_pull = results.json()
    print(data_pull)
    with open("optoptv.txt", 'w') as f:
        for key, value in data_pull.items():
            f.write('%s%s\n\n' % (key, value))
    f.close()



main()




