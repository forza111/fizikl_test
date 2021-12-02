import datetime

from pydantic import BaseModel,validator
from fastapi import HTTPException

from computation import start_date


class CheckDate(BaseModel):
    calculated_date: datetime.date

    @validator("calculated_date")
    def check_correct_date(cls, calculated_date):
        if calculated_date < start_date:
            raise HTTPException(status_code=400, detail=f"The calendar starts counting down from {start_date}. "
                                                        f"Field calculated_date must be greater than this date, "
                                                        f"you passed {calculated_date}"
)
        return calculated_date

class WeekNumber(BaseModel):
    week_number: int