from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import events, participants
import os
import sqlite3

app = FastAPI(
    title="Campus Event Registration API (SQLite)",
    description="Sistem Registrasi Event Kampus menggunakan SQLite",
    version="1.0.0"
)

# 🔧 Izinkan frontend (HTML/JS) mengakses API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Lokasi file database dan SQL ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "campus_event.db")

# Cari file SQL di dua tempat: backend/ atau root/
SQL_FILE = os.path.join(BASE_DIR, "create_db.sql")
if not os.path.exists(SQL_FILE):
    SQL_FILE = os.path.join(os.path.dirname(BASE_DIR), "create_db.sql")

# --- Buat database otomatis jika belum ada ---
if not os.path.exists(DB_PATH):
    print("🛠️ Membuat database SQLite baru dari create_db.sql ...")
    try:
        conn = sqlite3.connect(DB_PATH)
        with open(SQL_FILE, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()
        print("✅ Database SQLite berhasil dibuat!")
    except FileNotFoundError:
        print("❌ Gagal: File create_db.sql tidak ditemukan.")
    except Exception as e:
        print(f"⚠️ Terjadi kesalahan saat membuat database: {e}")
else:
    print("✅ Database SQLite sudah ada, langsung digunakan.")

# --- Daftarkan semua route ---
app.include_router(events.router)
app.include_router(participants.router)

# --- Root endpoint ---
@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Selamat datang di API Registrasi Event Kampus (SQLite) 👋",
        "docs": "Lihat dokumentasi lengkap di /docs"
    }
