from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import create_user
from app.models.user import User
from app.core.security import get_current_user, hash_password

router = APIRouter(prefix="/users", tags=["Users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create(user: UserCreate, db: Session = Depends(get_db)):
    print("PASSWORD RECEIVED:", user.password)
    print("LENGTH:", len(user.password))
    return create_user(db, user.email, hash_password(user.password[:72]))

@router.get("/")
def get_all_users(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/me")
def read_users_me(current_user=Depends(get_current_user)):
    return current_user

#@router.get("/", response_model=list[UserOut])
#def get_users(db: Session = Depends(get_db),current_user: str = Depends(get_current_user)):
#    return db.query(User).all()

#@router.get("/")
#def get_users(db: Session = Depends(get_db)):
#    return db.query(User).all()

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()

@router.put("/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.email = user.email
        db_user.password = hash_password(user.password[:72])
        db.commit()
        return db_user
    return {"error": "User not found"}


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"message": "Deleted"}
    return {"error": "User not found"}
