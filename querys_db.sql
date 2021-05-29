CREATE DATABASE dbBiblioteca
use dbBiblioteca

-- Secciones

CREATE TABLE catSECCIONES(
	ID_ESTANTE SMALLINT NOT NULL PRIMARY KEY, 
	DESC_ESTANTE VARCHAR (35) NOT NULL,
);

DROP TABLE catSECCIONES
Select * FROM catSECCIONES

INSERT INTO catSECCIONES 
VALUES (1101,
		'Estante 1, repisa 1');

INSERT INTO catSECCIONES
VALUES (1102,
		'Estante 1, repisa 2');

INSERT INTO catSECCIONES
VALUES (1103,
		'Estante 1, repisa 3');

INSERT INTO catSECCIONES 
VALUES (1201,
		'Estante 2, repisa 1');

INSERT INTO catSECCIONES 
VALUES (1202,
		'Estante 2, repisa 2');

INSERT INTO catSECCIONES 
VALUES (1203,
		'Estante 2, repisa 3');

INSERT INTO catSECCIONES 
VALUES (1301,
		'Estante 3, repisa 1');

INSERT INTO catSECCIONES 
VALUES (1302,
		'Estante 3, repisa 2');

INSERT INTO catSECCIONES 
VALUES (1303,
		'Estante 3, repisa 3');

INSERT INTO catSECCIONES 
VALUES (1401,
		'Estante 4, repisa 1');

INSERT INTO catSECCIONES 
VALUES (1402,
		'Estante 4, repisa 2');

INSERT INTO catSECCIONES 
VALUES (1403,
		'Estante 4, repisa 3');

INSERT INTO catSECCIONES 
VALUES (1501,
		'Estante 5, repisa 1');

INSERT INTO catSECCIONES 
VALUES (1502,
		'Estante 5, repisa 2');

INSERT INTO catSECCIONES 
VALUES (1503,
		'Estante 5, repisa 3');

INSERT INTO catSECCIONES 
VALUES (1601,
		'Estante 6, repisa 1');

INSERT INTO catSECCIONES 
VALUES (1602,
		'Estante 5, repisa 2');

INSERT INTO catSECCIONES 
VALUES (1603,
		'Estante 5, repisa 3');

INSERT INTO catSECCIONES 
VALUES (1701,
		'Estante 7, repisa 1');

INSERT INTO catSECCIONES 
VALUES (1702,
		'Estante 7, repisa 2');

INSERT INTO catSECCIONES 
VALUES (1703,
		'Estante 7, repisa 3');




-- PUESTOS DE EMPLEADOS

SELECT * FROM catPUESTO

CREATE TABLE catPUESTO(
	ID_PUESTO SMALLINT NOT NULL PRIMARY KEY, 
	DESC_PUESTO VARCHAR (70) NOT NULL,
);

DROP TABLE catPUESTO
SELECT * FROM catPUESTO

INSERT INTO catPUESTO
VALUES (2001,
		'Jefe de servicios de sala y prestamo');

INSERT INTO catPUESTO
VALUES (2002,
		'Bibliotecario');

INSERT INTO catPUESTO
VALUES (2003,
		'Soporte Técnico');

INSERT INTO catPUESTO
VALUES (2004,
		'Director de Biblioteca');

INSERT INTO catPUESTO
VALUES (2005,
		'Subdirector de Biblioteca');



INSERT INTO catPUESTO
VALUES (2006,
		'Administrador de Biblioteca');

INSERT INTO catPUESTO
VALUES (2007,
		'Jefe de procesos técnicos');

INSERT INTO catPUESTO
VALUES (2008,
		'Jefe de servicios al público');

INSERT INTO catPUESTO
VALUES (2009,
		'Coordinador de servicios informáticos');

INSERT INTO catPUESTO
VALUES (2010,
		'Coordinador de desarrollo de colecciones');

