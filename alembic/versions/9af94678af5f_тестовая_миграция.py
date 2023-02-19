"""Тестовая миграция

Revision ID: 9af94678af5f
Revises: aa626d631b10
Create Date: 2023-02-18 17:17:11.325588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9af94678af5f'
down_revision = 'aa626d631b10'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
