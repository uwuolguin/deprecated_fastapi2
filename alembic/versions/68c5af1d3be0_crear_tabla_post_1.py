"""crear tabla post  #1

Revision ID: 68c5af1d3be0
Revises: efa2176321cd
Create Date: 2023-10-28 22:50:51.028627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import text

# revision identifiers, used by Alembic.
revision: str = '68c5af1d3be0'
down_revision: Union[str, None] = 'efa2176321cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',
    sa.PrimaryKeyConstraint('id'),
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('title',sa.String(),nullable=False),
    sa.Column('content',sa.String(),nullable=False),
    sa.Column('published',sa.Boolean(),server_default="TRUE"),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')),
    sa.Column('owner_id',sa.Integer(),nullable=False),
    #,op.add_column('user',sa.Column('created_at2',sa.TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')))
#lo comentado es un ejemplo de como agregra una revision para añadir y sacar columnas
    )

    op.create_foreign_key('post_users_fk',source_table="posts",referent_table="users",
                          local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE"

    )

    pass


def downgrade() -> None:
    op.drop_table('posts')\
    #,op.drop_column('users','created_at2')
    pass
