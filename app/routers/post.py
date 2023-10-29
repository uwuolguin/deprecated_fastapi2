from fastapi import  Response, status, HTTPException, Depends, APIRouter
from .. import models,schemas,oath2
from ..database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func

router= APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("/")
#async def get_posts(db: Session = Depends(get_db),current_user =  Depends(oath2.get_current_user),Limit:int = 10):
async def get_posts(db: Session = Depends(get_db)):

    #posts= db.query(models.Post).limit(Limit).all()
    posts= db.query(models.Post.id,models.Post.title,func.count(models.Vote.post_id).label("votes")
                    ).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id
                                                                                                  ).all()

    lista=[]
    for i in posts:
        lista.append({"id": i.id,"title": i.title, "votes":i.votes})
    return lista

@router.get("/{id}")
async def get_post(id:int, db: Session = Depends(get_db) ):

    post= db.query(models.Post.id,models.Post.title,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return {"id": post.id,"title": post.title, "votes":post.votes}


@router.post("/",status_code=status.HTTP_201_CREATED)
async def get_posts(post:schemas.Post,db: Session = Depends(get_db),current_user =  Depends(oath2.get_current_user)):

    new_post=models.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"id": new_post.fullid,
            "title: ": new_post.fulltitle,
            "owner_id: ": new_post.fullownerid,
            "owner": new_post.fullowner.id}

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int,db: Session = Depends(get_db),
                      current_user =  Depends(oath2.get_current_user)):

    post=db.query(models.Post).filter(models.Post.id==id)

    if post.first() == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    
    if post.first().owner_id !=  current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN)
    
    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}")
async def update_post(id:int,updated_post:schemas.Post,db: Session = Depends(get_db),current_user =  Depends(oath2.get_current_user)):
    
    post_query=db.query(models.Post).filter(models.Post.id==id)

    post=post_query.first()

    if post == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    
    if post.owner_id !=  current_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN)
    
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)