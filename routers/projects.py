# pyrefly: ignore [missing-import]
import crud
import database
import schemas
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
# pyrefly: ignore [missing-import]
import crud, schemas, database  

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.post("/", response_model=schemas.ProjectResponse)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(database.get_db)):
    return crud.create_project(db=db, project=project)

@router.get("/", response_model=List[schemas.ProjectResponse])
def read_projects(skip: int = 0, limit: int = 100, visible_only: bool = False, db: Session = Depends(database.get_db)):
    return crud.get_projects(db, skip=skip, limit=limit, visible_only=visible_only)

@router.put("/{project_id}", response_model=schemas.ProjectResponse)
def update_project(project_id: str, project_update: schemas.ProjectUpdate, db: Session = Depends(database.get_db)):
    updated_project = crud.update_project(db=db, project_id=project_id, project_update=project_update)
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project

@router.delete("/{project_id}")
def delete_project(project_id: str, db: Session = Depends(database.get_db)):
    success = crud.delete_project(db=db, project_id=project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}