from typing import List, Optional
import datetime
from fastapi import APIRouter, Depends

from computation import week_number
import schemas

router = APIRouter(tags=["Calculating the day of the week API"])


@router.post('/week',response_model=schemas.WeekNumber)
async def get_week_number(date: schemas.CheckDate):
    """
    ## Вычисление номера недели переданной даты, начиная с 2019-01-01. Нумерация недель в соответствии с ISO 8601

    Body Parameters
    ----------
    JSON
    * {calculated_date: datetime.date}  - дата, необходимая для получения номера недели
    ##### Example {"calculated_date": "2021-12-02"}

    Returns
    -------
    JSON:
    * {"week_number": int} - номер недели для искомой даты
    """
    response = week_number(date.calculated_date)
    return response
