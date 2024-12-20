from typing import Annotated
from sqlalchemy.orm import mapped_column
import sqlalchemy as sa


__all__ = (
    'bigint',
    'bigint_not_null',
    'float_',
    'float_not_null',
)


bigint = Annotated[
    int,
    mapped_column(
        sa.BigInteger,
    )
]


bigint_not_null = Annotated[
    int,
    mapped_column(
        sa.BigInteger,
        nullable=False,
    )
]


float_ = Annotated[
    float,
    mapped_column(
        sa.Float,
    )
]


float_not_null = Annotated[
    float,
    mapped_column(
        sa.Float,
        nullable=False,
    )
]
