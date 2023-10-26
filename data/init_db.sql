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
    identifiant_personne_recommandant int4,
    identifiant_personne_recommandee int4,
    date DATE,
    PRIMARY KEY (identifiant_personne_recommandant, identifiant_personne_recommandee),
    FOREIGN KEY (identifiant_personne_recommandant) REFERENCES "Projet_Info".personne(identifiant_personne),
    FOREIGN KEY (identifiant_personne_recommandee) REFERENCES "Projet_Info".personne(identifiant_personne)
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
    identifiant_personne int4,
    FOREIGN KEY (identifiant_personne) REFERENCES "Projet_Info".personne(identifiant_personne)
);

-- Table Page_visitee
CREATE TABLE "Projet_Info".page_visitee (
    Identifiant_page SERIAL4 PRIMARY KEY,
    date_visite DATE,
    URL_page text,
    identifiant_personne int4,
    FOREIGN KEY (identifiant_personne) REFERENCES "Projet_Info".personne(identifiant_personne)
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
    identifiant_personne_sauvegarde int4,
    identifiant_personne_ajout int4,
    identifiant_modif int4,
    FOREIGN KEY (identifiant_personne_sauvegarde) REFERENCES "Projet_Info".personne(identifiant_personne),
    FOREIGN KEY (identifiant_personne_ajout) REFERENCES "Projet_Info".personne(identifiant_personne),
    FOREIGN KEY (identifiant_modif) REFERENCES "Projet_Info".personne(identifiant_personne)
);
