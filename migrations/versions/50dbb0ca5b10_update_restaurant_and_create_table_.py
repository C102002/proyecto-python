"""update restaurant and create table tables manually

Revision ID: 50dbb0ca5b10
Revises: c603b0767818
Create Date: 2025-07-03 00:11:00.969575

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

from src.restaurant.domain.entities.enums.table_location_enum import TableLocationEnum


# revision identifiers, used by Alembic.
revision: str = "50dbb0ca5b10"
down_revision: Union[str, None] = "c603b0767818"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1) Creamos el ENUM en la base
    values = [e.value for e in TableLocationEnum]
    enum_type = sa.Enum(*values, name="tablelocationenum", create_type=True)
    enum_type.create(op.get_bind(), checkfirst=True)

    # 2) Creamos la tabla 'table'
    op.create_table(
        "table",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("number", sa.Integer(), nullable=False),
        sa.Column("capacity", sa.Integer(), nullable=False),
        sa.Column("location", enum_type, nullable=False),           
        sa.Column(
            "restaurant_id",
            sa.String(),
            sa.ForeignKey("restaurant.id", ondelete="CASCADE"),
            nullable=False,
        ),
    )
    op.create_index(op.f("ix_table_number"), "table", ["number"], unique=False)



def downgrade() -> None:
    op.drop_index(op.f("ix_table_number"), table_name="table")
    op.drop_table("table")

    # Eliminamos el ENUM
    values = [e.value for e in TableLocationEnum]
    enum_type = sa.Enum(*values, name="tablelocationenum", create_type=False)
    enum_type.drop(op.get_bind(), checkfirst=True)

    op.drop_index(op.f("ix_restaurant_id"), table_name="restaurant")