INSERT INTO catPUESTO
VALUES (2011,
		'Diseñador gráfico web');

INSERT INTO catPUESTO
VALUES (2012,
		'Administrador de contenidos y servicios digitales');


INSERT INTO catPUESTO
VALUES (2013,
		'Catalogador');

INSERT INTO catPUESTO
VALUES (2014,
		'Asistente de catalogación');

INSERT INTO catPUESTO
VALUES (2015,
		'Referencista');

INSERT INTO catPUESTO
VALUES (2016,
		'Auxiliar de administración');

INSERT INTO catPUESTO
VALUES (2017,
		'Auxiliar de servicios al público');

INSERT INTO catPUESTO
VALUES (2018,
		'Auxiliar de servicios informáticos');

INSERT INTO catPUESTO
VALUES (2019,
		'Asistente de dirección de biblioteca');

		
-- IDIOMAS

CREATE TABLE catIDIOMA(
	ID_IDIOMA SMALLINT PRIMARY KEY, 
	DESC_IDIOMA VARCHAR (20) NOT NULL,
);

DROP TABLE catIDIOMA

SELECT * FROM catIDIOMA

INSERT INTO catIDIOMA
VALUES (3001,
		'Español');

INSERT INTO catIDIOMA
VALUES (3002,
		'Ingles');

INSERT INTO catIDIOMA
VALUES (3003,
		'Francés');

INSERT INTO catIDIOMA
VALUES (3004,
		'Alemán');

INSERT INTO catIDIOMA
VALUES (3005,
		'Italiano');



INSERT INTO catIDIOMA
VALUES (3006,
		'Portugués');

INSERT INTO catIDIOMA
VALUES (3007,
		'Catalán');
		
INSERT INTO catIDIOMA
VALUES (3008,
		'Ruso');

INSERT INTO catIDIOMA
VALUES (3009,
		'Croata');

INSERT INTO catIDIOMA
VALUES (3010,
		'Yugoslavo');

INSERT INTO catIDIOMA
VALUES (3010,
		'Polaco');

INSERT INTO catIDIOMA
VALUES (3011,
		'Turco');

INSERT INTO catIDIOMA
VALUES (3012,
		'Chino');

INSERT INTO catIDIOMA
VALUES (3013,
		'Japonés');

INSERT INTO catIDIOMA
VALUES (3014,
		'Romaní');

INSERT INTO catIDIOMA
VALUES (3015,
		'Coreano');

INSERT INTO catIDIOMA
VALUES (3016,
		'Hindi');

INSERT INTO catIDIOMA
VALUES (3017,
		'Árabe');

INSERT INTO catIDIOMA
VALUES (3018,
		'Totonaco');

INSERT INTO catIDIOMA
VALUES (3019,
		'Latín');

INSERT INTO catIDIOMA
VALUES (3020,
		'Griego');

INSERT INTO catIDIOMA
VALUES (3021,
		'Arameo');

INSERT INTO catIDIOMA
VALUES (3022,
		'Egipcio');

INSERT INTO catIDIOMA
VALUES (3023,
		'Hebreo');



ROP TABLE catLIBRO_AUTOR


-- GENERO

CREATE TABLE catGENERO(
	ID_GENERO SMALLINT NOT NULL PRIMARY KEY, 
	DESC_GENERO VARCHAR (50) NOT NULL,
);

DROP TABLE catGENERO

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



INSERT INTO catGENERO
VALUES (4008,
		'Paranormal');

INSERT INTO catGENERO
VALUES (4009,
		'Romántico');

INSERT INTO catGENERO
VALUES (4010,
		'Terror');

INSERT INTO catGENERO
VALUES (4011,
		'Misterio');

INSERT INTO catGENERO
VALUES (4012,
		'Humor');

INSERT INTO catGENERO
VALUES (4013,
		'Poesía');

INSERT INTO catGENERO
VALUES (4014,
		'Mitología');

