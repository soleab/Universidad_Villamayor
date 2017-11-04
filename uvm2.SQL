/*
Created: 04/11/2017
Modified: 04/11/2017
Model: PostgreSQL 9.5
Database: PostgreSQL 9.5
*/

-- Create tables section -------------------------------------------------

-- Table Universidad

CREATE TABLE "Universidad"(
 "nombre_uni" Text NOT NULL,
 "direccion_uni" Text NOT NULL,
 "telefono" Numeric NOT NULL,
 "correo" Text NOT NULL,
 "logo" Bigint,
 "web" Text NOT NULL
)
;

-- Add keys for table Universidad

ALTER TABLE "Universidad" ADD CONSTRAINT "Key1" PRIMARY KEY ("nombre_uni")
;

-- Table Carrera

CREATE TABLE "Carrera"(
 "nombre" Text NOT NULL,
 "codigo" Text NOT NULL,
 "creditos_obl" Numeric NOT NULL,
 "creditos_op" Numeric NOT NULL,
 "tfg" Numeric NOT NULL,
 "direccion_facultad" Text,
 "nombre_uni" Text
)
;

-- Create indexes for table Carrera

CREATE INDEX "IX_Relationship19" ON "Carrera" ("direccion_facultad","nombre_uni")
;

-- Add keys for table Carrera

ALTER TABLE "Carrera" ADD CONSTRAINT "Key3" PRIMARY KEY ("codigo")
;

-- Table Asignaturas

CREATE TABLE "Asignaturas"(
 "nombre" Text NOT NULL,
 "tipo" Text NOT NULL,
 "creditos" Numeric NOT NULL,
 "precio" Numeric NOT NULL,
 "codigo" Text,
 "dia" Text,
 "hora" Time,
 "direccion_facultad" Text,
 "nombre_uni" Text
)
;

-- Create indexes for table Asignaturas

CREATE INDEX "IX_Relationship20" ON "Asignaturas" ("codigo")
;

CREATE INDEX "IX_Relationship21" ON "Asignaturas" ("dia","hora","direccion_facultad","nombre_uni")
;

-- Add keys for table Asignaturas

ALTER TABLE "Asignaturas" ADD CONSTRAINT "Key5" PRIMARY KEY ("nombre")
;

-- Table Aula

CREATE TABLE "Aula"(
 "dia" Text NOT NULL,
 "hora" Time NOT NULL,
 "capacidad" Numeric NOT NULL,
 "direccion_facultad" Text NOT NULL,
 "nombre_uni" Text NOT NULL
)
;

-- Add keys for table Aula

ALTER TABLE "Aula" ADD CONSTRAINT "Key6" PRIMARY KEY ("dia","hora","direccion_facultad","nombre_uni")
;

-- Table Facultad

CREATE TABLE "Facultad"(
 "nombre_facultad" Text NOT NULL,
 "direccion_facultad" Text NOT NULL,
 "fax" Numeric,
 "telefono" Numeric NOT NULL,
 "logo" Bigint,
 "correo" Text NOT NULL,
 "nombre_uni" Text NOT NULL
)
;

-- Add keys for table Facultad

ALTER TABLE "Facultad" ADD CONSTRAINT "Key8" PRIMARY KEY ("direccion_facultad","nombre_uni")
;

-- Table Persona

CREATE TABLE "Persona"(
 "nombre" Text NOT NULL,
 "apellido1" Text NOT NULL,
 "apellido2" Text,
 "direccion_persona" Text NOT NULL,
 "telefono" Numeric NOT NULL,
 "correo" Text NOT NULL,
 "DNI" Text NOT NULL,
 "nombre_usuario" Text NOT NULL,
 "contraseña" Text NOT NULL,
 "fecha_nacimiento" Date NOT NULL
)
;

-- Add keys for table Persona

ALTER TABLE "Persona" ADD CONSTRAINT "Key9" PRIMARY KEY ("DNI")
;

ALTER TABLE "Persona" ADD CONSTRAINT "nombre_usuario" UNIQUE ("nombre_usuario")
;

-- Table Profesor

