# pylint: disable=E1101,C0301,W0611
"""add Created at

Revision ID: 2f0015c281bd
Revises: eada31b694e9
Create Date: 2024-01-03 20:40:13.633340

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2f0015c281bd'
down_revision: Union[str, None] = 'eada31b694e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transcripts', sa.Column('created_at', sa.DateTime(), nullable=True), schema='rtvt')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transcripts', 'created_at', schema='rtvt')