INSERT INTO catGENERO
VALUES (4015,
		'Teatro');

INSERT INTO catGENERO
VALUES (4016,
		'Cuento');
		
-- CASAS EDITORIALES

CREATE TABLE catEDITORIAL(
	ID_EDITORIAL SMALLINT NOT NULL PRIMARY KEY, 
	DESC_EDITORIAL VARCHAR (50) NOT NULL,
);

DROP TABLE catEDITORIAL
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



INSERT INTO catEDITORIAL
VALUES (5008,
		'Editorial Acantilado');

INSERT INTO catEDITORIAL
VALUES (5009,
		'Editorial Kal');

INSERT INTO catEDITORIAL
VALUES (5010,
		'Editorial Alba');

INSERT INTO catEDITORIAL
VALUES (5011,
		'Editorial Alfaguara');

INSERT INTO catEDITORIAL
VALUES (5012,
		'Editorial Alianza');

INSERT INTO catEDITORIAL
VALUES (5013,
		'Editorial Almadia');

INSERT INTO catEDITORIAL
VALUES (5014,
		'Editorial Anagrama');

INSERT INTO catEDITORIAL
VALUES (5015,
		'Editorial Alpha Decay');

INSERT INTO catEDITORIAL
VALUES (5016,
		'Editorial Ariel');

INSERT INTO catEDITORIAL
VALUES (5017,
		'Editorial Atalanta');

INSERT INTO catEDITORIAL
VALUES (5018,
		'Editorial Caja Negra');

INSERT INTO catEDITORIAL
VALUES (5019,
		'Editorial Gallo Nero');

INSERT INTO catEDITORIAL
VALUES (5020,
		'Editorial Critica');-- TURNOS / HORARIOS DE TRABAJO

CREATE TABLE catTURNOS(
	ID_TURNOS SMALLINT NOT NULL PRIMARY KEY, 
	DESC_TURNO VARCHAR (35) NOT NULL,
);

SELECT * FROM catTURNOS
DROP TABLE catTURNOS

INSERT INTO catTURNOS
VALUES (6001,
		'Matutino');

INSERT INTO catTURNOS
VALUES (6002,
		'Vespertino');

INSERT INTO catTURNOS
VALUES (6003,
		'Nocturno');



-- Tipo de Libro

CREATE TABLE catTIPO_LIBRO(
	ID_TIPOLIBRO SMALLINT NOT NULL PRIMARY KEY, 
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
		'Científico');
	
INSERT INTO catTIPO_LIBRO
VALUES (7007,
		'Libro de texto');

INSERT INTO catTIPO_LIBRO
VALUES (7008,
		'Libro de gran formato');

INSERT INTO catTIPO_LIBRO
VALUES (7009,
		'Libro recreativo');

INSERT INTO catTIPO_LIBRO
VALUES (7010,
		'Libro poetico');

INSERT INTO catTIPO_LIBRO
VALUES (7011,
		'Libro juvenil');

INSERT INTO catTIPO_LIBRO
VALUES (7012,
		'Libro infantil');
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


-- ****** AUTORES *********

CREATE TABLE tblAUTOR(
	ID_AUTOR SMALLINT NOT NULL PRIMARY KEY, 
	NOMBRES VARCHAR (80) NOT NULL,
	APELLIDO_PAT VARCHAR (80) NOT NULL,
	APELLIDO_MAT VARCHAR (80) NULL);

DROP TABLE tblAUTOR
INSERT INTO tblAUTOR
VALUES (
	'111',
	'Gabriel',
	'Garcia',
	'Marquez'
);

