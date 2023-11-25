import sys
import shutil
from pathlib import Path
from datetime import datetime

import pandas as pd
from loguru import logger
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
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
    Основная функция по добавлению файла в формате csv и выводе его в xlsx    
    с помощью модели all_pavlov
    """

    # Сохраняем файл
    path_to_save = Path.cwd().parent.joinpath('download').joinpath(file.filename)
    with open(path_to_save, "wb") as dest_file:
        shutil.copyfileobj(file.file, dest_file)

    data = pd.read_csv(path_to_save.__str__(), delimiter=';', encoding='utf-8')

    logger.debug(data['Текст инцидента'])

    start = datetime.now()

    # result = []

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

        # # Данные для ответа по REST
        # result.append({
        #     "ner": ner,
        #     "organisation": organisation,
        #     "loc": loc[0],
        #     "coords": coords,
        #     "theme": theme,
        #     "group": group,
        #     "text": text,
        #     "date": date
        # })

    logger.warning(type(total_texts[0]))
    logger.warning(total_texts[0][0])

    dataframe = pd.DataFrame(data= {
            "Тексты" : [x[0].replace("'", "").replace(',', ' ') for x in total_texts], 
            "Темы" : [x[0] for x in total_themes], 
            "Группы тем" : [x[0] for x in total_group], 
            "Исполнители" : [x[0] for x in  total_organisations], 
            "NER" : [x.replace(',', ' ') for x in total_ner]
        })  
          
    # dataframe.to_excel('data_result.xlsx', engine="openpyxl", index=False)
    # return FileResponse(
    #     filename="data_result.xlsx", 
    #     path='data_result.xlsx' 
    #     )
    dataframe.to_csv('data_result.csv', encoding="utf-8", sep=';')

    end = datetime.now()
    logger.debug(f'Calculating: {end - start}')

    return FileResponse(
        filename="data_result.csv", 
        path='data_result.csv' 
        )