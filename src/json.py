from typing import Annotated
from sqlalchemy.orm import mapped_column
import sqlalchemy.dialects.postgresql as pg_dialect


__all__ = (
    'json',
    'jsonb',
)


json = Annotated[
    dict | list | None,
    mapped_column(
        pg_dialect.JSON,
        nullable=True,
    )
]

jsonb = Annotated[
    dict | list | None,
    mapped_column(
        pg_dialect.JSONB,
        nullable=True,
    )
]
