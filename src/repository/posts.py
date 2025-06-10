from sqlalchemy import insert, select, delete, update

from database import async_session_maker
from src.models.models import Post
from src.schemas.posts import SPost


class PostRepository:
    model = Post

    async def add_one(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self, offset: int, limit: int, theme: str | None):
        async with async_session_maker() as session:
            stmt = select(self.model).offset(offset).limit(limit)
            if theme:
                stmt = stmt.where(Post.theme == theme)
            res = await session.execute(stmt)
            res = [SPost.model_validate(row[0]) for row in res.all()]
            return res

    async def get(self, id: int) -> SPost | None:
        async with async_session_maker() as session:
            stmt = select(self.model).where(PostRepository.model.id == id)
            result = await session.execute(stmt)
            post_model = result.scalar_one_or_none()
            if post_model is None:
                return None
            return SPost.model_validate(post_model)

    async def delete(self, id: int) -> bool:
        async with async_session_maker() as session:
            stmt = delete(self.model).where(PostRepository.model.id == id)
            result = await session.execute(stmt)
            await session.commit()
            return result.rowcount > 0

    async def update(self, id: int, data: dict) -> bool:
        async with async_session_maker() as session:
            stmt = (
                update(Post)
                .where(PostRepository.model.id == id)
                .values(**data)
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.rowcount > 0
