from fastapi import APIRouter, HTTPException
from database import get_db_connection
from models import Participant
import sqlite3

router = APIRouter(prefix="/participants", tags=["Participants"])

@router.get("/", summary="Lihat semua peserta")
def get_participants():
    conn = get_db_connection()
    rows = conn.execute("""
        SELECT participants.id, participants.name, participants.email, events.title AS event_title
        FROM participants
        JOIN events ON participants.event_id = events.id
        ORDER BY participants.id DESC
    """).fetchall()
    conn.close()
    return {"status": "success", "data": [dict(r) for r in rows]}

@router.post("/register", summary="Daftarkan peserta ke event")
def register_participant(p: Participant):
    conn = get_db_connection()
    try:
        conn.execute(
            "INSERT INTO participants (name, email, event_id) VALUES (?, ?, ?)",
            (p.name, p.email, p.event_id)
        )
        conn.commit()
        conn.close()
        return {"status": "success", "message": "Peserta berhasil didaftarkan"}
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Email sudah terdaftar")
