from sqlalchemy import insert, select

from database import async_session_maker, Post
from schemas.posts import SPost


class PostRepository:
    model = Post

    async def add_one(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [SPost.model_validate(row[0]) for row in res.all()]
            return res
