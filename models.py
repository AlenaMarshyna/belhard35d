from sqlalchemy import Column, INT, VARCHAR, ForeignKey, DECIMAL, BOOLEAN, create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False, unique=True)


class Product(Base):
    __tablename__ = 'products'

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False)
    price = Column(DECIMAL(8, 2), default=1)
    is_published = Column(BOOLEAN, default=False)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)


engine = create_engine('postgresql://belhard:belhard@0.0.0.0:5432/bh35d')
Session = sessionmaker(bind=engine)

from csv import DictReader

with open('categories.csv', 'r', encoding='utf-8') as file:
    reader = DictReader(file)

    with Session() as session:
        for category in reader:
            cat = Category(**category)
            session.add(cat)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
