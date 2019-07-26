--
-- File generated with SQLiteStudio v3.2.1 on qui jul 25 21:52:33 2019
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: tb_faces
CREATE TABLE tb_faces (
    cd_id     INTEGER PRIMARY KEY AUTOINCREMENT
                      NOT NULL,
    nm_client STRING  NOT NULL,
    cd_dir            NOT NULL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
