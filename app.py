from fastapi import FastAPI
from routes.user import user as userRouter
from docs import tags_metadata

app = FastAPI(
    title="REST API with FastAPI and Mongodb",
    description="a simple REST API using fastapi and mongodb",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(userRouter)
