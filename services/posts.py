from typing import List

from repository.posts import PostRepository
from schemas.posts import SPostAdd, SPost


class PostService:
    def __init__(self, repository: PostRepository) -> None:
        self.repository = repository

    async def add(self, post: SPostAdd) -> SPost:
        return await self.repository.add_one(post.model_dump())

    async def get_all(self, theme: str | None, offset: int = 0, limit: int = 100) -> List[SPost]:
        return await self.repository.find_all(offset=offset, limit=limit, theme=theme)

    async def get_one(self, id: int) -> SPost | None:
        return await self.repository.get(id)

    async def delete(self, id: int) -> bool:
        return await self.repository.delete(id)
