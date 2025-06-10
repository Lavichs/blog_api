from repository.posts import PostRepository
from services.posts import PostService

post_repo = PostRepository()
post_service = PostService(post_repo)

def get_post_service() -> PostService:
    return post_service