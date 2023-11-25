import sys
import shutil
from pathlib import Path
from datetime import datetime

import pandas as pd
from loguru import logger
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel

sys.path.append(Path(__file__).parent.parent.joinpath('database').__str__())

from .extractions import *

from database.dbmodels import MessagesModel
from database.sqlalchemy import current_session

class Message(BaseModel):
    message: str
    
router = APIRouter()

@router.post('/add_file_all_pavlov')
def addNewFileAllPavlov(file: UploadFile = File(...)):
    """
    Основная функция по добавлению файла в формате csv    
    с помощью модели all_pavlov
    """

    # Сохраняем файл
    path_to_save = Path.cwd().parent.joinpath('download').joinpath(file.filename)
    with open(path_to_save, "wb") as dest_file:
        shutil.copyfileobj(file.file, dest_file)

    data = pd.read_csv(path_to_save.__str__(), delimiter=';', encoding='utf-8')

    logger.debug(data['Текст инцидента'])

    start = datetime.now()

    result = []

    total_texts = []
    total_ner = []
    total_organisations = []
    total_group = []
    total_themes = []

    # Собираем данные по колонке текста (и только текста!)
    for text in data["Текст инцидента"]:

        # Обработка данных
        ner = nerExtraction(text)
        organisation = organisationExtraction(text),
        loc = locExtraction(ner),
        coords = coordsExtraction(loc),
        theme = themeExtraction(text),
        group = groupExtraction(text),
        text = text,
        date = datetime.now().__str__()

        # Данные для возвращаемого файла
        total_texts.append(text)
        total_organisations.append(organisation)
        total_ner.append(ner.__str__())
        total_group.append(group)
        total_themes.append(theme)

        # Данные для БД
        current_session.add(MessagesModel(
            message = text,
            organisation = organisation,
            theme = theme,
            group = group,
            date = date,
            ner = ner.__str__(),
            coords = coords.__str__(),
            loc = loc.__str__()
            )
        )
        current_session.commit()

        # Данные для ответа по REST
        result.append({
            "ner": ner,
            "organisation": organisation,
            "loc": loc,
            "coords": coords,
            "theme": theme,
            "group": group,
            "text": text,
            "date": date
        })

    dataframe = pd.DataFrame(data= {
            "Тексты" : total_texts, 
            "Темы" : total_themes, 
            "Группы тем" :total_group, 
            "Исполнители" : total_organisations, 
            "NER" : total_ner
        })    
    dataframe.to_csv('data_result.csv', encoding='utf-8', sep=';')

    end = datetime.now()
    logger.debug(f'Calculating: {end - start}')

    return JSONResponse(
        status_code=200, 
        content = {
            "result": result,
            }        
        )