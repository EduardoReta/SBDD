CREATE DATABASE dbBiblioteca
use dbBiblioteca

-- Secciones

CREATE TABLE catSECCIONES(
	ID_ESTANTE INT NOT NULL PRIMARY KEY, 
	DESC_ESTANTE VARCHAR (25) NOT NULL,
	ID_REPISA SMALLINT NOT NULL,
);

DROP 


INSERT INTO catSECCIONES 
VALUES (1101,
		'Estante 1, repisa 1',
		01);

INSERT INTO catSECCIONES 
VALUES (1102,
		'Estante 1, repisa 2',
		02);

INSERT INTO catSECCIONES 
VALUES (1103,
		'Estante 1, repisa 3',
		03);

INSERT INTO catSECCIONES 
VALUES (1201,
		'Estante 2, repisa 1',
		01);

INSERT INTO catSECCIONES 
VALUES (1202,
		'Estante 2, repisa 2',
		02);

INSERT INTO catSECCIONES 
VALUES (1203,
		'Estante 2, repisa 3',
		03);

INSERT INTO catSECCIONES 
VALUES (1301,
		'Estante 3, repisa 1',
		01);

INSERT INTO catSECCIONES 
VALUES (1302,
		'Estante 3, repisa 2',
		02);

INSERT INTO catSECCIONES 
VALUES (1303,
		'Estante 3, repisa 3',
		03);


SELECT * FROM catSECCIONES

-- PUESTOS DE EMPLEADOS

CREATE TABLE catPUESTO(
	ID_PUESTO INT NOT NULL PRIMARY KEY, 
	DESC_PUESTO VARCHAR (50) NOT NULL,
);

SELECT * FROM catPUESTO

INSERT INTO catPUESTO
VALUES (2001,
		'Jefe de servicios sala y prestamo');

INSERT INTO catPUESTO
VALUES (2002,
		'Bibliotecario');

INSERT INTO catPUESTO
VALUES (2003,
		'Soporte Técnico');

INSERT INTO catPUESTO
VALUES (2004,
		'Direccion de Biblioteca');

-- IDIOMAS

CREATE TABLE catIDIOMA(
	ID_IDIOMA INT NOT NULL PRIMARY KEY, 
	DESC_IDIOMA VARCHAR (20) NOT NULL,
);

SELECT * FROM catIDIOMA

INSERT INTO catIDIOMA
VALUES (3001,
		'Español');

INSERT INTO catIDIOMA
VALUES (3002,
		'Ingles');

INSERT INTO catIDIOMA
VALUES (3003,
		'Frances');

INSERT INTO catIDIOMA
VALUES (3004,
		'Aleman');

INSERT INTO catIDIOMA
VALUES (3005,
		'Italiano');

DROP TABLE catLIBRO_AUTOR


-- GENERO

CREATE TABLE catGENERO(
	ID_GENERO INT NOT NULL PRIMARY KEY, 
	DESC_GENERO VARCHAR (50) NOT NULL,
);

SELECT * FROM catGENERO

INSERT INTO catGENERO
VALUES (4001,
		'Aventuras');

INSERT INTO catGENERO
VALUES (4002,
		'Ciencia ficción');

INSERT INTO catGENERO
VALUES (4003,
		'Gótico');

INSERT INTO catGENERO
VALUES (4004,
		'Divulgación Científica');

INSERT INTO catGENERO
VALUES (4005,
		'Policiaco');

INSERT INTO catGENERO
VALUES (4006,
		'Fantasia');

INSERT INTO catGENERO
VALUES (4007,
		'Distópico');

-- CASAS EDITORIALES

CREATE TABLE catEDITORIAL(
	ID_EDITORIAL INT NOT NULL PRIMARY KEY, 
	DESC_EDITORIAL VARCHAR (50) NOT NULL,
);

SELECT * FROM catEDITORIAL

INSERT INTO catEDITORIAL
VALUES (5001,
		'Alias Editorial');

INSERT INTO catEDITORIAL
VALUES (5002,
		'AM Editores');

INSERT INTO catEDITORIAL
VALUES (5003,
		'Amate Editorial');

INSERT INTO catEDITORIAL
VALUES (5004,
		'Caligrama Editores');

INSERT INTO catEDITORIAL
VALUES (5005,
		'Ediciones el Naranjo');

INSERT INTO catEDITORIAL
VALUES (5006,
		'Ediciones Era');

INSERT INTO catEDITORIAL
VALUES (5007,
		'Editorial CIDCLI');

-- TURNOS / HORARIOS DE TRABAJO

