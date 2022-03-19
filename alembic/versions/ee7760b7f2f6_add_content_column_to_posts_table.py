"""add content column to posts table

Revision ID: ee7760b7f2f6
Revises: 84376eac811b
Create Date: 2022-03-15 22:49:52.559273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee7760b7f2f6'
down_revision = '84376eac811b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
