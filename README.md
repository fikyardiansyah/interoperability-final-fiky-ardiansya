# 🎓 Campus Event Registration Platform

**UTS - Interoperability**
Politeknik Negeri Bali – Jurusan Teknologi Informasi

## 📘 Deskripsi Singkat

Proyek ini adalah implementasi sederhana sistem pendaftaran event kampus untuk tugas Ujian Tengah Semester (UTS) mata kuliah *Interoperability*. Sistem menunjukkan interoperabilitas antara komponen backend, database, dan frontend:

* Backend: FastAPI (atau Flask)
* Database: MySQL (atau SQLite)
* Frontend/Client: HTML + Fetch API (atau Python CLI)

Fungsionalitas utama: melihat daftar event, CRUD event, pendaftaran peserta, dan relasi one-to-many antara `events` dan `participants`.

---

## ⚙️ Fitur Utama

* **Manajemen Event (CRUD)**

  * Melihat daftar event
  * Menambah event baru
  * Mengubah data event
  * Menghapus event
* **Pendaftaran Peserta**

  * Mendaftarkan peserta ke event
  * Menampilkan daftar peserta
* **Relasi Antar Tabel**

  * Relasi one-to-many: satu event memiliki banyak participants
* **Frontend Sederhana**

  * Halaman HTML dengan Fetch API untuk menampilkan event dan formulir pendaftaran
* **(Bonus)** Autentikasi Token untuk akses admin (opsional)
* **(Bonus)** Dokumentasi API otomatis (FastAPI Swagger)

---

## 📁 Struktur Direktori (contoh)

```
project-root/
├─ backend/
│  ├─ main.py
│  ├─ models.py
│  ├─ schemas.py
│  ├─ crud.py
│  ├─ database.py
│  ├─ requirements.txt
│  └─ README.md
├─ frontend/
│  ├─ index.html
│  ├─ styles.css
│  
├─ README.md   
└─ .gitignore
```

---

## 🛠️ Teknologi

* Python 3.10+
* FastAPI (direkomendasikan) atau Flask
* Uvicorn sebagai ASGI server
* SQLAlchemy + Alembic (opsional) atau langsung sqlite/mysql
* HTML + Fetch API untuk frontend

---

## 🚀 Instalasi & Menjalankan (Langkah-per-langkah)

> Contoh menggunakan FastAPI dan SQLite (pengaturan sederhana untuk development)

### 1. Siapkan virtual environment

```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Menjalankan Backend (FastAPI)

```bash
# berada di folder backend
python -m uvicorn main:app --reload
```

Server akan berjalan di: `http://127.0.0.1:8000`

Untuk melihat dokumentasi otomatis (Swagger UI): `http://127.0.0.1:8000/docs`

### 3. Menjalankan Frontend (HTML static)

```bash
cd frontend
python -m http.server 5500
```

Frontend akan tersedia di: `http://127.0.0.1:5500/index.html`

> Pastikan `API_URL` di `frontend/app.js` (atau `index.html`) mengarah ke `http://127.0.0.1:8000`.

---

## 🔗 Endpoints API (ringkasan)

| Metode | Endpoint                 | Deskripsi                 |
| ------ | ------------------------ | ------------------------- |
| GET    | `/events`                | Menampilkan semua event   |
| POST   | `/events`                | Menambahkan event baru    |
| PUT    | `/events/{id}`           | Mengedit data event       |
| DELETE | `/events/{id}`           | Menghapus event           |
| GET    | `/participants`          | Menampilkan semua peserta |
| POST   | `/participants/register` | Mendaftarkan peserta baru |

> Jika menggunakan FastAPI, dokumentasi endpoint akan tersedia otomatis di `/docs`.

---

## 🧩 Contoh Skema Database (SQLAlchemy)

```python
# models.py (singkat)
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    date = Column(String(50), nullable=True)
    location = Column(String(255), nullable=True)

    participants = relationship('Participant', back_populates='event', cascade='all, delete')

class Participant(Base):
    __tablename__ = 'participants'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'))

    event = relationship('Event', back_populates='participants')
```

---

## ✅ Contoh Request (Fetch API)

```javascript
const API_URL = "http://127.0.0.1:8000";

// ambil semua event
fetch(`${API_URL}/events`)
  .then(r => r.json())
  .then(data => console.log(data));

// register participant
fetch(`${API_URL}/participants/register`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'Budi', email: 'budi@example.com', event_id: 1 })
})
  .then(r => r.json())
  .then(resp => console.log(resp));
```

---

## 🔐 (Bonus) Autentikasi Token (Opsional)

* Untuk akses Admin (menambah/hapus event), bisa implementasikan JWT Token sederhana.
* Endpoint admin diberi dependency `get_current_user` yang memverifikasi token.
* Pada frontend, simpan token di `localStorage` dan sertakan header `Authorization: Bearer <token>` pada request yang membutuhkan.

---

## 📚 Testing & Dokumentasi

* Gunakan `pytest` untuk unit test sederhana (opsional)
* FastAPI menyediakan dokumentasi interaktif di `/docs`

---

## 💡 Tips & Perbaikan untuk GitHub

* Tambahkan `requirements.txt` yang jelas (`fastapi`, `uvicorn`, `sqlalchemy`, `databases`/`aiomysql` jika perlu)
* Sertakan `example.env` jika menggunakan konfigurasi berbasis env (DB URL, SECRET_KEY)
* Tambahkan `Makefile` atau skrip `run.sh` untuk ease-of-use
* Buat file `CONTRIBUTING.md` singkat jika ingin kolaborasi
* Tambahkan screenshot frontend di `README.md` untuk tampilan visual

---



## 👤 Kontributor

* Nama: *[Moh Fiky Ardiansyah]*
* Mata Kuliah: Interoperability (UTS)
* Politeknik Negeri Bali - Jurusan Teknologi Informasi

---