CREATE TABLE catTURNOS(
	ID_TURNOS INT NOT NULL PRIMARY KEY, 
	DESC_TURNO VARCHAR (35) NOT NULL,
);

SELECT * FROM catTURNOS
DROP TABLE catTURNOS

INSERT INTO catTURNOS
VALUES (6001,
		'Matutino: 7:00 AM a 12:00 PM');

INSERT INTO catTURNOS
VALUES (6002,
		'Vespertino: 12:00 PM a 8:00 PM');

-- Tipo de Libro

CREATE TABLE catTIPO_LIBRO(
	ID_TIPOLIBRO INT NOT NULL PRIMARY KEY, 
	DESC_TIPOLIBRO VARCHAR (50) NOT NULL,
);

SELECT * FROM catTIPO_LIBRO
DROP TABLE catTIPO_LIBRO


INSERT INTO catTIPO_LIBRO
VALUES (7001,
		'Literatura y linguisticos');

INSERT INTO catTIPO_LIBRO
VALUES (7002,
		'De viaje');

INSERT INTO catTIPO_LIBRO
VALUES (7003,
		'Biografías');

INSERT INTO catTIPO_LIBRO
VALUES (7004,
		'De referencia o consulta');

INSERT INTO catTIPO_LIBRO
VALUES (7005,
		'Monografía');

INSERT INTO catTIPO_LIBRO
VALUES (7006,
		'Científico')

-- Tipo de Usuario que consulta o renta

CREATE TABLE catCATEGORIA_USUARIO(
	ID_CATUSUARIO INT NOT NULL PRIMARY KEY, 
	DESC_CATUSUARIO VARCHAR (15) NOT NULL,
);

SELECT * FROM catCATEGORIA_USUARIO
DROP TABLE catCATEGORIA_USUARIO


INSERT INTO catCATEGORIA_USUARIO
VALUES (9001,
		'Empleado');

INSERT INTO catCATEGORIA_USUARIO
VALUES (9002,
		'Estudiante');

INSERT INTO catCATEGORIA_USUARIO
VALUES (9003,
		'Visita externa');

-- DONACIÓN 

CREATE TABLE catADQUISICION(
	ID_ADQUISICION INT NOT NULL PRIMARY KEY, 
	DESC_ADQUISICION VARCHAR (50) NOT NULL,
);

INSERT INTO catADQUISICION
VALUES (12001,
		'Compra');

INSERT INTO catADQUISICION
VALUES (12002,
		'Donación');

INSERT INTO catADQUISICION
VALUES (12003,
		'Intercambio');

SELECT * FROM catADQUISICION
DROP TABLE catADQUISICION

-- Stock de Libros

CREATE TABLE catLIBROS_STOCK(
    ID_LIBRO INT NOT NULL PRIMARY KEY,
    CANT_STOCK TINYINT NOT NULL
);



DROP TABLE catLibrosStock

-- Cantidad de prestamos de libro "x"

CREATE TABLE catLIBRO_PRESTAMO(
    ID_LIBRO INT NOT NULL PRIMARY KEY, -- FIXME: No se pudo marcar como foreign key. 
    CANT_PRESTAMO SMALLINT NOT NULL 
);

DROP FULLTEXT CATALOG ftCatalog;
-- ****** AUTORES *********

CREATE TABLE tblAUTOR(
	ID_AUTOR SMALLINT NOT NULL PRIMARY KEY, 
	NOMBRES VARCHAR (80) NOT NULL,
	APELLIDO_PAT VARCHAR (80) NOT NULL,
	APELLIDO_MAT VARCHAR (80) NULL);


INSERT INTO tblAUTOR
VALUES (
	'111',
	'Jsada',
	'Reta',
	'a'
);

EXEC sp_fkeys 'tblAUTOR'


DROP TABLE tblAUTOR
SELECT * FROM tblAUTOR

-- ******** EMPLEADOS ********

CREATE TABLE EMPLEADOS(

);

SELECT * FROM tblEMPLEADOS
DROP TABLE EMPLEADOS


INSERT INTO tblEMPLEADOS
VALUES (0001,
		'Eduardo',
		19,
		'Reta',
		'Nochebuena',
		6001,
		2002,
		'hdiaw@gmail.com',
		83934521);


--**********   TABLA LIBRO   **********


