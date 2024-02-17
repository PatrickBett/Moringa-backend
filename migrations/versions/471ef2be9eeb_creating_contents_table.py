"""Creating contents table

Revision ID: 471ef2be9eeb
Revises: ed9c1ddd9b4c
Create Date: 2024-02-16 10:05:00.681004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '471ef2be9eeb'
down_revision = 'ed9c1ddd9b4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contents', schema=None) as batch_op:
        batch_op.drop_column('published_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contents', schema=None) as batch_op:
        batch_op.add_column(sa.Column('published_date', sa.DATETIME(), nullable=True))

    # ### end Alembic commands ###
