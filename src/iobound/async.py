from typing import Annotated, Any

import aiohttp
import asyncio
import tqdm


async def fetch_data(session: aiohttp.ClientSession, url: str) -> Any:
  async with session.get(url) as response:
    return await response.json()
  

async def main(host = 'localhost', port = 8000) -> None:
  
  async with aiohttp.ClientSession() as session:
    url = f'http://{host}:{port}'
    async with session.get(f'{url}/total') as response:
      total = await response.json()
      
      tasks = []
      for index in range(int(total['total'])):
        tasks.append(
          asyncio.create_task(fetch_data(session, f'{url}/text/{index}'))
        )

      results = [
        await f for f in tqdm.tqdm(asyncio.as_completed(tasks), total=len(tasks)) 
      ]

      # print(results)


if __name__ == '__main__':
  asyncio.run(main())


