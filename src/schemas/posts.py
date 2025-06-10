from pydantic import BaseModel


class SPostAdd(BaseModel):
    title: str
    content: str
    theme: str

    class Config:
        from_attributes = True

class SPost(SPostAdd):
    id: int

    class Config:
        from_attributes = True

