"""Default avatar add

Revision ID: f4a3bbeff142
Revises: a5bb3bbdc640
Create Date: 2024-11-07 17:32:28.777195

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4a3bbeff142'
down_revision: Union[str, None] = 'a5bb3bbdc640'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        'users',
        'avatar',
        existing_server_default=False,
        server_default=sa.text("'default.jpg'")
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    op.alter_column(
        'users',
        'avatar',
        existing_server_default=True,
        server_default=None
    )
    # ### end Alembic commands ###
