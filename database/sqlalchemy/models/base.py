import sqlalchemy
from sqlalchemy import String, Integer, Numeric
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, registry

from .types import *


class Base(DeclarativeBase):

    type_annotation_map = {
        str_15: String(15),
        str_30: String(30),
        str_50: String(50),
        dec_16_4: Numeric(16, 4),
        dec_6_2: Numeric(6, 2),
    }

    id: Mapped[intpk]
