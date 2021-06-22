from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///delivery_company2.db")
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    phone_number = Column(Integer, nullable=False)
    email = Column(String, nullable=False)

    address = relationship("Address", back_populates="customers")
    packages = relationship("Packages", back_populates="customers")


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(30), nullable=False)
    number = Column(Integer, nullable=False)
    postal_code = Column(Integer, nullable=False)
    city = Column(String(30), nullable=False)
    id_customer = Column(Integer, ForeignKey('customers.id'), nullable=False)

    customers = relationship("Customer", back_populates="address")
    packages = relationship("Packages", back_populates="address")


class Packages(Base):
    __tablename__ = "package"
    id = Column(Integer, primary_key=True, autoincrement=True)
    delivery_date = Column(Date, nullable=False)
    id_address = Column(Integer, ForeignKey("address.id"), nullable=False)

    customers = relationship("Customer", back_populates="package")
    address = relationship("Address", back_populates="package")


Base.metadata.create_all(engine)
