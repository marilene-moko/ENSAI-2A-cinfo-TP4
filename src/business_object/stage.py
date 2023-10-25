class Stage:
    def __init__(
        self,
        ID_stage,
        titre, 
        description, 
        specialite, 
        localisation,
        siteSource,
        employeurContact
        ):

        self.ID_stage = ID_stage
        self.titre = titre
        self.description = description
        self.specialite = specialite
        self.localisation = localisation
        self.siteSource = siteSource
        self.employeurContact = employeurContact

        

    def recupererContact(self):

