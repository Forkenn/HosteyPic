"""Add FTS on posts

Revision ID: 7e2f3d27db8f
Revises: f4a3bbeff142
Create Date: 2024-11-13 16:42:39.878049

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '7e2f3d27db8f'
down_revision: Union[str, None] = 'f4a3bbeff142'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('lang', postgresql.REGCONFIG(), server_default='english', nullable=False))
    # ### end Alembic commands ###
    op.create_index(
        op.f('idx_gin_post'),
        'posts',
        [sa.text("to_tsvector(lang, coalesce(title,'') || ' ' || coalesce(body,''))")],
        postgresql_using='gin'
    )


def downgrade() -> None:
    op.drop_index('idx_gin_post', 'post')
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'lang')
    # ### end Alembic commands ###