CREATE TABLE tblLIBRO(
	ID_LIBRO SMALLINT NOT NULL PRIMARY KEY, 
	TITULO VARCHAR (80) NOT NULL,
	ID_EDITORIAL INT FOREIGN KEY REFERENCES catEDITORIAL(ID_EDITORIAL),
	PUBLICACION SMALLINT NOT NULL, -- year of publication
	ID_ADQUISICION INT FOREIGN KEY REFERENCES catADQUISICION(ID_ADQUISICION),
	ID_GENERO INT FOREIGN KEY REFERENCES catGENERO(ID_GENERO),
	NUM_PAGINAS SMALLINT NOT NULL,
	EDICION SMALLINT NULL,
	VOLUMEN SMALLINT NULL,
	TOMO SMALLINT NULL,
	ID_IDIOMA INT FOREIGN KEY REFERENCES catIDIOMA(ID_IDIOMA),
	ID_ESTANTE INT FOREIGN KEY REFERENCES catSECCIONES(ID_ESTANTE),
	ID_TIPOLIBRO INT FOREIGN KEY REFERENCES catTIPO_LIBRO(ID_TIPOLIBRO),
);



SELECT * FROM tblLIBRO
DROP TABLE tblLIBRO


DELETE FROM tblLIBRO

DELETE FROM tblLIBRO WHERE ID_LIBRO=2;
DROP TABLE catOBRAS

INSERT INTO tblLIBRO
VALUES (1,
		'Álgebra',
		5007,
		2004,
		12002,
		4004,
		204,
		1,
		1,
		1,
		3001,
		1203,
		7006);


INSERT INTO tblLIBRO
VALUES (2,
		'El principito',
		5002,
		1956,
		12001,
		4006,
		611,
		1,
		3,
		1,
		3005,
		1301,
		7001);




-- ******* EMPLEADOS ********

CREATE TABLE tblEMPLEADOS(
	ID_EMPLEADO SMALLINT NOT NULL PRIMARY KEY,
	NOMBRE VARCHAR (80) NOT NULL,
	EDAD TINYINT NOT NULL,
	APELLIDO_PAT VARCHAR (80) NOT NULL,
	APELLIDO_MAT VARCHAR (80) NOT NULL, 
	ID_TURNOS INT FOREIGN KEY REFERENCES catTURNOS(ID_TURNOS),
	ID_PUESTO INT FOREIGN KEY REFERENCES catPUESTO(ID_PUESTO),
	CORREO VARCHAR(50) NOT NULL,
);

SELECT * FROM tblEMPLEADOS

INSERT INTO tblEMPLEADOS
VALUES (14001,
		'Oskar Yhahiir',
		21,
		'CASTILLO',
		'Sanchez',
		6001,
		2001,
		'reta@gudnait.com');



--******* USUARIOS *********

CREATE TABLE tblUSUARIO(
	ID_USUARIO INT NOT NULL PRIMARY KEY,
	NOMBRE VARCHAR (80) NOT NULL,
	APELLIDO_PAT VARCHAR (80) NOT NULL,
	APELLIDO_MAT VARCHAR (80) NOT NULL, 
	DIRECCION VARCHAR (80) NOT NULL,
	CORREO VARCHAR(50) NOT NULL,
	CODIGO_POSTAL BIGINT NOT NULL,
	TELEFONO BIGINT NOT NULL,
	ID_CATUSUARIO INT FOREIGN KEY REFERENCES catCATEGORIA_USUARIO(ID_CATUSUARIO),
	EDAD TINYINT NOT NULL,
);

INSERT INTO tblUSUARIO
VALUES (
	15001,
	'asdasd',
	'asda',
	'asdasd',
	'adhdoiahdoaishdoiasdiasd',
	'dau@gmail.com',
	67400,
	8123723355,
	9001,
	21
);

SELECT * FROM tblUSUARIO
DROP TABLE tblUSUARIO

-- Donacion

CREATE TABLE tblDONACION(
	ID_DONACION SMALLINT NOT NULL,
	NOMBRE_DONADOR VARCHAR (80) NOT NULL,
	NOMBRE_INSTITUCION VARCHAR (80) NULL,
	ID_LIBRO SMALLINT FOREIGN KEY REFERENCES tblLIBRO(ID_LIBRO),
	CANT_LIBROS SMALLINT NOT NULL,
)

SELECT * FROM tblDONACIONES
DROP TABLE tblDONACIONES

INSERT INTO tblDonacion 
VALUES (
	16001,
	'Eduardo Reta Nochebuena',
	'Facultad de Ciencias Fisico-Matematicas',
	2, --FIXME: Para poder ingresar el ID_LIBRO de la donacion antes tiene que checar cual es.
	50
)

INSERT INTO tblEMPLEADOS
VALUES (
	14002,
	'Eduardo',
	'21',
	'Gaytan',
	'Valadez',
	6002,
	2003,
	'eduardo.retana@uanl.edu.mx'
)

