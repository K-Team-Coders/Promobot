import re
import sys
from pathlib import Path
from loguru import logger
from geopy.geocoders import Nominatim

import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

mystem = Mystem() 
russian_stopwords = stopwords.words("russian")

sys.path.append(Path(__file__).parent.parent.joinpath('models').__str__())

from models.model_pavlov_all_data.model import pavlov_all
from models.model_group.model import pavlov_group_all
from models.model_organisations.model import pavlov_organisations_all
from models.ner.model import nner

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

geolocator = Nominatim(user_agent="promobot_k_team")

def upcase_first_letter(s):
    return s[0].upper() + s[1:]

def lemmatize(text):
    words = text.split() # разбиваем текст на слова
    res = list()
    for word in words:
        p = morph.parse(word)[0]
        res.append(upcase_first_letter(p.normal_form))

    return res


def preprocessText(text):

    text = re.sub(r"https?://\S+", "", text)
    text = " ".join([w for w in text.split() if w.isalpha()])
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"\b[0-9]+\b\s*", "", text)
    text = re.sub(r'(.)\1{3,}',r'\1', text)
    text = " ".join([w for w in text.split() if not w.isdigit()])
    tokens = mystem.lemmatize(text) 
    tokens = [upcase_first_letter(token) for token in tokens if token not in russian_stopwords\
              and token != " " \
              and token.strip() not in punctuation]
    text = " ".join(tokens)
    return text

def themeExtraction(text):
    """
    Функция по вычленению темы из поднанного текста

    моделью pavlov_all
    """
    return pavlov_all.predict(text)

def nerExtraction(text):
    """
    Извлечение именованных сущностей
    """
    logger.debug(text)

    markup = nner(text)

    text_spans = markup.spans

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
    """
    Функция по поиску LOC в Нерах
    """
    logger.debug(ners)

    locs = []
    
    # Отбраковка багов
    if type(ners) == type(list()):

        # Если нера нет
        if type(ners[0]) == type('s'): return locs
    
        for ner in ners:
            if ner["named_entity"] == "LOC":
                locs.append(lemmatize(ner["token"])[0])
    return locs

def coordsExtraction(loc):
    """
    Выборка координат если есть локации в НЕР
    """

    logger.debug(loc)
    
    coords = []

    # Проверка багов
    if type(loc) == type(list()) and len(loc) != 0:
        # Проверка типов
        if type(loc[0]) == type('s'):

            for subloc in loc:
                location = geolocator.geocode(str(subloc))
                if location:
                    coords.append((location.latitude, location.longitude))

            return coords    

        return []
    
    return []

def groupExtraction(text):
    """
    Функция по поиску группы тем в заданных текстах
    pavlov_group_model
    """
    return pavlov_group_all.predict(text)

def organisationExtraction(text):
    """
    Функция по поиску исполнителя в заданных текстах
    pavlov_organisations_model
    """
    return pavlov_organisations_all.predict(text)
