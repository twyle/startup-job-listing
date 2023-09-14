from pydantic import BaseModel, Field


class Quote(BaseModel):
    quote_content: str
    tags: list[str] = Field(default_factory=list)