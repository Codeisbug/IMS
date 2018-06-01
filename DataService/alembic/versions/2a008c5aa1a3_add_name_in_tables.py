"""add name in Tables

Revision ID: 2a008c5aa1a3
Revises: 9f6b19e8f385
Create Date: 2018-05-03 23:21:05.336216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a008c5aa1a3'
down_revision = '9f6b19e8f385'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tables', sa.Column('name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tables', 'name')
    # ### end Alembic commands ###