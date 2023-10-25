<<<<<<< HEAD
class Siterecherche:
    def __init__(self, nom, url, methoderecherche):
        self.nom = nom
        self.url = url
        self.methoderecherche = methoderecherche

    def __str__(self):
        return "Ce stage peut être brèvement décrit comme étant {} et est situé dans la zone de {}. Vous pourrez contacter l'employeur via le contact {}".format(
            self.description, self.localisation, self.employeurContact
        )
=======
class SiteRecherche:
    def __init__(
        self,
        nom, 
        url, 
        ):

        self.nom = nom
        self.url = url

    def methodeRecherche(self):

    def lancerRechercheSurSite(self):
>>>>>>> 00fb7d363678e41e95ea81d0f52cce835bccf59f
