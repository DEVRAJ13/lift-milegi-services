from fastapi import FastAPI
from routers.users import router as user_router
from routers.auth import router as auth_router

app = FastAPI()
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(auth_router, prefix="/auth")

@app.get("/")
def root():
    return {"message": "Welcome to LiftMilegi API Services!"}