EXEC sp_fkeys 'tblAUTOR'



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
	ID_AUTOR SMALLINT FOREIGN KEY REFERENCES tblAUTOR(ID_AUTOR),
	ID_EDITORIAL SMALLINT FOREIGN KEY REFERENCES catEDITORIAL(ID_EDITORIAL),
	PUBLICACION SMALLINT NOT NULL, -- year of publication
	ID_ADQUISICION INT FOREIGN KEY REFERENCES catADQUISICION(ID_ADQUISICION),
	ID_GENERO SMALLINT FOREIGN KEY REFERENCES catGENERO(ID_GENERO),
	NUM_PAGINAS SMALLINT NOT NULL,
	EDICION SMALLINT NULL,
	VOLUMEN SMALLINT NULL,
	TOMO SMALLINT NULL,
	ID_IDIOMA SMALLINT FOREIGN KEY REFERENCES catIDIOMA(ID_IDIOMA),
	ID_ESTANTE SMALLINT FOREIGN KEY REFERENCES catSECCIONES(ID_ESTANTE),
	ID_TIPOLIBRO SMALLINT FOREIGN KEY REFERENCES catTIPO_LIBRO(ID_TIPOLIBRO),
);

INSERT INTO 



SELECT * FROM tblLIBRO
DROP TABLE tblLIBRO


DELETE FROM tblLIBRO

DELETE FROM tblLIBRO WHERE ID_LIBRO=2;
DROP TABLE catOBRAS

INSERT INTO tblLIBRO
VALUES (1,
		'ALGEBRA',
		18001,
		5007,
		2004,
		12002,
		4004,
		204,
		1,
		2,
		2,
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
	ID_TURNOS SMALLINT FOREIGN KEY REFERENCES catTURNOS(ID_TURNOS),
	ID_PUESTO SMALLINT FOREIGN KEY REFERENCES catPUESTO(ID_PUESTO),
	CORREO VARCHAR(50) NOT NULL,
);

SELECT * FROM tblEMPLEADOS



INSERT INTO tblEMPLEADOS
VALUES (14001,
		'Oscar De Jesus',
		21,
		'Castillo',
		'Martinez',
		6001,
		2001,
		'ocjcm@outlook.com');

INSERT INTO tblEMPLEADOS
VALUES (14021, 'Cesar', 28, 'Gonzalez', 'Castillo', 6001, 2014, 'cesarg@gmail.com'),
	   (14022, 'Juan', 45, 'Mata', 'Rodriguez', 6002, 2018, 'juanmat@gmail.com'),
	   (14023, 'Hidalgo', 65, 'Venez', 'Riberto', 6003, 2005, 'hidalven@gmail.com'),
	   (14024, 'Sara', 62, 'Reta', 'Tovar', 6002, 2008, 'sar_tovar@gmal.com'),
	   (14025, 'Maria', 20, 'Castillo', 'Gonzalez', 6001, 2016, 'ma_gz@gmail.com')


INSERT INTO tblEMPLEADOS
VALUES 
	(
	14002,
	'José de Jesús',
	24,
	'Pérez',
	'Sánchez',
	6003,
	2004,
	'jose.jesuspesan@uanl.edu.mx'
	),
	(
	14003,
	'Eduardo Alonso',
	21,
	'Gaytan',
	'Valadez',
	6001,
	2011,
	'ed.gaval12@gmail.com'
	),
	(
	14004,
	'Oscar Yair',
	19,
	'Castle',
	'Gutiérrez',
	6001,
	2019,
	'os.yahiiir@hotmail.com'
	),
	(
	14005,
	'Roxanna',
	15,
	'García',
	'Goodnight',
	6002,
	2001,
	'roxx_girl44@uanl.edu.mx'
	),
	(
	14006,
	'Alejandra',
	31,
	'Triana',
	'Santa-Cruz',
	6003,
	2013,
	'alejandria.sa21@gmail.com'
	),
	(
	14007,
	'Diego',
	21,
	'Martínez',
	'González',
	6001,
	2003,
	'diego.mart0000@gmail.com'
	),
	(
	14008,
	'Miguel Ángel',
	41,
	'Miranda',
	'Rodríguez',
	6002,
	2016,
	'mike.miranda21221@hotmail.com'
	),
	(
	14009,
	'Ebry Aldair',
	83,
	'Mendez',
	'Scott',
	6001,
	2002,
	'ebraindu_loco@uanl.edu.mx'
	),
	(
	14010,
	'Erick',
	56,
	'Esparza',
	'Hernández',
	6002,
	2014,
	'erick.hernandez@hotmail.com'
	),
	(
	14011,
	'Jaime',
	31,
	'Escutia',
	'Roemer',
	6001,
	2019,
	'esc.jaimer13@gmail.com'
	),
	(
	14012,
	'Alex',
	41,
	'Syntex',
	'Domeli',
	6002,
	2011,
	'alex_bajistarock@uanl.edu.mx'
	),
	(
	14013,
	'Leo',
	62,
	'Dan',
	'Olivares',
	6001,
	2015,
	'leo.dan97@gmail.com'
	),
	(
	14014,
	'Sofía',
	73,
	'Gómez',
	'Ríos',
	6003,
	2003,
	'sofia_gori@hotmail.com'
	),
	(
	14015,
	'Enrique',
	42,
	'Tovar',
	'Quezada',
	6001,
	2017,
	'riquiko.tobarXD@uanl.edu.mx'
	);


