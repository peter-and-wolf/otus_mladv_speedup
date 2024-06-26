from concurrent.futures import ProcessPoolExecutor, as_completed
import pandas as pd
import tqdm

from workload import process_text


def main(data_path: str = 'data/kinopoisk_sample.csv') -> None: 
  
  df = pd.read_csv(data_path)

  results = []
  with ProcessPoolExecutor() as pool:
    futures = (pool.submit(process_text, text) for text in df['review'])
    
    for future in tqdm.tqdm(as_completed(futures), total=df.shape[0]):
      results.append(future.result())

  print(pd.Series(results).head())


if __name__ == '__main__':
  main()



    
