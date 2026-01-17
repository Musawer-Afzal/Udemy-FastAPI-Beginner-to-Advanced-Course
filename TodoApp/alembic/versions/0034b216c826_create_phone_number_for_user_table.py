"""Create phone number for user Table

Revision ID: 0034b216c826
Revises: 
Create Date: 2026-01-10 21:59:43.747788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0034b216c826'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable = True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')
