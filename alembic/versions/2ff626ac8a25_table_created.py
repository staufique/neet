"""table created

Revision ID: 2ff626ac8a25
Revises: 91f7a583b90e
Create Date: 2023-11-26 12:18:41.713776

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ff626ac8a25'
down_revision: Union[str, None] = '91f7a583b90e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
