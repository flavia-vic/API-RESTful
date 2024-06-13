"""adicionando coluna quantidade em purchase_orders_items

Revision ID: 25963985e671
Revises: 9abe58b9f52e
Create Date: 2024-06-12 15:13:43.326960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25963985e671'
down_revision = '9abe58b9f52e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchase_orders_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchase_orders_items', schema=None) as batch_op:
        batch_op.drop_column('quantity')

    # ### end Alembic commands ###