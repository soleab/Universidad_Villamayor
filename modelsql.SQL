/*
Created: 12/12/2017
Modified: 12/12/2017
Model: PostgreSQL 9.5
Database: PostgreSQL 9.5
*/

-- Create tables section -------------------------------------------------

-- Table Facultades

CREATE TABLE "Facultades"(
 "id" Integer NOT NULL,
 "Nombre" Varchar
)
;

-- Add keys for table Facultades

ALTER TABLE "Facultades" ADD CONSTRAINT "Key1" PRIMARY KEY ("id")
;

-- Table Grados

CREATE TABLE "Grados"(
 "GradoID" Integer NOT NULL,
 "NombreGrado" Varchar,
 "CreditosGrado" Smallint,
 "CreditosOptativos" Smallint,
 "CreditosTransversales" Smallint,
 "id" Integer
)
;

-- Create indexes for table Grados

CREATE INDEX "IX_Relationship1" ON "Grados" ("id")
;

-- Add keys for table Grados

ALTER TABLE "Grados" ADD CONSTRAINT "Key2" PRIMARY KEY ("GradoID")
;

-- Table Alumnos

CREATE TABLE "Alumnos"(
 "NombreCompleto" Text,
 "Dni" Varchar NOT NULL,
 "FechaNacimiento" Date,
 "GradoID" Integer,
 "LoginID" Varchar
)
;

-- Create indexes for table Alumnos

CREATE INDEX "IX_Relationship2" ON "Alumnos" ("GradoID")
;

CREATE INDEX "IX_Relationship9" ON "Alumnos" ("LoginID")
;

-- Add keys for table Alumnos

ALTER TABLE "Alumnos" ADD CONSTRAINT "Key3" PRIMARY KEY ("Dni")
;

-- Table Asignaturas

CREATE TABLE "Asignaturas"(
 "AsignaturaID" Integer NOT NULL,
 "Nombre" Varchar,
 "Creditos" Smallint,
 "Tipo" Varchar,
 "Curso" Smallint,
 "Semestre" Smallint,
 "GradoID" Integer
)
;

-- Create indexes for table Asignaturas

CREATE INDEX "IX_Relationship3" ON "Asignaturas" ("GradoID")
;

-- Add keys for table Asignaturas

ALTER TABLE "Asignaturas" ADD CONSTRAINT "Key4" PRIMARY KEY ("AsignaturaID")
;

-- Table Matricula

CREATE TABLE "Matricula"(
 "MatriculaID" Integer NOT NULL,
 "FechaMatricula" Date,
 "PrecioTotal" Double precision,
 "Estado" Boolean,
 "FormaPago" Integer,
 "Reserva" Boolean,
 "Dni" Varchar,
 "GradoID" Integer
)
;

-- Create indexes for table Matricula

CREATE INDEX "IX_Relationship4" ON "Matricula" ("Dni")
;

CREATE INDEX "IX_Relationship5" ON "Matricula" ("GradoID")
;

-- Add keys for table Matricula

ALTER TABLE "Matricula" ADD CONSTRAINT "Key5" PRIMARY KEY ("MatriculaID")
;

-- Table MatriculaAsignaturas

CREATE TABLE "MatriculaAsignaturas"(
 "Nota" Varchar,
 "NotaNumerica" Double precision,
 "Cursado" Boolean,
 "Convocatoria" Smallint,
 "Evaluacion" Varchar,
 "MatriculaID" Integer NOT NULL,
 "AsignaturaID" Integer NOT NULL
)
;

-- Create indexes for table MatriculaAsignaturas

CREATE INDEX "IX_Relationship6" ON "MatriculaAsignaturas" ("MatriculaID")
;

CREATE INDEX "IX_Relationship7" ON "MatriculaAsignaturas" ("AsignaturaID")
;

-- Table OrdenPago

CREATE TABLE "OrdenPago"(
 "id" Integer NOT NULL,
 "Plazo" Smallint,
 "Importe" Double precision,
 "Pagado" Boolean,
 "FechaOrden" Date,
 "FechaVencimiento" Date,
 "MatriculaID" Integer
)
;

-- Create indexes for table OrdenPago

CREATE INDEX "IX_Relationship8" ON "OrdenPago" ("MatriculaID")
;

-- Add keys for table OrdenPago

ALTER TABLE "OrdenPago" ADD CONSTRAINT "Key7" PRIMARY KEY ("id")
;

-- Table Profesores

