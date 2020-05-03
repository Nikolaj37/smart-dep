"""empty message

Revision ID: f34491dca5db
Revises: 1a67d2f02e18
Create Date: 2020-05-02 19:00:33.448953

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f34491dca5db'
down_revision = '1a67d2f02e18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('configs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('config', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('device_id', sa.String(length=50), nullable=True),
    sa.Column('place_id', sa.String(length=20), nullable=True),
    sa.Column('type', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('params')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('params',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('params', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('device_id', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('place_id', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('type', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='params_pkey')
    )
    op.drop_table('configs')
    # ### end Alembic commands ###
