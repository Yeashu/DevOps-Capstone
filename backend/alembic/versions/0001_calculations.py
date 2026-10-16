"""Create persisted scientific calculations.

Revision ID: 0001
Revises:
"""
from alembic import op
import sqlalchemy as sa

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "calculations",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("expression", sa.String(256), nullable=False),
        sa.Column("result", sa.Float(), nullable=False),
        sa.Column("angle_mode", sa.String(3), nullable=False),
        sa.Column("label", sa.String(80), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.CheckConstraint("angle_mode IN ('rad', 'deg')", name="ck_angle_mode"),
    )


def downgrade():
    op.drop_table("calculations")
