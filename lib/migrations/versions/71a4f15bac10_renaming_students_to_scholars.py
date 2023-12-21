"""Renaming students to scholars

Revision ID: 71a4f15bac10
Revises: 791279dd0760
Create Date: 2023-12-21 04:36:06.541862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71a4f15bac10'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
