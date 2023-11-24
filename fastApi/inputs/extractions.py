from geopy.geocoders import Nominatim
import sys
from pathlib import Path
from loguru import logger

sys.path.append(Path(__file__).parent.parent.joinpath('models').__str__())

from models.model_pavlov_all_data.model import pavlov_all
from models.ner.model import nner

geolocator = Nominatim(user_agent="promobot_k_team")

def themeExtraction(text):
    """
    Функция по вычленению темы из поднанного текста

    моделью pavlov_all
    """
    return pavlov_all.predict(text)

def nerExtraction(text):
    markup = nner(text)

    text_spans = markup.spans

    print(text_spans)

    if len(text_spans) == 0:
        return ["В тексте именованные сущности не обнаружены"]
    
    ners = []
    for span in text_spans:
        ners.append(
            {
                "token": text[span.start:span.stop],
                "named_entity": span.type
            }
        )
    return ners

def locExtraction(ners):
    logger.debug(ners)

    locs = []
    
    # Отбраковка багов
    if type(ners) == type(list()):

        # Если нера нет
        if type(ners[0]) == type('s'): return locs
    
        for ner in ners:
            if ner["named_entity"] == "LOC":
                locs.append(ner["token"])
    return locs

def coordsExtraction(loc):
    """
    Выборка координат если есть локации в НЕР
    """
    logger.debug(loc)

    coords = []

    # Проверка багов
    if type(loc) == type(list()):
        # Проверка типов
        if type(loc[0]) == type('s'):

            for subloc in loc:
                location = geolocator.geocode(str(subloc))
                coords.append((location.latitude, location.longitude))

            return coords    

        return []
    
    return []

def groupExtraction(text):
    return 'group'

def organisationExtraction(text):
    return 'organisation'
