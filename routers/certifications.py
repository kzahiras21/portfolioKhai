from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database
import uuid

router = APIRouter(prefix="/certifications", tags=["Certifications"])

@router.get("/", response_model=List[schemas.CertificationResponse])
def get_certifications(db: Session = Depends(database.get_db)):
    return db.query(models.Certification).order_by(models.Certification.order.asc()).all()

@router.post("/", response_model=schemas.CertificationResponse)
def create_certification(cert: schemas.CertificationCreate, db: Session = Depends(database.get_db)):
    new_id = str(uuid.uuid4())
    db_cert = models.Certification(id=new_id, **cert.model_dump())
    db.add(db_cert)
    db.commit()
    db.refresh(db_cert)
    return db_cert

@router.put("/{cert_id}", response_model=schemas.CertificationResponse)
def update_certification(cert_id: str, cert_update: schemas.CertificationUpdate, db: Session = Depends(database.get_db)):
    cert = db.query(models.Certification).filter(models.Certification.id == cert_id).first()
    if not cert:
        raise HTTPException(status_code=404, detail="Certification not found")
    update_data = cert_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(cert, key, value)
    db.commit()
    db.refresh(cert)
    return cert

@router.delete("/{cert_id}")
def delete_certification(cert_id: str, db: Session = Depends(database.get_db)):
    cert = db.query(models.Certification).filter(models.Certification.id == cert_id).first()
    if not cert:
        raise HTTPException(status_code=404, detail="Certification not found")
    db.delete(cert)
    db.commit()
    return {"message": "Deleted successfully"}