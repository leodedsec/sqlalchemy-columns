from typing import Annotated
from datetime import datetime
from sqlalchemy.orm import mapped_column
import sqlalchemy as sa


__all__ = (
    'created_at_tz',
    'updated_at_tz',
    'datetime_tz',
)


created_at_tz = Annotated[
    datetime,
    mapped_column(
        sa.DateTime(timezone=True),
        default=sa.func.now(),
        nullable=False,
    )
]


updated_at_tz = Annotated[
    datetime | None,
    mapped_column(
        sa.DateTime(timezone=True),
        onupdate=sa.func.now(),
        nullable=True,
    )
]


datetime_tz = Annotated[
    datetime | None,
    mapped_column(
        sa.DateTime(timezone=True),
        nullable=True,
    )
]
