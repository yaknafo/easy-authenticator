"""your_migration_name

Revision ID: 6b99402f0104
Revises: 371147316c02
Create Date: 2023-09-08 12:03:40.113342

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b99402f0104'
down_revision: Union[str, None] = '371147316c02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create role table
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("user_name", sa.String(50), nullable=False, unique=True),
        sa.Column("password", sa.String(200)),
        sa.Column("role_id", sa.Integer, sa.ForeignKey("role.id"))
    )


def downgrade() -> None:
    op.drop_table("user")

