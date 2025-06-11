import uvicorn
from fastapi import FastAPI

from config import settings
from src.routing.posts import router


app = FastAPI(
    openapi_url="/core/openapi.json",
    docs_url="/core/docs",
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.APP_PORT)
