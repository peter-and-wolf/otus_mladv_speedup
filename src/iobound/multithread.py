from typing import Any
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
import tqdm


def fetch_data(session: requests.Session, url: str) -> Any: 
  response = session.get(url)
  return response.json()


def main(host: str = 'localhost', port: int = 8000) -> None: 
  
  url = f'http://{host}:{port}'
  
  results = []
  with requests.Session() as session:
    total = int(session.get(f'{url}/total').json()['total'])

    with ThreadPoolExecutor(max_workers=8) as pool:
      
      futures = (pool.submit(fetch_data, session, f'{url}/text/{index}') for index in range(total))

      for future in tqdm.tqdm(as_completed(futures), total=total):
        results.append(future.result())

    # print(results)


if __name__ == '__main__':
  main()






