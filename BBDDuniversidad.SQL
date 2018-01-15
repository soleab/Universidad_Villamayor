/*
Created: 16/10/2017
Modified: 17/10/2017
Model: PostgreSQL 9.5
Database: PostgreSQL 9.5
*/

-- Create tables section -------------------------------------------------

-- Table Persona

CREATE TABLE "Persona"(
 "dni" Text NOT NULL,
 "nombre" Text NOT NULL,
 "apellidos" Text NOT NULL,
 "tipo_perfil" Text NOT NULL,
 "contrasena" Text,
 "telefono" Integer,
 "direccion" Text
)
;

-- Add keys for table Persona

ALTER TABLE "Persona" ADD CONSTRAINT "Key1" PRIMARY KEY ("dni")
;

-- Table Alumno

CREATE TABLE "Alumno"(
 "dni" Text NOT NULL,
 "carrera" Bigint,
 "matricula" Bigint
)
;

-- Create indexes for table Alumno

CREATE INDEX "IX_Relationship3" ON "Alumno" ("dni")
;

-- Add keys for table Alumno

ALTER TABLE "Alumno" ADD CONSTRAINT "Key4" PRIMARY KEY ("dni")
;

-- Table Profesor

CREATE TABLE "Profesor"(
 "dni" Text NOT NULL,
 "fecha_inscripción" Date NOT NULL,
 "categoria" Text NOT NULL,
 "num_tramos_docentes" Integer NOT NULL,
 "num_tramos_investigacion" Integer NOT NULL
)
;

-- Create indexes for table Profesor

CREATE INDEX "IX_Relationship4" ON "Profesor" ("dni")
;

-- Add keys for table Profesor

ALTER TABLE "Profesor" ADD CONSTRAINT "Key5" PRIMARY KEY ("dni")
;

-- Table Facultades

CREATE TABLE "Facultades"(
 "direccion" Text NOT NULL,
 "telefono" Integer NOT NULL,
 "fax" Integer,
 "nombreUniversidad" Text NOT NULL,
 "correo_electronico" Text
)
;

-- Add keys for table Facultades

ALTER TABLE "Facultades" ADD CONSTRAINT "Key6" PRIMARY KEY ("direccion","nombreUniversidad")
;

-- Table Universidad

CREATE TABLE "Universidad"(
 "nombreUniversidad" Text NOT NULL,
 "direccion" Text NOT NULL,
 "correo_electronico" Text NOT NULL,
 "telefono" Text NOT NULL,
 "logotipo" Text NOT NULL,
 "web" Text NOT NULL
)
;

-- Add keys for table Universidad

ALTER TABLE "Universidad" ADD CONSTRAINT "Key7" PRIMARY KEY ("nombreUniversidad")
;

-- Table tiene

CREATE TABLE "tiene"(
 "nombreUniversidad" Text NOT NULL,
 "direccion" Text NOT NULL,
 "nombre" Text NOT NULL
)
;

-- Add keys for table tiene

ALTER TABLE "tiene" ADD CONSTRAINT "Key8" PRIMARY KEY ("nombreUniversidad","direccion","nombre")
;

-- Table Carrera

CREATE TABLE "Carrera"(
 "nombreCarrera" Text NOT NULL,
 "creditos" Integer NOT NULL,
 "direccion" Text NOT NULL,
 "nombre" Text NOT NULL
)
;

-- Add keys for table Carrera

ALTER TABLE "Carrera" ADD CONSTRAINT "Key9" PRIMARY KEY ("nombreCarrera","direccion","nombre")
;

-- Table Asignaturas

CREATE TABLE "Asignaturas"(
 "codigo" Integer NOT NULL,
 "nombre" Text NOT NULL,
 "creditos" Integer NOT NULL,
 "caracter" Text NOT NULL
)
;

-- Add keys for table Asignaturas

ALTER TABLE "Asignaturas" ADD CONSTRAINT "Key10" PRIMARY KEY ("codigo")
;

-- Table imparte

CREATE TABLE "imparte"(
 "dni" Text NOT NULL,
 "codigo" Integer NOT NULL
)
;

