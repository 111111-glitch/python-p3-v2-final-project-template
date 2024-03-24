"""Initial migration

Revision ID: 65313d5eb26e
Revises: 
Create Date: 2024-03-24 13:42:18.192282

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65313d5eb26e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the tasks table
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String),
        sa.Column('status', sa.String)
    )


def downgrade() -> None:
    # Drop the tasks table
    op.drop_table('tasks')
