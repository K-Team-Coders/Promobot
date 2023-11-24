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

    for text in data["Текст инцидента"]:
        result.append({
            "ner": nerExtraction(text),
            "organisation": organisationExtraction(text),
            "loc": locExtraction(nerExtraction(text)),
            "coords": coordsExtraction(locExtraction(nerExtraction(text))),
            "theme": themeExtraction(text),
            "group": groupExtraction(text),
            "text": text,
            "date": datetime.now().__str__()
        })

    end = datetime.now()
    logger.debug(f'Calculating: {end - start}')

    return JSONResponse(
        status_code=200, 
        content = {
            "result": result,
            }        
        )