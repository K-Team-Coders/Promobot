import sys
from pathlib import Path
from datetime import datetime

from loguru import logger
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

sys.path.append(Path(__file__).parent.parent.joinpath('database').__str__())

from database.dbmodels import MessagesModel
from database.sqlalchemy import current_session

from .extractions import *

class Message(BaseModel):
    message: str
    
router = APIRouter()

@router.post('/add_message_all_pavlov')
def addNewMessageAllPavlov(item: Message):
    """
    Основная функция по добавлению сообщения    
    с помощью модели all_pavlov
    """
    # Получаем сообщение 
    logger.debug(f"Сообщение -- {item}")
    message = item.message

    # Обрабатываем поля
    theme = themeExtraction(message)
    ner = nerExtraction(message)
    loc = locExtraction(ner)
    group = groupExtraction(message)
    date = datetime.now()
    organisation = organisationExtraction(message)
    coords = coordsExtraction(loc)

    # Логгируем
    logger.debug(f"Тема сообщения -- {theme}")
    logger.debug(f"Сущности (закодированные) -- {ner}")
    logger.debug(f"Группы -- {group}")
    logger.debug(f"Локации -- {loc}")
    logger.debug(f"Время -- {date}")
    logger.debug(f"Координаты -- {coords}")
    logger.debug(f"Организация -- {organisation}")
    logger.debug(f"Обработанный текст -- {message}")

    # Добавляем в БД
    current_session.add(MessagesModel(
        message = message,
        organisation = organisation,
        theme = theme,
        group = group,
        date = date,
        ner = ner.__str__(),
        coords = coords.__str__()
        )
    )
    current_session.commit()

    return JSONResponse(
        status_code=201, 
        content = {
            "organisation": organisation,
            "message": item.message,
            "group": group,
            "theme": theme,
            "date": date.__str__(),
            "ner": ner,
            "loc": loc,
            "coords": coords
            }
        )