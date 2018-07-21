"""add server_entry

Revision ID: 0c2aa98b2fb5
Revises: 68601f75e9f3
Create Date: 2018-07-19 17:05:20.104118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c2aa98b2fb5'
down_revision = '68601f75e9f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('module_reg', sa.Column('server_entry', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('module_reg', 'server_entry')
    # ### end Alembic commands ###