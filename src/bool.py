from typing import Annotated
from sqlalchemy.orm import mapped_column
import sqlalchemy as sa


__all__ = (
    'boolean_false',
    'boolean_true',
)


boolean_false = Annotated[
    bool,
    mapped_column(
        sa.Boolean,
        default=False,
        nullable=False,
    )
]


boolean_true = Annotated[
    bool,
    mapped_column(
        sa.Boolean,
        default=True,
        nullable=False,
    )
]