CREATE TABLE "Profesores"(
 "NombreCompleto" Varchar,
 "Dni" Varchar NOT NULL,
 "FechaNacimiento" Date,
 "Investigacion" Smallint,
 "Docencia" Smallint,
 "LoginID" Varchar,
 "CategoriaId" Varchar,
 "DepartamentoId" Integer
)
;

-- Create indexes for table Profesores

CREATE INDEX "IX_Relationship10" ON "Profesores" ("LoginID")
;

CREATE INDEX "IX_Relationship11" ON "Profesores" ("CategoriaId")
;

CREATE INDEX "IX_Relationship12" ON "Profesores" ("DepartamentoId")
;

-- Add keys for table Profesores

ALTER TABLE "Profesores" ADD CONSTRAINT "Key8" PRIMARY KEY ("Dni")
;

-- Table Usuarios

CREATE TABLE "Usuarios"(
 "LoginID" Varchar NOT NULL,
 "Contraseña" Varchar,
 "FechaRegistro" Date,
 "email" Varchar
)
;

-- Add keys for table Usuarios

ALTER TABLE "Usuarios" ADD CONSTRAINT "Key9" PRIMARY KEY ("LoginID")
;

-- Table Categoria

CREATE TABLE "Categoria"(
 "Id" Varchar NOT NULL,
 "Tipo" Bigint,
 "HorasDocentes" Smallint,
 "HorasLaborales" Smallint,
 "Sueldo" Double precision
)
;

-- Add keys for table Categoria

ALTER TABLE "Categoria" ADD CONSTRAINT "Key10" PRIMARY KEY ("Id")
;

-- Table Departamento

CREATE TABLE "Departamento"(
 "Id" Integer NOT NULL,
 "CargaDocente" Smallint,
 "HorasDocentes" Smallint
)
;

-- Add keys for table Departamento

ALTER TABLE "Departamento" ADD CONSTRAINT "Key11" PRIMARY KEY ("Id")
;

-- Table PeriodoAcademico

CREATE TABLE "PeriodoAcademico"(
 "Id" Integer NOT NULL,
 "FechaCursoDesde" Date,
 "FechaCursoHasta" Date,
 "FechaMatriculaDesde" Date,
 "FechaMatriculaHasta" Date,
 "Descripcion" Varchar,
 "CursoActual" Boolean,
 "PrecioCreditos" Smallint,
 "Precioreserva" Double precision,
 "FechaEvaluacionEnero" Date,
 "FechaEvaluacionMayo" Date,
 "FechaEvaluacionJunio" Date
)
;

-- Add keys for table PeriodoAcademico

ALTER TABLE "PeriodoAcademico" ADD CONSTRAINT "Key12" PRIMARY KEY ("Id")
;

-- Create relationships section ------------------------------------------------- 

ALTER TABLE "Grados" ADD CONSTRAINT "Relationship1" FOREIGN KEY ("id") REFERENCES "Facultades" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Alumnos" ADD CONSTRAINT "Relationship2" FOREIGN KEY ("GradoID") REFERENCES "Grados" ("GradoID") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Asignaturas" ADD CONSTRAINT "Relationship3" FOREIGN KEY ("GradoID") REFERENCES "Grados" ("GradoID") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Matricula" ADD CONSTRAINT "Relationship4" FOREIGN KEY ("Dni") REFERENCES "Alumnos" ("Dni") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Matricula" ADD CONSTRAINT "Relationship5" FOREIGN KEY ("GradoID") REFERENCES "Grados" ("GradoID") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "MatriculaAsignaturas" ADD CONSTRAINT "Relationship6" FOREIGN KEY ("MatriculaID") REFERENCES "Matricula" ("MatriculaID") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "MatriculaAsignaturas" ADD CONSTRAINT "Relationship7" FOREIGN KEY ("AsignaturaID") REFERENCES "Asignaturas" ("AsignaturaID") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "OrdenPago" ADD CONSTRAINT "Relationship8" FOREIGN KEY ("MatriculaID") REFERENCES "Matricula" ("MatriculaID") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Alumnos" ADD CONSTRAINT "Relationship9" FOREIGN KEY ("LoginID") REFERENCES "Usuarios" ("LoginID") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Profesores" ADD CONSTRAINT "Relationship10" FOREIGN KEY ("LoginID") REFERENCES "Usuarios" ("LoginID") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Profesores" ADD CONSTRAINT "Relationship11" FOREIGN KEY ("CategoriaId") REFERENCES "Categoria" ("Id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "Profesores" ADD CONSTRAINT "Relationship12" FOREIGN KEY ("DepartamentoId") REFERENCES "Departamento" ("Id") ON DELETE NO ACTION ON UPDATE NO ACTION
;




