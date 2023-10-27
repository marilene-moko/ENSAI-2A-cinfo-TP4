DROP TABLE "Projet_Info".stage ;
DROP TABLE "Projet_Info".page_visitee ;
DROP TABLE "Projet_Info".voeu;
DROP TABLE "Projet_Info".recommander ;
DROP TABLE "Projet_Info".personne;
DROP SCHEMA "Projet_Info";

CREATE SCHEMA "Projet_Info" AUTHORIZATION id2241;

CREATE TABLE "Projet_Info".personne (
    identifiant_personne SERIAL4 PRIMARY KEY,
    nom text NOT NULL,
    prenom text NOT NULL,
    adresse_mail VARCHAR(255) NOT NULL,
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
    identifiant_voeu SERIAL4 PRIMARY KEY,
    URL_voeu VARCHAR(255),
    Categorie text,
    Intitule text,
    Ville text,
    Poste text,
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
    Entreprise VARCHAR(255),
    Date_publication date,
    Description_stage text,
    adresse_mail_sauvegardee VARCHAR(255),
    adresse_mail_ajout VARCHAR(255),
    adresse_mail_modif VARCHAR(255),
    FOREIGN KEY (adresse_mail_sauvegardee) REFERENCES "Projet_Info".personne(adresse_mail),
    FOREIGN KEY (adresse_mail_ajout) REFERENCES "Projet_Info".personne(adresse_mail),
    FOREIGN KEY (adresse_mail_modif) REFERENCES "Projet_Info".personne(adresse_mail)
);
