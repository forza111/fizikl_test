from datetime import timedelta,date
import datetime

start_date = date(2019, 1, 1)

def week_number(calculated_date: datetime.date) -> int:
    """
    Вычисление номера недели переданной даты, начиная с 2019-01-01

    Parameters
    ----------
    calculated_date: datetime.date - дата для определения номера недели

    Returns
    -------
    w_num: int - порядковый номер недели, на момент calculated_date начиная с 2019-01-01
    """
    if calculated_date < start_date:
        raise ValueError(f"Параметр calculated_date должен быть больше {start_date}\n "
                         f"Вы попытались передать {calculated_date}")
    reference_point = start_date - timedelta(days=2)
    quantity_days = (calculated_date - reference_point).days
    w_num = quantity_days // 7 + 1
    return {"week_number": w_num}
