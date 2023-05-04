from fastapi import APIRouter
from .. import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.show(id,db)


# from fastapi import APIRouter
# from blog import database, schemas, models
# from sqlalchemy.orm import Session
# from fastapi import APIRouter, Depends, status
# from blog.repository import user

# router = APIRouter(
#     prefix="/user",
#     tags=['Users']
# )

# get_db = database.get_db


# @router.post('/', response_model=schemas.ShowUser)
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     return user.create(request, db)


# @router.get('/{id}', response_model=schemas.ShowUser)
# def get_user(id: int, db: Session = Depends(get_db)):
#     return user.show(id, db)






















# from fastapi import APIRouter, Depends
# from .. import schemas, database
# from sqlalchemy.orm import Session
# get_db = database.get_db
# from ..repository import user


# router = APIRouter(
#     prefix="/user",
#     tags=['User']

# )


# @router.post("/",response_model=schemas.ShowUserDetails)
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     return user.create(request, db)


# @router.get("/{id}", response_model=schemas.ShowUser)
# def get_user(id: int, db: Session = Depends(get_db)):
#     return user.show(id,db)
