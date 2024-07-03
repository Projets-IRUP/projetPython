
CREATE DATABASE `bdd_maree` ;

USE bdd_maree;

CREATE TABLE port(
   id_port INT AUTO_INCREMENT,
   nom VARCHAR(50)  NOT NULL,
   url VARCHAR(50)  NOT NULL COMMENT 'Complement url pour météo marine',
   latitude DECIMAL(9,6)   NOT NULL,
   longitude DECIMAL(9,6)   NOT NULL,
   PRIMARY KEY(id_port)
);

CREATE TABLE maree(
   id_maree INT AUTO_INCREMENT,
   date_heure DATETIME NOT NULL,
   hauteur DECIMAL(4,2)   NOT NULL COMMENT 'En mètre',
   maree_type BOOLEAN NOT NULL COMMENT '0 = basse 1 = haute',
   coefficient tinyint, 
   id_port INT NOT NULL,
   PRIMARY KEY(id_maree),
   FOREIGN KEY(id_port) REFERENCES port(id_port)
);

INSERT INTO port (nom,url,latitude,longitude)
VALUES
(
'port-maria', 'port-maria-999',47.4781,-3.1234);
INSERT INTO port (nom,url,latitude,longitude)
VALUES
(
'Le Palais', 'belle-ile-le-palais-1000',47.34720678928164,-3.153561329334396); 