DELETE FROM tblDONACION
UPDATE tblEMPLEADOS 
SET 
SELECT * FROM tblEMPLEADOS
DELETE tblEMPLEADOS WHERE ID_EMPLEADO=17001

-- Prestamos

CREATE TABLE tblPRESTAMO (
	ID_PRESTAMO SMALLINT NOT NULL PRIMARY KEY,
	ID_EMPLEADO SMALLINT FOREIGN KEY REFERENCES tblEMPLEADOS(ID_EMPLEADO),
	ID_USUARIO INT FOREIGN KEY REFERENCES tblUSUARIO(ID_USUARIO),
	ID_LIBRO SMALLINT FOREIGN KEY REFERENCES tblLIBRO(ID_LIBRO),
	FECHA_PRESTAMO VARCHAR(20),
	FECHA_REGRESO VARCHAR(20)
);

DROP TABLE tblPRESTAMOS

INSERT INTO tblPRESTAMO
VALUES (
	17001,
	14001,
	15001,
	2,
	'2020-08-18',
	'2020-08-21'
);

SELECT FECHA_PRESTAMO FROM tblPRESTAMOS WHERE ID_PRESTAMO=17006;
SELECT FECHA_DEVOLUCION FROM tblDEVOLUCION WHERE ID_PRESTAMO=17006;

DELETE FROM tblPRESTAMOS
DROP TABLE tblPRESTAMOS
SELECT * FROM tblPRESTAMOS

CREATE TABLE tblDEVOLUCION(
	ID_DEVOLUCION SMALLINT NOT NULL PRIMARY KEY,
	ID_PRESTAMO SMALLINT FOREIGN KEY REFERENCES tblPRESTAMO(ID_PRESTAMO),
	ID_USUARIO INT FOREIGN KEY REFERENCES tblUSUARIO(ID_USUARIO),
	FECHA_DEVOLUCION VARCHAR(20) NULL ,
	ESTADO VARCHAR(20) NULL -- Pendiente, Entregado
)

INSERT INTO tblDEVOLUCION
VALUES (
	19001,
	17001,
	15001,
	'2020-08-21',
	'ENTREGADO'
)

DELETE FROM tblDEVOLUCION
SELECT * FROM tblDEVOLUCION
DELETE tblDEVOLUCION WHERE ID_PRESTAMO=17028
DROP TABLE tblDEVOLUCION

SELECT

-- Multas

CREATE TABLE tblMULTA (
	ID_MULTA SMALLINT NOT NULL PRIMARY KEY,
	ID_DEVOLUCION SMALLINT FOREIGN KEY REFERENCES tblDEVOLUCION(ID_DEVOLUCION),
	DIAS_RETRASO TINYINT NULL,
	COSTO_MULTA SMALLINT NOT NULL,
	ESTADO VARCHAR(20) NULL
);

DELETE FROM tblMULTA
SELECT * FROM tblMULTA
DROP TABLE tblMULTA
INSERT INTO tblMULTAS 
VALUES (
)


CREATE TABLE tblAUTOR (
	ID_AUTOR SMALLINT NOT NULL PRIMARY KEY,
	NOMBRE VARCHAR (30) NOT NULL,
	APELLIDO_PAT VARCHAR (30) NOT NULL,
	APELLIDO_MAT VARCHAR (30) NULL, --opcional
	DIA_PUBLICACION TINYINT NULL, --opcional
	MES_PUBLICACION TINYINT NULL, --opcional
	AÑO_PUBLICACION SMALLINT NOT NULL,
)

INSERT INTO tblAUTOR
VALUES (
	18002,
	'Oscar',
	'Yair',
	'Castillo',
	18,
	08,
	2008
)

UPDATE tblAUTOR SET NOMBRES = 'Jose' WHERE ID_AUTOR = 111
SELECT * FROM tblAUTOR


SELECT ID_LIBRO FROM tblLIBRO;

SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'tblLIBRO'

ALTER TABLE tblLIBRO ADD prueba varchar(80)
ALTER TABLE tblLIBRO DROP COLUMN prueba

INSERT INTO dbo.tblAUTOR

-- Obtener ultimo valor de tabla
SELECT TOP 1 ID_AUTOR FROM tblAUTOR ORDER BY ID_AUTOR DESC;  




SELECT * FROM catGENERO
SELECT * FROM tblLIBRO

ALTER TABLE tblAUTOR DROP COLUMN pruebas1

INSERT INTO tblAUTOR (ID_AUTOR) VALUES ('18003');

-- Obtener ultima columna
SELECT TOP 1 * FROM tblAUTOR ORDER BY ID_AUTOR DESC
