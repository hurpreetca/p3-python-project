"""Changed the name to final_status

Revision ID: 989720e89a76
Revises: 73269d75e434
Create Date: 2023-09-02 11:57:26.404717

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '989720e89a76'
down_revision: Union[str, None] = '73269d75e434'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('final_status', sa.String(length=20), nullable=True))
        batch_op.drop_column('resolution_status')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('resolution_status', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('final_status')

    # ### end Alembic commands ###
