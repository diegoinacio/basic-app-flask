-- sqlite3 people.db < init_tables.sql

DROP TABLE IF exists person;
CREATE TABLE person (
    id integer primary key autoincrement,
    name text not null,
    title text not null,
    descript text,
    email varchar(64),
    img varchar(64)
);
