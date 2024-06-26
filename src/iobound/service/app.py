from typing import Annotated


import typer
from fastapi import FastAPI, HTTPException
from pydantic_settings import BaseSettings

import pandas as pd 


class Settings(BaseSettings):
  data_path: str = 'data/kinopoisk_sample.csv'


settings = Settings()
df = pd.read_csv(settings.data_path)
app = FastAPI()


@app.get('/text/{text_id}')
async def text(text_id: int):
  if text_id >= 0 and text_id < df.shape[0]:
    return df.iloc[text_id]
  else:
    raise HTTPException(status_code=404)


@app.get('/total')
async def total():
  return {
    'total': df.shape[0],
  }

