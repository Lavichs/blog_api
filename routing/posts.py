from typing import List, Annotated

from fastapi import APIRouter, Depends

from depends import get_post_service
from schemas.posts import SPost, SPostAdd
from services.posts import PostService

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("")
async def get_all(
        post_service: PostService = Depends(get_post_service),
) -> List[SPost]:
    posts = await post_service.get_all()
    return posts

@router.post("")
async def create(
        post: Annotated[SPostAdd, Depends()],
        post_service: PostService = Depends(get_post_service),
) -> SPost:
    post = await post_service.add(post)
    return post
