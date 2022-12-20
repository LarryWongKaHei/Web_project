DROP TABLE IF EXISTS class_attend;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS members;


CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    membership_level VARCHAR(255),
    gender VARCHAR(255),
    availability VARCHAR(255),
    salary INT,
    status BOOLEAN
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    fee INT,
    gender VARCHAR(255),
    availability VARCHAR(255),
    duration INT,
    max_capacity INT
);

CREATE TABLE class_attend (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    classes_id INT REFERENCES classes(id) ON DELETE CASCADE
);
