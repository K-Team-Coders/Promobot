import sys
import ast
import shutil
from pathlib import Path
from datetime import timedelta
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
            "coords": ast.literal_eval(part.coords),
            "loc": part.loc
        })

    return result

@router.get('/extra_issues')
def getExtraIssues():
    """
    Функция по нахождению актуальных событий за последние 5 часов
    """
    result = []

    query = current_session.query(MessagesModel).filter(MessagesModel.date >= (datetime.now() - timedelta(hours=5)))

    total_themes = []

    stats_themes = {}
    stats_groups = {}
    for part in query:
        total_themes.append(part.theme)

        if part.theme in list(stats_themes.keys()):
            stats_themes[f"{part.theme}"] += 1 
        else:
            stats_themes[f"{part.theme}"] = 1 

        if part.group in list(stats_groups.keys()):
            stats_groups[f"{part.group}"] += 1 
        else:
            stats_groups[f"{part.group}"] = 1 

    total_themes = list(set(total_themes))

    for part in query:
        result.append({
            "message": part.message,
            "organisation": part.organisation,
            "theme": part.theme,
            "group": part.group,
            "date": part.date.__str__(),
            "ner": ast.literal_eval(part.ner),
            "coords": ast.literal_eval(part.coords),
            "loc": part.loc
        })

    return JSONResponse(status_code=200, content={
        "actual" : result,
        "theme_stats": stats_themes,
        "group_stats": stats_groups,
    })
