"""Create country and measure tables

Revision ID: 865d9efba6ea
Revises: 4f2e2c180af
Create Date: 2019-06-19 22:46:11.465239

"""

# revision identifiers, used by Alembic.
revision = '865d9efba6ea'
down_revision = '4f2e2c180af'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('measure',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=32), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('date', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('measure')
    op.drop_table('country')
