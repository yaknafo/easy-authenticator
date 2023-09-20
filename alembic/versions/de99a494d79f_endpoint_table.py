"""endpoint_table

Revision ID: de99a494d79f
Revises: 6b99402f0104
Create Date: 2023-09-20 15:59:54.677515

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de99a494d79f'
down_revision: Union[str, None] = '6b99402f0104'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create endpoint table
    op.create_table(
        "endpoint",
        sa.Column("api_id", sa.String(200), primary_key=True),
        sa.Column("listen_path", sa.String(255), nullable=False, unique=True),
        sa.Column("target_url", sa.String(255), nullable=False),
        sa.Column("auth_header_name", sa.String(255), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("endpoint")

