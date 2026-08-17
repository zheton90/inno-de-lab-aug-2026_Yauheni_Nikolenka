-- CREATE TABLE

CREATE TABLE Departments (
DepartmentID SERIAL PRIMARY KEY,
DepartmentName VARCHAR(50) UNIQUE NOT NULL,
LOCATION VARCHAR(50)
);

-- ADD COLUMN

ALTER TABLE employees ADD COLUMN Email VARCHAR(100)

-- ADD Email

UPDATE employees e
SET  email = e.firstname || e.lastname || '@gmail.com'
WHERE email IS NULL



ALTER TABLE employees ADD CONSTRAINT uniq_employees_email UNIQUE (Email)-- CREATE TABLE

CREATE TABLE Departments (
DepartmentID SERIAL PRIMARY KEY,
DepartmentName VARCHAR(50) UNIQUE NOT NULL,
LOCATION VARCHAR(50)
);

-- ADD COLUMN

ALTER TABLE employees ADD COLUMN Email VARCHAR(100)

-- ADD Email

UPDATE employees e
SET  email = e.firstname || e.lastname || '@gmail.com'
WHERE email IS NULL



ALTER TABLE employees ADD CONSTRAINT uniq_employees_email UNIQUE (Email)-- CREATE TABLE

CREATE TABLE Departments (
DepartmentID SERIAL PRIMARY KEY,
DepartmentName VARCHAR(50) UNIQUE NOT NULL,
LOCATION VARCHAR(50)
);

-- ADD COLUMN

ALTER TABLE employees ADD COLUMN Email VARCHAR(100)

-- ADD Email

UPDATE employees e
SET  email = e.firstname || e.lastname || '@gmail.com'
WHERE email IS NULL

-- ADD CONSTRAINT

ALTER TABLE employees ADD CONSTRAINT uniq_employees_email UNIQUE (Email)

-- RENAME COLUMN

ALTER TABLE departments RENAME COLUMN "location" TO "OfficeLocation"