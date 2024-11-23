from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class UnitOfWork:

    def __init__(self):
        # we obtain a session factory object
        self.session_maker = sessionmaker(
            bind=create_engine('sqlite:///orders.db')
        )

    def __enter__(self):
        self.session = self.session_maker()  # we open a new database session
        return self  # We return an instance of the unit of work object

    def __exit__(self, exc_type, exc_val, traceback):  # On existing the context, we have access to any exception
        # raised during the context's execution
        if exc_type is not None:  # We check whether an exception took place
            self.rollback()  # if an exception took place, roll back the transaction
            self.session.close()  # we close the database session
        self.session.close()

    def commit(self):
        self.session.commit()  # Wrapper around SQLAlchemy's commit() method

    def rollback(self):
        self.session.rollback()  # Wrapper around SQLAlchemy rollback() method


# We get an instance of the orders repository passing in the UnitOfWork's session.

with UnitOfWork() as unit_of_work:  # we enter the unit of work context
    repo = OrderRepository(unit_of_work.session)
    orders_service = OrdersService(
        repo)  # we get an instance of the OrderService class passing in the orders repository object
    orders_service.place_order(order_details)  # we place an order
    unit_of_work.commit()  # we commit the transaction
