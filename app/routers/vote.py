from fastapi import  status, HTTPException, Depends, APIRouter
from .. import models,schemas,oath2
from ..database import get_db
from sqlalchemy.orm import Session

router= APIRouter(
    prefix="/votes",
    tags=["Votes"]
)


@router.post("/",status_code=status.HTTP_201_CREATED) 
async def get_posts(vote:schemas.Vote,db: Session = Depends(get_db),
                    current_user =  Depends(oath2.get_current_user)):

    post=db.query(models.Post).filter(models.Post.id==vote.post_id).first()

    if post : 
    
        vote_query=db.query(models.Vote).filter(
                models.Vote.post_id==vote.post_id,models.Vote.user_id==current_user.id)
        found_vote=vote_query.first()

        if (vote.dir == 1):
            print("1")
            if found_vote:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT)
            new_vote= models.Vote(post_id=vote.post_id,user_id=current_user.id)
            db.add(new_vote)
            db.commit()

            return {"messeage":"post correctly voted"}
        
        else:
            print("0")
            if not found_vote:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            vote_query.delete(synchronize_session=False)
            db.commit()
            return {"messeage":"vote on post correctly eliminated"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)