"""create_tables

Revision ID: 480c3ee0f15f
Revises: 
Create Date: 2018-01-26 23:02:35.863263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '480c3ee0f15f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "patient",
        sa.Column("id", sa.Integer, primary_key=True,
                  unique=True, index=True, nullable=False),
        sa.Column("first_name", sa.String(255), nullable=False),
        sa.Column("last_name", sa.String(255), nullable=False),
        sa.Column("cpf", sa.String(11), nullable=False),
        sa.Column("date_of_birth", sa.Date, nullable=False),
        sa.Column("gender", sa.Boolean, nullable=False),
        sa.Column("active", sa.Boolean, default=True, nullable=False)
    )

    op.create_table(
        "procedure",
        sa.Column("id", sa.Integer, primary_key=True,
                  unique=True, index=True, nullable=False),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("active", sa.Boolean, default=True, nullable=False)
    )

    op.create_table(
        "appointment",
        sa.Column("id", sa.Integer, primary_key=True,
                  unique=True, index=True, nullable=False),
        sa.Column("patient_id", sa.Integer,
                  sa.ForeignKey("patient.id"), nullable=False),
        sa.Column("procedure_id", sa.Integer,
                  sa.ForeignKey("procedure.id"), nullable=False),
        sa.Column("start_date", sa.DateTime,
                  default=sa.func.now(), nullable=False),
        sa.Column("end_date", sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table("patient")
    op.drop_table("procedure")
    op.drop_table("appointment")
