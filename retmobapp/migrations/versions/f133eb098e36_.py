"""empty message

Revision ID: f133eb098e36
Revises: 41e45ddf136c
Create Date: 2017-11-13 23:55:20.313947

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f133eb098e36'
down_revision = '41e45ddf136c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('filemap_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'tasks', 'filemap', ['filemap_id'], ['id'])
    op.drop_column('tasks', 'task_uploads_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('task_uploads_url', mysql.VARCHAR(length=128), nullable=False))
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'filemap_id')
    # ### end Alembic commands ###
