from decimal import Decimal
from datetime import datetime
from typing_extensions import Annotated

from sqlalchemy import func
from sqlalchemy.orm import mapped_column

str_15 = Annotated[str, 15]
str_30 = Annotated[str, 30]
str_50 = Annotated[str, 50]
dec_16_4 = Annotated[Decimal, 16]
dec_6_2 = Annotated[Decimal, 6]

intpk = Annotated[int, mapped_column(primary_key=True)]

timestamp = Annotated[
    datetime,
    mapped_column(nullable=True, server_default=func.current_timestamp())
]

update_timestamp = Annotated[
    datetime,
    mapped_column(
        nullable=False,
        server_default=func.now(),
        server_onupdate=func.now()
    ),
]
