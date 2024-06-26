from typing import Annotated
import requests

import tqdm



def main(host: str = 'localhost', port: int = 8000) -> None: 
  
  url = f'http://{host}:{port}'
  results = []
  
  with requests.Session() as session:
    total = int(session.get(f'{url}/total').json()['total'])
    for index in tqdm.tqdm(range(total), total=total):
      results.append(
        session.get(f'{url}/text/{index}').json()
      )
  
  # print(results)


if __name__ == '__main__':
  main()