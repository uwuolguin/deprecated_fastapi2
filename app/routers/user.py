from fastapi import  status, HTTPException, Depends, APIRouter
from .. import models,schemas,utils
from ..database import get_db
from sqlalchemy.orm import Session
router= APIRouter(
    
    prefix="/users",
    tags=["Users"]
)




@router.post("/",status_code=status.HTTP_201_CREATED)
async def get_posts(user:schemas.userCreate,db: Session = Depends(get_db)):

    hashed_password= utils.hash(user.password)
    user.password=hashed_password

    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"email" : new_user.fullemail}

@router.get("/{id}")
async def get_user(id:int, db: Session = Depends(get_db) ):

    user= db.query(models.User).filter(models.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return {"data": user.fullemail}
