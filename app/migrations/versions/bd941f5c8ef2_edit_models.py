"""Edit models

Revision ID: bd941f5c8ef2
Revises: f18d8339442f
Create Date: 2023-11-08 23:31:13.596009

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bd941f5c8ef2'
down_revision = 'f18d8339442f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('medications', 'appointment_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('medications', 'appointment_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
