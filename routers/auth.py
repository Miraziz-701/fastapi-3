from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from config import SECRET_KEY, ALGORITHM
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.db import DepSession
from models.user import UserValidation, User
from sqlalchemy import select
from jose import jwt, JWTError

router = APIRouter(prefix="/auth", tags=["Auth"])

bycrpt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login")


async def authenticate_user(username: str, password: str, session: DepSession):
    query = select(User).filter(User.username == username)
    result = await session.execute(query)
    user = result.scalar_one_or_none()

    if not user:
        return False
    if not bycrpt_context.verify(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    result = {"sub": username, "id": user_id}
    expires = datetime.utcnow() + expires_delta
    result.update({"exp": expires})
    return jwt.encode(result, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate user",
            )
        return {"username": username, "id": user_id}
    except JWTError:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate user",
)
        

CurrentUser = Annotated[dict, Depends(get_current_user)]


@router.post("/login")
async def login(
    form: Annotated[OAuth2PasswordRequestForm, Depends()], session: DepSession
):
    user = await authenticate_user(form.username, form.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Couldn't validate user"
        )
    token = create_access_token(user.username, user.id, timedelta(minutes=30))
    return {"access_token": token, "token_type": "bearer"}


@router.post("/create/user")
async def create_user(user: UserValidation, session: DepSession):
    new_user = User(
        username=user.username, hashed_password=bycrpt_context.hash(user.password)
    )
    session.add(new_user)
    await session.commit()

@router.get('/')
async def user(user: CurrentUser):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')
    return {"User": user}