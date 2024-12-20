from typing import Annotated
from sqlalchemy.orm import mapped_column
import sqlalchemy as sa


__all__ = (
    'text',
    'text_unique',
    'text_not_null',
)


text = Annotated[
    str | None,
    mapped_column(
        sa.Text,
        nullable=True,
    )
]

text_unique = Annotated[
    str,
    mapped_column(
        sa.Text,
        unique=True,
        nullable=False,
    )
]


text_not_null = Annotated[
    str,
    mapped_column(
        sa.Text,
        nullable=False,
    )
]
