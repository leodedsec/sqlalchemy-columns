from typing import Annotated
import uuid
from sqlalchemy.orm import mapped_column
import sqlalchemy as sa


__all__ = (
    'pk_uuid7',
    'pk_uuid4',
    'pk_int',
    'pk_big_int',
)


pk_uuid7 = Annotated[
    uuid.UUID,
    mapped_column(
        sa.UUID,
        primary_key=True,
        server_default=sa.func.text("idkit_uuidv7_generate()"),
    ),
]


pk_uuid4 = Annotated[
    uuid.UUID,
    mapped_column(
        sa.UUID,
        primary_key=True,
        default=sa.func.text("gen_random_uuid()"),
    )
]


pk_int = Annotated[
    int,
    mapped_column(
        primary_key=True,
    )
]


pk_big_int = Annotated[
    int,
    mapped_column(
        sa.BigInteger,
        primary_key=True,
    )
]
