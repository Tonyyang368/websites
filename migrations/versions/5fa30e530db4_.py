"""empty message

Revision ID: 5fa30e530db4
Revises: ad963fa1c675
Create Date: 2020-08-18 23:09:03.080793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fa30e530db4'
down_revision = 'ad963fa1c675'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_food_groceryName'), 'food', ['groceryName'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_food_groceryName'), table_name='food')
    # ### end Alembic commands ###
