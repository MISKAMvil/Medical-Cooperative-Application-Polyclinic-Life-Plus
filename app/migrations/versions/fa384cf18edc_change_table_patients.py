"""Change table patients

Revision ID: fa384cf18edc
Revises: 1db2884ee99a
Create Date: 2023-10-25 20:49:44.191309

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fa384cf18edc'
down_revision = '1db2884ee99a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('middle_name', sa.String(length=100), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('home_address', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_patients'))
    )
    op.drop_table('patient')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patient',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('gender', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('birth_date', sa.DATE(), nullable=False),
    sa.Column('home_address', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('patients')
    # ### end Alembic commands ###
