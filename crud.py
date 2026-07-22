import models
import schemas
from sqlalchemy.orm import Session
# pyrefly: ignore [missing-import]
import models
# pyrefly: ignore [missing-import]
import schemas
import uuid

# ==========================================
# CREATE: Menambah Project Baru
# ==========================================
def create_project(db: Session, project: schemas.ProjectCreate):
    # Karena Prisma menggunakan cuid, di Python kita bisa menggunakan uuid4
    # sebagai ID unik yang setara keamanannya.
    new_project_id = str(uuid.uuid4())
    
    db_project = models.Project(
        id=new_project_id,
        title=project.title,
        category=project.category,
        problem=project.problem,
        contribution=project.contribution,
        result=project.result,
        techStack=project.techStack, # PostgreSQL mendukung tipe data Array secara native
        liveUrl=project.liveUrl,
        caseStudyUrl=project.caseStudyUrl,
        imageUrl=project.imageUrl,
        featured=project.featured,
        order=project.order,
        visible=project.visible
    )
    
    db.add(db_project)      # Simpan di memori
    db.commit()             # Permanenkan ke database
    db.refresh(db_project)  # Ambil data terbaru dari database (termasuk createdAt)
    
    return db_project

# ==========================================
# READ: Mengambil Semua Project
# ==========================================
def get_projects(db: Session, skip: int = 0, limit: int = 100, visible_only: bool = False):
    query = db.query(models.Project)
    
    # Fitur filter: berguna untuk UI utama (hanya tampilkan yang visible)
    if visible_only:
        query = query.filter(models.Project.visible == True)
        
    # Urutkan berdasarkan kolom 'order' (sesuai skema kamu)
    return query.order_by(models.Project.order.asc()).offset(skip).limit(limit).all()

# ==========================================
# READ: Mengambil Satu Project (Berdasarkan ID)
# ==========================================
def get_project_by_id(db: Session, project_id: str):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

# ==========================================
# UPDATE: Mengedit Project
# ==========================================
def update_project(db: Session, project_id: str, project_update: schemas.ProjectUpdate):
    db_project = get_project_by_id(db, project_id)
    
    if not db_project:
        return None
        
    # Mengambil hanya data yang dikirimkan oleh user untuk di-update (exclude_unset)
    update_data = project_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_project, key, value)
        
    db.commit()
    db.refresh(db_project)
    
    return db_project

# ==========================================
# DELETE: Menghapus Project
# ==========================================
def delete_project(db: Session, project_id: str):
    db_project = get_project_by_id(db, project_id)
    
    if db_project:
        db.delete(db_project)
        db.commit()
        return True
        
    return False
