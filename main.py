from routers import education
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import models
from database import engine

# 1. Import semua router dari folder routers/
from routers import projects, profile, experience, education, certifications

# 2. Membuat tabel di database jika belum ada
models.Base.metadata.create_all(bind=engine)

# 3. DEFINISIKAN 'app' DI SINI
app = FastAPI(title="Portfolio API")

# 4. Konfigurasi CORS agar frontend bisa akses API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 5. Setup folder uploads untuk foto dokumentasi
os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    return {"imageUrl": f"http://127.0.0.1:8000/{file_location}"}

# 6. DAFTARKAN ROUTER (Pastikan ini ada di BAWAH app = FastAPI())
app.include_router(projects.router)
app.include_router(profile.router)
app.include_router(experience.router)
app.include_router(education.router)
app.include_router(certifications.router)
# 7. Endpoint utama
@app.get("/")
def read_root():
    return {"message": "API is running"}