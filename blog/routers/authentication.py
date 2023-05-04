from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models, token
from ..hashing import Hash
from sqlalchemy.orm import Session
router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}



# from fastapi import APIRouter, Depends ,HTTPException, status
# from .. import schemas, database, models
# from sqlalchemy.orm import Session
# from ..hashing import Hash


# router = APIRouter()

# router = APIRouter(
#     # prefix="/blog",
#     tags=['Authentication']
# )


# @router.post("/login")
# def login(request :schemas.Login, db:Session = Depends(database.get_db)):
#     # user = models.User(name = request.username,  password = Hash.bcrypt(request.password))

#     user = db.query(models.User).filter(models.User.email == request.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
#     if not Hash.verify(user.password, request.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorect Pasword")
    
#     #generate jwt token and return token

#     return user

 
