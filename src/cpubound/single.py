import pandas as pd
import tqdm

from workload import process_text

tqdm.tqdm.pandas()


def main(data_path: str = 'data/kinopoisk_sample.csv'): 
  
  df = pd.read_csv(data_path)

  results = df['review'].progress_apply(process_text)

  print(results.head())


if __name__ == '__main__':
  main()

