import pandas as pd
import requests
from requests import Response
from typing import Optional

def get_most_popular_tags(page: int = None) -> pd.DataFrame:
    url: str = f'http://localhost:8000/quotes/popular_quotes'
    resp: Response = requests.get(url=url, params={'page': page})
    # else:
    #     url: str = f'http://localhost:8000/quotes/popular_quotes'
    #     resp: Response = requests.get(url=url)
    if resp.ok:
        most_popular_quotes: list[dict[str, float]] = resp.json()['tags']
        df = pd.DataFrame(most_popular_quotes)
        return df
    
def get_most_popular_authors() -> pd.DataFrame:
    url: str = f'http://localhost:8000/quotes/popular_authors'
    resp: Response = requests.get(url=url)
    if resp.ok:
        most_popular_authors: list[dict[str, float]] = resp.json()['authors']
        df = pd.DataFrame(most_popular_authors)
        return df
    
def get_pages() -> int:
    return 6