INSERT INTO tblEMPLEADOS
VALUES 
	(
	14016,
	'Manuel',
	24,
	'Calderon',
	'Sánchez',
	6002,
	2011,
	'manuel_calderonismo2006@uanl.edu.mx'
	),
	(
	14017,
	'Homero',
	18,
	'Germain',
	'Sosa',
	6001,
	2017,
	'Homero.sosa@gmail.com'
	),
	(
	14018,
	'Carlos',
	27,
	'Gómez',
	'García',
	6002,
	2001,
	'karloz.gomez@hotmail.com'
	),
	(
	14019,
	'Federico',
	25,
	'Franco',
	'Cervantes',
	6001,
	2010,
	'fedefrank_cerv@uanl.edu.mx'
	),
	(
	14020,
	'Nicolás',
	61,
	'Mora',
	'Salazar',
	6001,
	2018,
	'nicolas_salamor313@gmail.com'
	);


DROP TABLE tblEMPLEADOS

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
	--EDAD TINYINT NOT NULL,
);

INSERT INTO tblUSUARIO
VALUES (
	15001,
	'Jesus',
	'Vazquez',
	'Martinez',
	'Calle Fresno Colonia Cumbres 5to Sector',
	'dau@gmail.com',
	67400,
	8123723355,
	9001
);

INSERT INTO tblUSUARIO 
VALUES (15016, 'Belinda', 'Perez', 'MacCullagh', 'Calle Diamante Colonia Falda de la Montana')
	   (15017, 'Jesus', 'Torres', 'Torres', 'Calle Francisco Bocanegra Colonia Centro', 'tortor@outlook.com', 73043, 8346508317, 9001),
	   (15018, 'Debanhi', 'Valdez', 'Olague', 'Calle Jardines de Barcelona Colonia Mitras', 'debval@gmail.com', 73490, 83649107398, 9002),
	   (15019, 'Vanessa', 'Arrambide', 'Torres', 'Calle Santa Marta Colonia Aguila de Cumbres', 'vane_torr@gmail.com', 75209, 7364518399, 9003),
	   (15020, 'Florinda', 'Meza', 'Belmares', 'Calle Francisco I. Madero Colonia Centro', 'flor_bel@gmail.com', 89640, 8107423743, 9002)


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

DROP TABLE tblDONACION

