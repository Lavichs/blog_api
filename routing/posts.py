from typing import List, Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import Boolean

from depends import get_post_service
from schemas.posts import SPost, SPostAdd
from services.posts import PostService

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("")
async def get_all(
        offset: int = 0,
        limit: int = 10,
        theme: str = None,
        post_service: PostService = Depends(get_post_service),
) -> List[SPost]:
    posts = await post_service.get_all(theme, offset, limit)
    return posts


@router.get("/{id}")
async def get_post(
        id: int,
        post_service: PostService = Depends(get_post_service),
) -> SPost | None:
    post = await post_service.get_one(id)
    return post


@router.post("")
async def create(
        post: Annotated[SPostAdd, Depends()],
        post_service: PostService = Depends(get_post_service),
) -> SPost:
    post = await post_service.add(post)
    return post

@router.delete("/{id}")
async def delete(
        id: int,
        post_service: PostService = Depends(get_post_service),
) -> bool:
    res = await post_service.delete(id)
    return res
