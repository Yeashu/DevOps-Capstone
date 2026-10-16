from datetime import datetime, timezone

from sqlalchemy import CheckConstraint, DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Calculation(Base):
    __tablename__ = "calculations"
    __table_args__ = (CheckConstraint("angle_mode IN ('rad', 'deg')", name="ck_angle_mode"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    expression: Mapped[str] = mapped_column(String(256))
    result: Mapped[float] = mapped_column(Float)
    angle_mode: Mapped[str] = mapped_column(String(3))
    label: Mapped[str] = mapped_column(String(80), default="")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
