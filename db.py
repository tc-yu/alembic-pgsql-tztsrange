from datetime import datetime

from sqlalchemy import DateTime, Identity, func
from sqlalchemy.dialects.postgresql import ExcludeConstraint
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

from sqlalchemy import create_engine

DB_ADDRESS = "postgresql+psycopg://postgres:mysecretpassword@0.0.0.0:5432/timeslot"

Base = declarative_base()


class TimeSlot(Base):
    __tablename__ = "time_slot"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)

    effective_time: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), index=True
    )
    expiry_time: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), index=True
    )

    __table_args__ = (
        ExcludeConstraint(
            (func.tstzrange(effective_time, expiry_time), "&&"),
            using="gist",
        ),
    )

if __name__ == "__main__":
    engine = create_engine(DB_ADDRESS)

    with engine.connect() as conn:
        # conn.execute(text('CREATE EXTENSION IF NOT EXISTS btree_gist;'))

        # conn.commit()

        # Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
