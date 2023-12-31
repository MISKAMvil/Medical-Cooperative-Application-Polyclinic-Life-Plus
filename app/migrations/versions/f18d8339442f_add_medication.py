"""Add medication

Revision ID: f18d8339442f
Revises: a8431721f4a5
Create Date: 2023-11-08 20:13:04.165354

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision = 'f18d8339442f'
down_revision = 'a8431721f4a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    inspector = inspect(op.get_bind())
    if not inspector.has_table('medications'):
        op.create_table('medications',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(length=100), nullable=False),
            sa.Column('method_of_use', sa.String(length=255), nullable=False),
            sa.Column('description', sa.Text(), nullable=False),
            sa.Column('effects', sa.Text(), nullable=False),
            sa.Column('side_effects', sa.Text(), nullable=False),
            sa.Column('appointment_id', sa.Integer(), nullable=False),
            sa.ForeignKeyConstraint(['appointment_id'], ['appointments.id'], name=op.f('fk_medications_appointment_id_appointments')),
            sa.PrimaryKeyConstraint('id', name=op.f('pk_medications'))
        )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medications')
    # ### end Alembic commands ###