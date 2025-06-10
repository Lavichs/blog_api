from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import delete_tables, create_tables
from src.routing.posts import router


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await delete_tables()
#     print("База очищена")
#     await create_tables()
#     print("База готова")
#     yield
#     print("Выключение")
# app = FastAPI(lifespan=lifespan, openapi_url="/core/openapi.json", docs_url="/core/docs")
app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

app.include_router(router)
