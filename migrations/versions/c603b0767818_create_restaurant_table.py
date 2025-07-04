"""create restaurant table

Revision ID: c603b0767818
Revises: 9c463eb6c456
Create Date: 2025-07-02 01:01:52.576349

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c603b0767818'
down_revision: Union[str, None] = '9c463eb6c456'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "restaurant",
        sa.Column("id", sa.String(), primary_key=True, nullable=False, unique=True, index=True),
        sa.Column("lat", sa.Float(), nullable=False),
        sa.Column("lng", sa.Float(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("opening_time", sa.Time(), nullable=False),
        sa.Column("closing_time", sa.Time(), nullable=False),
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("restaurant")
    pass
