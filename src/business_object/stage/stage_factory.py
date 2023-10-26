from src.business_object.stage.stage_layout import Stagelayout
from utils.singleton import Singleton


class stageFactory(metaclass=Singleton):
    def instantiate_stage(
        id_stage: str = None,
        titre: str = None,
        description: str = None,
        specialite: str = None,
        localisation: str = None,
        siteSource: str = None,
        URL_stage: str = None,
        employeur: str = None,
        date_publication: str = None,
    ) -> Stagelayout:
        stage = None

        if specialite is not None or localisation is not None:
            stage = Stagelayout(
                id_stage=id_stage,
                titre=titre,
                description=description,
                specialite=specialite,
                localisation=localisation,
                siteSource=siteSource,
                URL_stage=URL_stage,
                employeur=employeur,
                date_publication=date_publication,
            )

        return stage
