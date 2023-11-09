class Stagelayout:
    def __init__(
        self,
        id_stage,
        titre,
        description,
        specialite,
        localisation,
        siteSource,
        URL_stage,
        employeur,
        date_publication,
    ):
        self.id_stage = id_stage
        self.titre = titre
        self.description = description
        self.specialite = specialite
        self.localisation = localisation
        self.siteSource = siteSource
        self.URL_stage = URL_stage
        self.employeur = employeur
        self.date_publication = date_publication

    def __list__(self):
        #        s1 = "Ce stage peut être brèvement décrit comme étant {} ".format(
        #            self.description
        #        )
        #        return s1
        stage = [
            self.id_stage,
            self.titre,
            self.description,
            self.specialite,
            self.localisation,
            self.siteSource,
            self.URL_stage,
            self.employeur,
            self.date_publication,
        ]
        return stage
