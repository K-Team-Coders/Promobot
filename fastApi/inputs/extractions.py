import sys
from pathlib import Path

sys.path.append(Path(__file__).parent.parent.joinpath('models').__str__())

from models.model_pavlov_all_data.model import pavlov_all
from models.ner.model import nner

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

def groupExtraction(text):
    return 'group'

def organisationExtraction(text):
    return 'organisation'
