import pandas as pd
from pandarallel import pandarallel #type: ignore

from workload import process_text

pandarallel.initialize(progress_bar=True)


def main(data_path: str = 'data/kinopoisk_sample.csv'): 
  
  df = pd.read_csv(data_path)

  results = df['review'].parallel_apply(process_text)

  print(results.head())


if __name__ == '__main__':
  main()

