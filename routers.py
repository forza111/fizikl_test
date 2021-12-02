from typing import List, Optional
import datetime
from fastapi import APIRouter, Depends

from computation import week_number
import schemas

router = APIRouter(tags=["Calculations API"])


@router.post('/week')
async def get_week_number(date: schemas.CheckDate):
    response = week_number(date.calculated_date)
    return response
