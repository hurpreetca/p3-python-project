"""Added data to user using faker version1

Revision ID: 2fcd1d5c748c
Revises: 571111b2364d
Create Date: 2023-08-30 21:28:03.425156

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2fcd1d5c748c'
down_revision: Union[str, None] = '571111b2364d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###