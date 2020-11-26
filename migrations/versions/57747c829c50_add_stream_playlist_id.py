"""Add Stream.playlist_id

Revision ID: 57747c829c50
Revises: 18ce384bb442
Create Date: 2020-11-26 13:18:23.914205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57747c829c50'
down_revision = '18ce384bb442'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('streams', sa.Column('playlist_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('streams', 'playlist_id')
    # ### end Alembic commands ###