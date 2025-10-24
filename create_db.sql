-- Hapus tabel lama jika ada
DROP TABLE IF EXISTS participants;
DROP TABLE IF EXISTS events;

-- Tabel events
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    date TEXT NOT NULL,
    location TEXT NOT NULL,
    quota INTEGER NOT NULL
);

-- Tabel participants
CREATE TABLE participants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    event_id INTEGER,
    FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
);

-- Data awal
INSERT INTO events (title, date, location, quota) VALUES
('Belajar Pemrograman Web', '2023-12-15', 'Gedung G FTI', 50),
('Seminar Nasional AI', '2023-12-20', 'Aula Politeknik', 200);

-- -- Hapus tabel lama jika ada
-- DROP TABLE IF EXISTS participants;
-- DROP TABLE IF EXISTS events;

-- -- Tabel 1: events
-- CREATE TABLE events (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     title VARCHAR(100) NOT NULL,
--     date DATE NOT NULL,
--     location VARCHAR(100) NOT NULL,
--     quota INT NOT NULL
-- );

-- -- Tabel 2: participants
-- CREATE TABLE participants (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     email VARCHAR(100) NOT NULL UNIQUE,
--     event_id INT,
--     FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
-- );

-- -- Data awal untuk testing
-- INSERT INTO events (title, date, location, quota) VALUES
-- ('belajar Pemrograman Web', '2023-12-15', 'Gedung G FTI', 50),
-- ('Seminar Nasional AI', '2023-12-20', 'Aula Politeknik', 200);
