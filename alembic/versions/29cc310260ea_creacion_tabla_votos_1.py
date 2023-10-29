"""creacion tabla votos #1

Revision ID: 29cc310260ea
Revises: 68c5af1d3be0
Create Date: 2023-10-28 23:18:52.687812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29cc310260ea'
down_revision: Union[str, None] = '68c5af1d3be0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('votes',
    sa.Column('post_id',sa.Integer(),nullable=False),
    sa.Column('user_id',sa.Integer(),nullable=False),
    #,op.add_column('user',sa.Column('created_at2',sa.TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')))
#lo comentado es un ejemplo de como agregra una revision para añadir y sacar columnas
    )

    op.create_foreign_key('post_fk',source_table="votes",referent_table="posts",
                          local_cols=['post_id'],remote_cols=['id'],ondelete="CASCADE"

    )

    op.create_foreign_key('user_fk',source_table="votes",referent_table="users",
                          local_cols=['user_id'],remote_cols=['id'],ondelete="CASCADE"

    )

    op.create_primary_key('pk_votes','votes',['post_id','user_id'])

    pass


def downgrade() -> None:
    op.drop_table('votes')\
    #,op.drop_column('users','created_at2')
    pass
