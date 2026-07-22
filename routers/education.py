from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database
import uuid

router = APIRouter(prefix="/educations", tags=["Education"])

@router.get("/", response_model=List[schemas.EducationResponse])
def get_educations(db: Session = Depends(database.get_db)):
    return db.query(models.Education).order_by(models.Education.order.asc()).all()

@router.post("/", response_model=schemas.EducationResponse)
def create_education(edu: schemas.EducationCreate, db: Session = Depends(database.get_db)):
    new_id = str(uuid.uuid4())
    db_edu = models.Education(id=new_id, **edu.model_dump())
    db.add(db_edu)
    db.commit()
    db.refresh(db_edu)
    return db_edu

@router.put("/{edu_id}", response_model=schemas.EducationResponse)
def update_education(edu_id: str, edu_update: schemas.EducationUpdate, db: Session = Depends(database.get_db)):
    edu = db.query(models.Education).filter(models.Education.id == edu_id).first()
    if not edu:
        raise HTTPException(status_code=404, detail="Education not found")
    update_data = edu_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(edu, key, value)
    db.commit()
    db.refresh(edu)
    return edu

@router.delete("/{edu_id}")
def delete_education(edu_id: str, db: Session = Depends(database.get_db)):
    edu = db.query(models.Education).filter(models.Education.id == edu_id).first()
    if not edu:
        raise HTTPException(status_code=404, detail="Education not found")
    db.delete(edu)
    db.commit()
    return {"message": "Deleted successfully"}