-- Add keys for table imparte

ALTER TABLE "imparte" ADD CONSTRAINT "Key11" PRIMARY KEY ("dni","codigo")
;

-- Table impartida_en

CREATE TABLE "impartida_en"(
 "codigo" Integer NOT NULL,
 "nombreCarrera" Text NOT NULL,
 "direccion" Text NOT NULL,
 "nombre" Text NOT NULL
)
;

-- Add keys for table impartida_en

ALTER TABLE "impartida_en" ADD CONSTRAINT "Key12" PRIMARY KEY ("codigo","nombreCarrera","direccion","nombre")
;

-- Table Matricula

CREATE TABLE "Matricula"(
 "periodo_finalizado" Boolean,
 "codigoMatricula" Text NOT NULL,
 "curso" Text
)
;

-- Add keys for table Matricula

ALTER TABLE "Matricula" ADD CONSTRAINT "Key13" PRIMARY KEY ("codigoMatricula")
;

-- Table asignadoa

CREATE TABLE "asignadoa"(
 "dni" Text NOT NULL,
 "codigo" Text NOT NULL
)
;

-- Add keys for table asignadoa

ALTER TABLE "asignadoa" ADD CONSTRAINT "Key14" PRIMARY KEY ("dni","codigo")
;

-- Table matriculado

CREATE TABLE "matriculado"(
 "codigoMatricula" Text NOT NULL,
 "codigo" Integer NOT NULL,
 "cursada" Boolean NOT NULL,
 "nota" Integer
)
;

-- Add keys for table matriculado

ALTER TABLE "matriculado" ADD CONSTRAINT "Key15" PRIMARY KEY ("codigoMatricula","codigo")
;

-- Create relationships section ------------------------------------------------- 

ALTER TABLE "Alumno" ADD CONSTRAINT "es" FOREIGN KEY ("dni") REFERENCES "Persona" ("dni") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Profesor" ADD CONSTRAINT "es1" FOREIGN KEY ("dni") REFERENCES "Persona" ("dni") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "tiene" ADD CONSTRAINT "Relationship3" FOREIGN KEY ("nombreUniversidad") REFERENCES "Universidad" ("nombreUniversidad") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "tiene" ADD CONSTRAINT "Relationship4" FOREIGN KEY ("direccion", "nombre") REFERENCES "Facultades" ("direccion", "nombreUniversidad") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Facultades" ADD CONSTRAINT "Relationship6" FOREIGN KEY ("nombreUniversidad") REFERENCES "Universidad" ("nombreUniversidad") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Carrera" ADD CONSTRAINT "Relationship7" FOREIGN KEY ("direccion", "nombre") REFERENCES "Facultades" ("direccion", "nombreUniversidad") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "imparte" ADD CONSTRAINT "Relationship9" FOREIGN KEY ("dni") REFERENCES "Profesor" ("dni") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "imparte" ADD CONSTRAINT "Relationship10" FOREIGN KEY ("codigo") REFERENCES "Asignaturas" ("codigo") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "impartida_en" ADD CONSTRAINT "Relationship11" FOREIGN KEY ("codigo") REFERENCES "Asignaturas" ("codigo") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "impartida_en" ADD CONSTRAINT "Relationship12" FOREIGN KEY ("nombreCarrera", "direccion", "nombre") REFERENCES "Carrera" ("nombreCarrera", "direccion", "nombre") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "asignadoa" ADD CONSTRAINT "Relationship13" FOREIGN KEY ("dni") REFERENCES "Alumno" ("dni") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "asignadoa" ADD CONSTRAINT "Relationship14" FOREIGN KEY ("codigo") REFERENCES "Matricula" ("codigoMatricula") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "matriculado" ADD CONSTRAINT "Relationship15" FOREIGN KEY ("codigoMatricula") REFERENCES "Matricula" ("codigoMatricula") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "matriculado" ADD CONSTRAINT "Relationship16" FOREIGN KEY ("codigo") REFERENCES "Asignaturas" ("codigo") ON DELETE NO ACTION ON UPDATE NO ACTION
;




