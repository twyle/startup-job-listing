from pydantic import BaseModel


class PopularQuotesTag(BaseModel):
    name: str
    count: float