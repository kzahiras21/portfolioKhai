import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Memuat variabel environment dari file .env
load_dotenv()

# Contoh isi .env: DATABASE_URL="postgresql://postgres:password@localhost:5432/portfolio"
# Jika menggunakan Supabase PostgreSQL, gunakan URL koneksinya di sini.
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Membuat 'mesin' koneksi ke database PostgreSQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal adalah kelas pabrik yang akan menghasilkan sesi (koneksi aktif) tiap kali API dipanggil
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base adalah kelas induk yang akan diwarisi oleh semua model tabel (models.py)
Base = declarative_base()

# Dependency function:
# Fungsi ini akan 'di-inject' ke dalam setiap route FastAPI.
# Tujuannya agar tiap request API mendapat sesi database sendiri dan otomatis ditutup setelah selesai.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
