import sys
import pandas as pd
from tqdm import tqdm
from pathlib import Path
from loguru import logger
from datetime import datetime

sys.path.append(Path(__file__).parent.parent.joinpath('models').__str__())

from models.model_pavlov_all_data.model import pavlov_all
from models.model_group.model import pavlov_group_all

def themeExtraction(text):
    """
    Функция по вычленению темы из поднанного текста

    моделью pavlov_all
    """
    return pavlov_all.predict(text)

def groupExtraction(text):
    """
    Функция по поиску группы тем в заданных текстах
    pavlov_group_model
    """
    return pavlov_group_all.predict(text)

test = pd.read_csv('test.csv', encoding='utf-8', sep=';')
submit = pd.read_csv('submission.csv', encoding='utf-8', sep=';')

print(test.head(5))
print(submit.head(5))

submit = submit.iloc[0:0]

print(submit)

start = datetime.now()

themes = []
groups= []
for index, data in tqdm(test.iterrows(), 'Предсказываем по моделям'):
    if len(data[1]) > 512:
        data = data[1][:511]
    try:
        themes.append(themeExtraction(data[1].replace("'", "")))
        groups.append(groupExtraction(data[1].replace("'", "")))
    except:
        themes.append('None')
        groups.append('None')
        logger.error(data)

end = datetime.now()
logger.debug(f'Finished counting -- {end - start}')

submit['Тема'] = themes
submit['Группа тем'] = groups
submit['id'] = range(len(themes))

submit.to_csv("submit.csv", sep = ';', index = False, encoding = 'utf-8')
 