INSERT INTO tblDonacion 
VALUES (
	16001,
	'Eduardo Reta Nochebuena',
	'Facultad de Ciencias Fisico-Matematicas',
	1, --FIXME: Para poder ingresar el ID_LIBRO de la donacion antes tiene que checar cual es.
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

DROP TABLE tblEMPLEADOS
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

DROP TABLE tblPRESTAMO

INSERT INTO tblPRESTAMO
VALUES (
	17001,
	14001,
	15001,
	1,
	'2020-08-18',
	'2020-08-21'
);

SELECT FECHA_PRESTAMO FROM tblPRESTAMOS WHERE ID_PRESTAMO=17006;
SELECT FECHA_DEVOLUCION FROM tblDEVOLUCION WHERE ID_PRESTAMO=17006;



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
	--DIA_PUBLICACION TINYINT NULL, --opcional
	--MES_PUBLICACION TINYINT NULL, --opcional
	--AÑO_PUBLICACION SMALLINT NOT NULL,
)

DROP TABLE tblAUTOR

INSERT INTO tblAUTOR
VALUES (
	18001,
	'Sergio',
	'Martinez',
	'Aregui'
)

INSERT INTO tblAUTOR(
	ID_AUTOR, NOMBRES, APELLIDO_PAT, APELLIDO_MAT
)
VALUES (18002, 'Jesus', 'Humberto', 'Vazquez'), (18003, 'Sebastian', 'Cavazos', 'Garza'),
		(18004, 'Gerardo', 'Martinez', 'Cruz'), (18005, 'Adrian', 'Vazquez', 'Sergui'),
		(18006, 'Miguel', 'Angel', 'Mancera'), (18007, 'Daniel', 'Cavazos', 'Manrique'),
		(18008, 'Jose', 'Huerta', 'Victoria'), (18009, 'Julio', 'Castillo', 'Sanchez'),
		(18010, 'Angel', 'Flores', 'Trejo'), (18011, 'Clara', 'Carrazo', 'Sepa'),
		(18012, 'Samuel', 'Reta', 'Gutierrez'), (18013, 'Benito', 'Juarez', 'Espinoza'),
		(18014, 'Eduardo', 'Martinez', 'Hernandez'), (18015, 'Fernando', 'Cervantes', 'Saavedra')


	--MES_PUBLICACION TINYINT NULL, --opcional
	--AÑO_PUBLICACION SMALLINT NOT NULL,

INSERT INTO tblAUTOR (
	ID_AUTOR, NOMBRES, APELLIDO_PAT, APELLIDO_MAT
)
VALUES 
	(
	18016,
	'Ricardo',
	'Monreal',
	'Garza'
	),
	(
	18017,
	'Eduardo',
	'Valdez',
	'Rivero'
	),
	(
	18018,
	'Joaquín',
	'Castillo',
	'Martínez'
	),
	(
	18019,
	'Fernando',
	'González',
	'Sullivan'
	),
	(
	18020,
	'Aliber',
	'Montoya',
	'Sánchez'
	),
	(
	18021,
	'Lucas',
	'Sáenz',
	'Lozano'
	),
	(
	18022,
	'Thomas',
	'Shelby',
	'Zegna'
	),
	(
	18023,
	'Ermenegildo',
	'Gaitan',
	'Villanueva'
	),
	(
	18024,
	'Cayetano',
	'Olivares',
	'Méndez'
	),
	(
	18025,
	'Venustiana',
	'Villarreal',
	'Bach'
	),
	(
	18026,
	'Norma',
	'Higareda',
	'Solorzano'
	),
	(
	18027,
	'Ximena',
	'Nochebuena',
	'Reta'
	),
	(
	18028,
	'Sofía',
	'Obrador',
	'Licari'
	),
	(
	18029,
	'Andrés',
	'Méndez',
	'Miranda'
	),
	(
	18030,
	'Rogelio',
	'Segura',
	'Scott'
	)
	

SELECT * FROM tblAUTOR

DROP TABLE tblAUTOR

INSERT INTO tblAUTOR
VALUES (
	18001,
	'Sergio',
	'Martinez',
	'Aregui'
)

INSERT INTO tblAUTOR(
	ID_AUTOR
)


DELETE FROM tblAUTOR
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
