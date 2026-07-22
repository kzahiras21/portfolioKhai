from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.get("/", response_model=schemas.ProfileUpdate)
def get_profile(db: Session = Depends(database.get_db)):
    profile = db.query(models.Profile).filter(models.Profile.id == 1).first()
    if not profile:
        # Buat data default jika belum ada di database
        profile = models.Profile(id=1, aboutBody="I build intelligent systems focusing on machine learning...")
        db.add(profile)
        db.commit()
        db.refresh(profile)
    return profile

@router.put("/", response_model=schemas.ProfileUpdate)
def update_profile(profile_update: schemas.ProfileUpdate, db: Session = Depends(database.get_db)):
    profile = db.query(models.Profile).filter(models.Profile.id == 1).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    update_data = profile_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(profile, key, value)
        
    db.commit()
    db.refresh(profile)
    return profile