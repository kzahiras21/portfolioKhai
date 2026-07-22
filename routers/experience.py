from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database
import uuid

router = APIRouter(prefix="/experiences", tags=["Experience"])

@router.get("/", response_model=List[schemas.ExperienceResponse])
def get_experiences(db: Session = Depends(database.get_db)):
    return db.query(models.Experience).order_by(models.Experience.order.asc()).all()

@router.post("/", response_model=schemas.ExperienceResponse)
def create_experience(exp: schemas.ExperienceCreate, db: Session = Depends(database.get_db)):
    new_id = str(uuid.uuid4())
    db_exp = models.Experience(id=new_id, **exp.model_dump())
    db.add(db_exp)
    db.commit()
    db.refresh(db_exp)
    return db_exp

@router.put("/{exp_id}", response_model=schemas.ExperienceResponse)
def update_experience(exp_id: str, exp_update: schemas.ExperienceUpdate, db: Session = Depends(database.get_db)):
    exp = db.query(models.Experience).filter(models.Experience.id == exp_id).first()
    if not exp:
        raise HTTPException(status_code=404, detail="Experience not found")
    update_data = exp_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(exp, key, value)
    db.commit()
    db.refresh(exp)
    return exp

@router.delete("/{exp_id}")
def delete_experience(exp_id: str, db: Session = Depends(database.get_db)):
    exp = db.query(models.Experience).filter(models.Experience.id == exp_id).first()
    if not exp:
        raise HTTPException(status_code=404, detail="Experience not found")
    db.delete(exp)
    db.commit()
    return {"message": "Deleted successfully"}