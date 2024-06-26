import pymemcache # type: ignore


class lru_cache:
  def __init__(self, func):
    self.func = func
    self.cache = pymemcache.Client(
      server='localhost', 
      allow_unicode_keys=True, 
      encoding='utf-8'
    )
        
  def __call__(self, x) -> str:
    result = self.cache.get(x)
    if result is None:
      result = self.func(x)
      self.cache.set(x, result)
    return str(result)   