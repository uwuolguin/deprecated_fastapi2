"""generacion tabla user  #1

Revision ID: efa2176321cd
Revises: 
Create Date: 2023-10-28 21:12:37.955268

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text


# revision identifiers, used by Alembic.
revision: str = 'efa2176321cd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('email',sa.String(),nullable=False),
    sa.Column('password',sa.String(),nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    #,op.add_column('user',sa.Column('created_at2',sa.TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')))
    
#lo comentado es un ejemplo de como agregra una revision para añadir y sacar columnas


    )


def downgrade() -> None:
    op.drop_table('users')\
    #,op.drop_column('users','created_at2')
