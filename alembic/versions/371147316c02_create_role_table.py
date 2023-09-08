"""create role table

Revision ID: 371147316c02
Revises: 
Create Date: 2023-09-01 11:13:14.265612

"""
from typing import Sequence, Union
from sqlalchemy.dialects.postgresql import UUID
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '371147316c02'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create role table
    op.create_table(
        "role",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(50), nullable=False, unique=True),
        sa.Column("token", sa.String(200)),
    )


def downgrade() -> None:
    op.drop_table("role")

