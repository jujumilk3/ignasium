from typing import Union

from fastapi import FastAPI, status
from shared.constants.configs import configs
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.router import router as v1_router

# from shared.core.container import Container
from app.core.container import Container


def create_app():
    _app = FastAPI(
        title=configs.PROJECT_NAME,
        docs_url=f"/{configs.ROOT_API_PREFIX}/docs",
        redoc_url=f"/{configs.ROOT_API_PREFIX}/redoc",
        openapi_url=f"/{configs.ROOT_API_PREFIX}/openapi.json",
    )
    container = Container()
    _app.container = container
    _app.db = container.db()

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=configs.CORS_ALLOW_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # set routes
    @_app.get(f"/{configs.ROOT_API_PREFIX}/healthcheck", status_code=status.HTTP_200_OK)
    def root():
        return "OK"

    _app.include_router(v1_router, prefix=f"/{configs.ROOT_API_PREFIX}/v1")

    return _app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
