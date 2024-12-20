from typing import Annotated
import uuid as uuid_
from sqlalchemy.orm import mapped_column
import sqlalchemy as sa


__all__ = (
    'uuid',
    'uuid_not_null',
)


uuid = Annotated[
    uuid_.UUID | None,
    mapped_column(
        sa.UUID,
        nullable=True,
    )
]


uuid_not_null = Annotated[
    uuid_.UUID,
    mapped_column(
        sa.UUID,
        nullable=False,
    )
]
