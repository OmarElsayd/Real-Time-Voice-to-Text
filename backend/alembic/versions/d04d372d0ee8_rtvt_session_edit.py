# pylint: disable=E1101,C0301
"""rtvt_session_edit

Revision ID: d04d372d0ee8
Revises: a017c4be5a28
Create Date: 2023-12-28 17:58:28.805177

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'd04d372d0ee8'
down_revision: Union[str, None] = 'a017c4be5a28'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rtvt_sessions', sa.Column('session_passcode', sa.String(length=100), nullable=True), schema='rtvt')
    op.add_column('rtvt_sessions', sa.Column('is_call', sa.Boolean(), nullable=False), schema='rtvt')
    op.add_column('rtvt_sessions', sa.Column('session_code', sa.String(length=20), nullable=False), schema='rtvt')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rtvt_sessions', 'session_code', schema='rtvt')
    op.drop_column('rtvt_sessions', 'is_call', schema='rtvt')
    op.drop_column('rtvt_sessions', 'session_passcode', schema='rtvt')

    # ### end Alembic commands ###
