"""Renaming student column

Revision ID: 53dd12e90963
Revises: 71a4f15bac10
Create Date: 2023-12-21 04:47:25.023553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53dd12e90963'
down_revision = '71a4f15bac10'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("students ",column_name="name",new_column_name="full_name")
    pass


def downgrade() -> None:
    op.alter_column("students ",column_name="full_name",new_column_name="name")
    pass
