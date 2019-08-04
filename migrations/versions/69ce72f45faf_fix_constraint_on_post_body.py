"""fix constraint on post body

Revision ID: 69ce72f45faf
Revises: c83da4a98bed
Create Date: 2019-08-04 21:41:27.065341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69ce72f45faf'
down_revision = 'c83da4a98bed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_post_body', table_name='post')
    op.create_index(op.f('ix_post_body'), 'post', ['body'], unique=False)
    op.create_unique_constraint(None, 'post', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='unique')
    op.drop_index(op.f('ix_post_body'), table_name='post')
    op.create_index('ix_post_body', 'post', ['body'], unique=1)
    # ### end Alembic commands ###
