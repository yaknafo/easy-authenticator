"""role_endpoint_table

Revision ID: 4702767fa03f
Revises: de99a494d79f
Create Date: 2023-09-20 16:30:18.615323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4702767fa03f'
down_revision: Union[str, None] = 'de99a494d79f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create role endpoint table
    op.create_table(
        "role_endpoint",
        sa.Column("role_id", sa.Integer, sa.ForeignKey("role.id"), primary_key=True),
        sa.Column("api_id", sa.String(200), sa.ForeignKey("endpoint.api_id"), primary_key=True)
    )


def downgrade() -> None:
    op.drop_table("role_endpoint")
