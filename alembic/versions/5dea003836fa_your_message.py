"""your_message

Revision ID: 5dea003836fa
Revises: 2443102041f6
Create Date: 2025-09-19 14:05:40.761139

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5dea003836fa'
down_revision: Union[str, Sequence[str], None] = '2443102041f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
