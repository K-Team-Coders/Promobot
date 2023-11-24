import sys
import ast
import shutil
from pathlib import Path
from datetime import datetime

import pandas as pd
from loguru import logger
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel

sys.path.append(Path(__file__).parent.parent.joinpath('database').__str__())

from database.dbmodels import MessagesModel
from database.sqlalchemy import current_session
    
router = APIRouter()

@router.get('/total_organisations')
def getTotalOrganisations():
    """
    Функция по просмотру организаций в бд
    """

    query = current_session.query(MessagesModel).all()
    data = [x.organisation for x in query]
    unique = list(set(data))

    return JSONResponse(
        status_code=200, 
        content = {
            "organisations": unique,
            }
        )

@router.get('/total_db')
def getTotalDB():
    """
    Функция для выписки всей собранной БД
    """

    result = []

    query = current_session.query(MessagesModel).all()
    for part in query:
        result.append({
            "message": part.message,
            "organisation": part.organisation,
            "theme": part.theme,
            "group": part.group,
            "date": part.date,
            "ner": ast.literal_eval(part.ner),
            "coords": ast.literal_eval(part.coords)
        })

    return result