from time import time
from pyrsistent import T
import requests
import fire
import time

URL_LOCAL = "http://0.0.0.0:9696/predict"

def main(n=1,
         url = URL_LOCAL):
  candidate = [{"gender": "M",
                "ssc_p": 71.0,
                "ssc_b": "Central",
                "hsc_p": 58.66,
                "hsc_b": "Central",
                "hsc_s": "Science",
                "degree_p": 58.0,
                "degree_t": "Sci&Tech",
                "etest_p": 56.0,
                "mba_p": 61.3,
                "specialisation": "Mkt&Fin",
                "workex": "Yes"
                }]

  t = time.time()
  for _ in range(n):
    result = requests.post(url=url,json=candidate).json()
    print('The Model Prediction for placement :',result)
  duration = time.time() - t
  avg = duration / n
  print("Number of calls {n}. Average latency {avg}")

if __name__ == '__main__':
    fire.Fire(main)


