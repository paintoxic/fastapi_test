
from os import getenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run


def start_app():
    from packages.web.routes import routes

    tags_metadata = [
        {
            "name": "healthy",
            "description": "Routes to inform the healthy of service",
        },
    ]

    app = FastAPI(openapi_tags=tags_metadata)

    app.add_middleware(
        CORSMiddleware,
        allow_origins="*",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(routes)

    return app


if __name__ == '__main__':
    from connections import start_connections
    start_connections()
    app = start_app()

    _PORT = int(getenv("PORT", "3000"))
    _HOST = getenv("HOST", "0.0.0.0")

    run(app, host=_HOST, port=_PORT)
