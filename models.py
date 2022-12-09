from sqlalchemy import Column, INT, VARCHAR, ForeignKey, \
    DECIMAL, BOOLEAN, create_engine, select, BIGINT
from sqlalchemy.orm import declarative_base, sessionmaker, declarative_mixin, Session

Base = declarative_base()


@declarative_mixin
class BaseMixin(object):
    id = Column(INT, primary_key=True)

    engine = create_engine('postgresql://belhard:belhard@0.0.0.0:5432/bh35d')
    _Session = sessionmaker(bind=engine)

    @staticmethod
    def create_session(func):
        def wrapper(*args, **kwargs):
            with BaseMixin._Session() as session:
                return func(*args, **kwargs, session=session)

        return wrapper

    @create_session
    def save(self, session: Session = None) -> None:
        session.add(self)
        session.commit()
        session.refresh(self)

    @classmethod
    @create_session
    def get(cls, pk, session: Session = None) -> Base | None:
        return session.get(cls, pk)

    @classmethod
    @create_session
    def all(cls, order_by: str = 'id', session: Session = None, **kwargs) -> list[Base]:
        return session.scalars(
            select(cls)
            .filter_by(**kwargs)
            .order_by(order_by)
        ).all()

    @create_session
    def delete(self, session: Session = None):
        session.delete(self)
        session.commit()


class Category(BaseMixin, Base):
    __tablename__ = 'categories'

    name = Column(VARCHAR(64), nullable=False, unique=True)

    def __str__(self):
        return self.name


class Product(BaseMixin, Base):
    __tablename__ = 'products'

    name = Column(VARCHAR(64), nullable=False)
    price = Column(DECIMAL(8, 2), default=1)
    is_published = Column(BOOLEAN, default=False)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)

    def __str__(self):
        return self.name


class User(BaseMixin, Base):
    __tablename__ = 'users'

    id = Column(BIGINT, primary_key=True)
    email = Column(VARCHAR(32), nullable=False, unique=True)
    name = Column(VARCHAR(32), nullable=False)

    def __str__(self):
        return self.email


# if __name__ == '__main__':
#
#     data = {
#         'name': 'petya',
#         'email': 'petya@gmail.com'
#     }
#
#     user = User(**data)
#     try:
#         user.save()
#     except IntegrityError:
#         print('email is not unique')
#     else:
#         print(f'register done {user.id}')
# category = Category(name='Very Cool Category')
# category.save()
# print(category.id, category.name)
# category = Category.get(pk=21)
# print(category)

# category.delete()
# categories = Product.all(order_by='name', category_id=1)
# print(categories)
# category.name = 'Category Cool'
# category.save()

# with Session() as session:
# session.execute(
#     update(Product)
#     .values(name='PRODUCT')
#     .where(Product.id == 1)
# )
# session.commit()
# product = session.get(Product, 1)
# product.price = 250.0
# session.add(product)
# session.commit()
# print(product.name)
# session.delete(product)
# session.commit()
# session.execute(
#     delete(Product)
#     .where(Product.is_published == False)
# )
# session.commit()
# query = session.execute(
#     select(Product, Category)
#     .join(Category)
#     .where(Product.is_published == True)
# )
# query = query.all()
# for product, category in query:
#     print(product.name, category.name)
