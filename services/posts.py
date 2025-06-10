from repository.posts import PostRepository
from schemas.posts import SPostAdd, SPost


class PostService:
    def __init__(self, repository: PostRepository) -> None:
        self.repository = repository

    async def add(self, post: SPostAdd):
        return await self.repository.add_one(post.model_dump())

    async def get_all(self):
        return await self.repository.find_all()
