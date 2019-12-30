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

DROP TABLE IF exists maillist;
CREATE TABLE maillist (
    id integer primary key autoincrement,
    fullname text not null,
    email varchar(64)
);
