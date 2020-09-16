"""empty message

Revision ID: bda0c8bc64a3
Revises: 4dd64e951c80
Create Date: 2020-09-16 23:43:35.660884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bda0c8bc64a3'
down_revision = '4dd64e951c80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('presets', sa.Column('secureon', sa.String(), nullable=True))
    op.drop_column('presets', 'secureOn')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('presets', sa.Column('secureOn', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('presets', 'secureon')
    # ### end Alembic commands ###