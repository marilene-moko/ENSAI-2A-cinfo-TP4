class Stage:
    def __init__(self,id_stage,titre,description,specialite,localisation,siteSource,employeurContact):
        self.id_stage=id_stage
        self.titre=titre
        self.description=description
        self.specialite=specialite
        self.localisation=localisation
        self.siteSource=siteSource
        self.employeurContact=employeurContact
    
    def __str__(self):
        return "Ce stage peut être brèvement décrit comme étant {} et est situé dans la zone de {}. Vous pourrez contacter l'employeur via le contact {}".format(self.description,self.localisation,self.employeurContact)

    def recuperer_contact(self):
          