CREATE TABLE "Profesor"(
 "categoria" Text NOT NULL,
 "fecha_inscripcion" Date NOT NULL,
 "tramos_docentes" Numeric NOT NULL,
 "tramos_investigacion" Numeric NOT NULL,
 "DNI" Text NOT NULL,
 "direccion" Text,
 "nombre_uni" Text
)
;

-- Create indexes for table Profesor

CREATE INDEX "IX_Relationship22" ON "Profesor" ("direccion","nombre_uni")
;

-- Add keys for table Profesor

ALTER TABLE "Profesor" ADD CONSTRAINT "Key10" PRIMARY KEY ("DNI")
;

-- Table Departamento

CREATE TABLE "Departamento"(
 "nombre" Text NOT NULL,
 "direccion" Text NOT NULL,
 "nombre_uni" Text NOT NULL
)
;

-- Add keys for table Departamento

ALTER TABLE "Departamento" ADD CONSTRAINT "Key11" PRIMARY KEY ("direccion","nombre_uni")
;

-- Table Alumno

CREATE TABLE "Alumno"(
 "DNI" Text NOT NULL
)
;

-- Add keys for table Alumno

ALTER TABLE "Alumno" ADD CONSTRAINT "Key12" PRIMARY KEY ("DNI")
;

-- Table Matricula

CREATE TABLE "Matricula"(
 "fecha_matricula" Date,
 "id_matricula" Numeric NOT NULL,
 "precio" Numeric,
 "DNI" Text NOT NULL
)
;

-- Add keys for table Matricula

ALTER TABLE "Matricula" ADD CONSTRAINT "Key13" PRIMARY KEY ("id_matricula","DNI")
;

-- Table Matriculado en

CREATE TABLE "Matriculado en"(
 "nombre" Text NOT NULL,
 "id_matricula" Numeric NOT NULL,
 "DNI" Text NOT NULL,
 "nota" Numeric
)
;

-- Add keys for table Matriculado en

ALTER TABLE "Matriculado en" ADD CONSTRAINT "Key14" PRIMARY KEY ("nombre","id_matricula","DNI")
;

-- Create relationships section ------------------------------------------------- 

ALTER TABLE "Facultad" ADD CONSTRAINT "tiene" FOREIGN KEY ("nombre_uni") REFERENCES "Universidad" ("nombre_uni") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Aula" ADD CONSTRAINT "Tiene" FOREIGN KEY ("direccion_facultad", "nombre_uni") REFERENCES "Facultad" ("direccion_facultad", "nombre_uni") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Profesor" ADD CONSTRAINT "Es" FOREIGN KEY ("DNI") REFERENCES "Persona" ("DNI") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Departamento" ADD CONSTRAINT "Tiene" FOREIGN KEY ("direccion", "nombre_uni") REFERENCES "Facultad" ("direccion_facultad", "nombre_uni") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Alumno" ADD CONSTRAINT "Es" FOREIGN KEY ("DNI") REFERENCES "Persona" ("DNI") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Matricula" ADD CONSTRAINT "Tiene" FOREIGN KEY ("DNI") REFERENCES "Alumno" ("DNI") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Matriculado en" ADD CONSTRAINT "Relationship17" FOREIGN KEY ("nombre") REFERENCES "Asignaturas" ("nombre") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Matriculado en" ADD CONSTRAINT "Relationship18" FOREIGN KEY ("id_matricula", "DNI") REFERENCES "Matricula" ("id_matricula", "DNI") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Carrera" ADD CONSTRAINT "Imparte" FOREIGN KEY ("direccion_facultad", "nombre_uni") REFERENCES "Facultad" ("direccion_facultad", "nombre_uni") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Asignaturas" ADD CONSTRAINT "formada por" FOREIGN KEY ("codigo") REFERENCES "Carrera" ("codigo") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Asignaturas" ADD CONSTRAINT "se imparte en" FOREIGN KEY ("dia", "hora", "direccion_facultad", "nombre_uni") REFERENCES "Aula" ("dia", "hora", "direccion_facultad", "nombre_uni") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Profesor" ADD CONSTRAINT "formado por" FOREIGN KEY ("direccion", "nombre_uni") REFERENCES "Departamento" ("direccion", "nombre_uni") ON DELETE NO ACTION ON UPDATE NO ACTION
;




