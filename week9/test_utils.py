# test_utils.py를 아래 내용으로 overwrite합니다(-a 옵션 없이!)

import datetime
from utils import is_working_day

def test_is_working_day():
    assert is_working_day(datetime.date(2020,7,5)) == False
    assert is_working_day(datetime.date(2020,7,4)) == False
    assert is_working_day(datetime.date(2020,7,6)) == True
