"""Initial migraton

Revision ID: 57ab8aeb53ce
Revises: 2401ae4a7218
Create Date: 2024-02-15 18:11:08.328427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57ab8aeb53ce'
down_revision = '2401ae4a7218'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=350), nullable=True),
    sa.Column('content_type', sa.String(length=50), nullable=True),
    sa.Column('published_date', sa.DateTime(), nullable=True),
    sa.Column('content_url', sa.String(length=250), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('dislikes', sa.Integer(), nullable=True),
    sa.Column('flagged', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('content_type')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contents')
    # ### end Alembic commands ###
