from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        start_date1 = self.dates[0][0]
        end_date1 = self.dates[0][1]
        delta = timedelta(days=1)
        while start_date1 <= end_date1:
            yield start_date1
            start_date1 += delta
        start_date2 = self.dates[1][0]
        end_date2 = self.dates[1][1]
        while start_date2 <= end_date2:
            yield start_date2
            start_date2 += delta


m = Movie('sw', [(datetime(2020, 1, 1), datetime(2020, 1, 7)), (datetime(2020, 1, 15), datetime(2020, 2, 7))])

for d in m.schedule():
    print(d)