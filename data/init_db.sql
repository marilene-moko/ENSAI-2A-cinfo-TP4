DROP TABLE "Projet_Info".stage ;
DROP TABLE "Projet_Info".page_visitee ;
DROP TABLE "Projet_Info".voeu;
DROP TABLE "Projet_Info".recommander ;
DROP TABLE "Projet_Info".personne;
DROP SCHEMA "Projet_Info";

CREATE SCHEMA "Projet_Info" AUTHORIZATION id2241;

CREATE TABLE "Projet_Info".personne (
    identifiant_personne SERIAL4 NOT NULL,
    nom text NOT NULL,
    prenom text NOT NULL,
    adresse_mail VARCHAR(255) PRIMARY KEY,
    mot_de_passe VARCHAR(255) NOT NULL,
    statut text NOT NULL
);

-- Table Recommander
CREATE TABLE "Projet_Info".recommander (
    adresse_mail_recommandant VARCHAR(255) NOT NULL,
    adresse_mail_recommandee VARCHAR(255) NOT NULL,
    date DATE,
    PRIMARY KEY (adresse_mail_recommandant, adresse_mail_recommandee),
    FOREIGN KEY (adresse_mail_recommandant) REFERENCES "Projet_Info".personne(adresse_mail),
    FOREIGN KEY (adresse_mail_recommandee) REFERENCES "Projet_Info".personne(adresse_mail)
);

-- Table Voeu
CREATE TABLE "Projet_Info".voeu (
    identifiant_stage_int SERIAL4 PRIMARY key,
    identifiant_stage text NOT Null,
    Categorie text,
    Intitule text,
    Ville text,
    Entreprise VARCHAR(255),
    adresse_mail VARCHAR(255) NOT NULL,
    FOREIGN KEY (adresse_mail) REFERENCES "Projet_Info".personne(adresse_mail)
);

-- Table Page_visitee
CREATE TABLE "Projet_Info".page_visitee (
    Identifiant_page SERIAL4 PRIMARY KEY,
    date_visite DATE,
    URL_page text,
    adresse_mail VARCHAR(255) NOT NULL,
    FOREIGN KEY (adresse_mail) REFERENCES "Projet_Info".personne(adresse_mail)
);

-- Table Stage
CREATE TABLE "Projet_Info".stage (
    identifiant_stage SERIAL4 PRIMARY KEY,
    URL_stage VARCHAR(255),
    Categorie text,
    Intitule text,
    Ville text,
    Poste text,
    Entreprise VARCHAR(255),²
    Date_publication date,
    Description_stage text,
    adresse_mail_sauvegardee VARCHAR(255),
    adresse_mail_ajout VARCHAR(255),
    adresse_mail_modif VARCHAR(255),
    FOREIGN KEY (adresse_mail_sauvegardee) REFERENCES "Projet_Info".personne(adresse_mail),
    FOREIGN KEY (adresse_mail_ajout) REFERENCES "Projet_Info".personne(adresse_mail),
    FOREIGN KEY (adresse_mail_modif) REFERENCES "Projet_Info".personne(adresse_mail)
);

INSERT INTO "Projet_Info".personne(nom, prenom, adresse_mail, mot_de_passe, statut) VALUES
('Mathieu','Maude','maude.mathieu@gmail.com','MaUdE123456','administrateur'),
('Mounier','Clément','clement.mounier@gmail.com','ClEmEnT987654321','administrateur'),
('Heidsieck', 'Suzanne','suzanne.heidsieck@gmail.com','Susudu35','administrateur'),
('Kougoum Moko Mani','Marilene','marilene.kougoum-moko-mani@gmail.com','RiRidu35000','administrateur'),
('Boubet','Sophie','sophie.boubet@gmail.com','SoPhIe35','administrateur'),
('Bouzeria','Abdel','abdel.bouzeria@gmail.com','Abdel98765432100','professeur'),
('Riviere','Leana','leana.riviere@gmail.com','JadoreLH2O','professeur'),
('Zitoun','Sarah','sarah.zitoun@gmail.com','SAsaSAsa94','professeur'),
('Defour','Vincent','vincent.defour@gmail.com','CupCake35','professeur'),
('Funaer','Catherine','catherine.funaer@gmail.com','CHaCHabada93','professeur'),
('Dupont','Kevin','kevin.dupont@gmail.com','Kev35','eleve'),
('Dupont', 'Nathalie', 'nathalie.dupont@gmail.com','Jdetestelamusique35','eleve'),
('Zaza','Jacob','jacob.zaza@gmail.com','1235Jac','eleve'),
('Elkarif','Abdelraouf','abdelraouf.elkarif@gmail.com','Karirif35','eleve'),
('Carofil','Mathieu','mathieu.carofil@gmail.com','JusteDance75','eleve'),
('Gewoncik','Zuzana','zuzana.gewoncik@gmail.com','Gege75','eleve');
('Visiteur','Visiteur','Visiteur','58a49412f5e6cacc84ebd0caa60d0ba55814d7e10b3c43ed97fc380cb1acf016','visiteur')