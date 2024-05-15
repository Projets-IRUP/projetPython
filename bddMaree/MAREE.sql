
CREATE DATABASE `bdd_maree` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE port(
   id_port INT AUTO_INCREMENT,
   nom VARCHAR(30)  NOT NULL,
   url VARCHAR(50)  NOT NULL COMMENT 'Url pour météo marine',
   PRIMARY KEY(id_port)
);

CREATE TABLE maree(
   id_maree INT AUTO_INCREMENT,
   date_heure DATETIME NOT NULL,
   hauteur DECIMAL(4,2)   NOT NULL COMMENT 'En mètre',
   maree_type BOOLEAN NOT NULL COMMENT '0 = basse 1 = haute',
   id_port INT NOT NULL,
   PRIMARY KEY(id_maree),
   FOREIGN KEY(id_port) REFERENCES port(id_port)
);

INSERT INTO `bdd_maree`.`port`
(
`nom`,
`url`)
VALUES
(
'port-maria', 'port-maria-999'),('port-haliguen','port-haliguen-1001');
