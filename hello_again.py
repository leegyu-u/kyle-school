import datetime
from datetime import timezone

seoul_timezone = timezone('Asia/Seoul')
ct = datetime.datetime.now(seoul_timezone).strftime("%Y-%m-%d %H:%M:%S")

print('hello again :)')
print(f'it\'s {ct}')
