class Siterecherche:
    def __init__(self, nom, url, methoderecherche):
        self.nom = nom
        self.url = url
        self.methoderecherche = methoderecherche

    def __str__(self):
        return "Ce stage peut être brèvement décrit comme étant {} et est situé dans la zone de {}. Vous pourrez contacter l'employeur via le contact {}".format(
            self.description, self.localisation, self.employeurContact
        )
