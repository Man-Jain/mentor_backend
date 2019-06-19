"""empty message

Revision ID: f86e8ba0200a
Revises: 
Create Date: 2019-06-19 15:39:07.516801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f86e8ba0200a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('credentials',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    op.create_table('enrollment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('topic_name', sa.String(), nullable=True),
    sa.Column('mentor', sa.String(), nullable=True),
    sa.Column('mentee', sa.String(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mentor_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notification',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('topic_name', sa.String(), nullable=True),
    sa.Column('mentee', sa.String(), nullable=True),
    sa.Column('mentor', sa.String(), nullable=True),
    sa.Column('request', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('timeline',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic_name', sa.String(), nullable=True),
    sa.Column('day', sa.String(), nullable=True),
    sa.Column('goal', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topics',
    sa.Column('topic_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('topic_name')
    )
    op.create_table('user_profile',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('college', sa.String(), nullable=True),
    sa.Column('interest', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    op.drop_table('topics')
    op.drop_table('timeline')
    op.drop_table('notification')
    op.drop_table('mentor_list')
    op.drop_table('enrollment')
    op.drop_table('credentials')
    # ### end Alembic commands ###
