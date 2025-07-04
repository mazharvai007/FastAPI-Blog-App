"""topic, tag, comment, and user_blog_like tables are created and using ForeignKey connected with corresponding tables

Revision ID: 19452c8c31e7
Revises: 310759b5d036
Create Date: 2025-05-19 09:15:01.037517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19452c8c31e7'
down_revision: Union[str, None] = '310759b5d036'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('topics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic_name', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_topics_id'), 'topics', ['id'], unique=False)
    op.create_index(op.f('ix_topics_topic_name'), 'topics', ['topic_name'], unique=True)
    op.add_column('blogs', sa.Column('category_id', sa.Integer(), nullable=True))
    op.add_column('blogs', sa.Column('topic_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blogs', 'topics', ['topic_id'], ['id'])
    op.create_foreign_key(None, 'blogs', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'topic_id')
    op.drop_column('blogs', 'category_id')
    op.drop_index(op.f('ix_topics_topic_name'), table_name='topics')
    op.drop_index(op.f('ix_topics_id'), table_name='topics')
    op.drop_table('topics')
    # ### end Alembic commands ###
