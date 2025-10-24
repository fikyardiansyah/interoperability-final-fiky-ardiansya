from fastapi import APIRouter, HTTPException
from database import get_db_connection
from models import Event

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/", summary="Lihat semua event")
def get_events():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM events ORDER BY date ASC").fetchall()
    conn.close()
    return {"status": "success", "data": [dict(r) for r in rows]}

@router.post("/", summary="Tambah event baru")
def add_event(event: Event):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO events (title, date, location, quota) VALUES (?, ?, ?, ?)",
        (event.title, event.date, event.location, event.quota)
    )
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Event berhasil ditambahkan"}

@router.put("/{event_id}", summary="Edit data event")
def update_event(event_id: int, event: Event):
    conn = get_db_connection()
    cur = conn.execute(
        "UPDATE events SET title=?, date=?, location=?, quota=? WHERE id=?",
        (event.title, event.date, event.location, event.quota, event_id)
    )
    conn.commit()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Event tidak ditemukan")
    conn.close()
    return {"status": "success", "message": "Event berhasil diperbarui"}

@router.delete("/{event_id}", summary="Hapus event")
def delete_event(event_id: int):
    conn = get_db_connection()
    cur = conn.execute("DELETE FROM events WHERE id=?", (event_id,))
    conn.commit()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Event tidak ditemukan")
    conn.close()
    return {"status": "success", "message": "Event berhasil dihapus"}
