"""Create phone number for user Table

Revision ID: 02b7939fcdeb
Revises: 0034b216c826
Create Date: 2026-01-10 22:10:00.484432

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02b7939fcdeb'
down_revision: Union[str, Sequence[str], None] = '0034b216c826'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
