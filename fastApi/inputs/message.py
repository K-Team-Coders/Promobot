import sys
from pathlib import Path
from datetime import datetime

from loguru import logger
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

sys.path.append(Path(__file__).parent.parent.joinpath('database').__str__())
sys.path.append(Path(__file__).parent.parent.joinpath('models').__str__())

logger.debug(sys.path)

from database.dbmodels import MessagesModel
from database.sqlalchemy import current_session

from models.model_pavlov_all_data.model import pavlov_all

def themeExtraction(text):
    return pavlov_all.predict(text)

def nerExtraction(text):
    return ['ner1', 'ner2', 'ner3']

def groupExtraction(text):
    return 'group'

def organisationExtraction(text):
    return 'organisation'

class Message(BaseModel):
    message: str
    
router = APIRouter()

@router.post('/add_message')
def addNewMessage(item: Message):
    """
    Основная функция по добавлению сообщения    
    """
    # Получаем сообщение 
    logger.debug(f"Сообщение -- {item}")
    message = item.message

    # Обрабатываем поля
    theme = themeExtraction(message)
    ner = ''
    for x in nerExtraction(message):
        ner += str(x) + ";;;"
    group = groupExtraction(message)
    date = datetime.now()
    organisation = organisationExtraction(message)

    # Логгируем
    logger.debug(f"Тема сообщения -- {theme}")
    logger.debug(f"Сущности (закодированные) -- {ner}")
    logger.debug(f"Группы -- {group}")
    logger.debug(f"Время -- {date}")
    logger.debug(f"Организация -- {organisation}")

    # Добавляем в БД
    current_session.add(MessagesModel(
        message = message,
        organisation = organisation,
        theme = theme,
        group = group,
        date = date,
        ner = ner
        )
    )
    current_session.commit()

    return JSONResponse(
        status_code=201, 
        content = {
            "organisation": organisation,
            "message": message,
            "group": group,
            "theme": theme,
            "date": date.__str__(),
            "ner": ner,
            }
        )