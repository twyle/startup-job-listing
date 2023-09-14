from pydantic import BaseModel


class PopularQuotesAuthor(BaseModel):
    name: str
    count: float