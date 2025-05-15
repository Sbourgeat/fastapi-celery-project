# project/__init__.py

from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    from project.users import users_router
    app.include_router(users_router)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    
    return app
