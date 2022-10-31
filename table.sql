-- Creación de tabla --

CREATE TABLE peliculas (
    NombrePelicula VARCHAR (20) PRIMARY KEY,
    Genero VARCHAR (20) NOT NULL,
    Director VARCHAR (20),
    AnoEstreno VARCHAR(4)
);

-- Algunos inserts --

INSERT INTO peliculas VALUES ('Dune','Ciencia-ficcion','Edwards','1984');
INSERT INTO peliculas VALUES ('Los Idiotas','Drama','Von Trier','1999');
INSERT INTO peliculas VALUES ('Kramer vs Kramer','Drama','Smith','1978');
INSERT INTO peliculas VALUES ('Mision Imposible','Ciencia-ficcion','Johnson','1998');
INSERT INTO peliculas VALUES ('Mi nombre es Joe','Drama','Loach','1995');
INSERT INTO peliculas VALUES ('Rompiendo las olas','Drama','Von Trier','1997');
INSERT INTO peliculas VALUES ('Los Otros','Suspense','Amenabar','2001');
