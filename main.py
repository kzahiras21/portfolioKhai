from fastapi import FastAPI, File, UploadFile, Request
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

# 3. Definisi App
app = FastAPI(title="Portfolio API")

# 4. Konfigurasi CORS agar Vercel/Frontend bisa akses
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 5. Setup folder uploads untuk foto
os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.post("/upload/")
async def upload_image(request: Request, file: UploadFile = File(...)):
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    
    # ✅ Dibuat dinamis mengikuti domain (Railway/Localhost)
    base_url = str(request.base_url).rstrip("/")
    return {"imageUrl": f"{base_url}/{file_location}"}

# 6. Daftarkan Router
app.include_router(projects.router)
app.include_router(profile.router)
app.include_router(experience.router)
app.include_router(education.router)
app.include_router(certifications.router)

# 7. Endpoint utama
@app.get("/")
def read_root():
    return {"message": "API is running"}
