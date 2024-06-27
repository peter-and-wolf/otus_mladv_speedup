
from functools import lru_cache
import os
import re
from functools import lru_cache

from typing import Any
from pymorphy3 import MorphAnalyzer #type: ignore


regexp = re.compile(r'\w+')
morph = MorphAnalyzer()


@lru_cache(maxsize=None)
def get_normal_form(word: str) -> str:
  return morph.parse(word)[0].normal_form


def process_text(text: str) -> str:
  return ' '.join(
    map(
      lambda x: get_normal_form(str(x)), \
      regexp.findall(text)
    )
  )
