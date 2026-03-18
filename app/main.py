from fastapi import FastAPI
from app.routes import user, auth
from app.db.base import Base
from app.db.session import engine
from fastapi import Depends
from app.core.security import get_current_user

app = FastAPI(title="Production API")

app.include_router(auth.router)
app.include_router(user.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/users/me")
def read_users_me(current_user = Depends(get_current_user)):
    return current_user
