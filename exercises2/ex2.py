from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///cinematic3.db")
Base = declarative_base()


class Directors(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    rating = Column(Integer, nullable=False)

    movies = relationship("Movies", back_populates="directors")

    def __repr__(self):
        return self.name + " " + self.surname


class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    category = Column(String(30), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    director_id = Column(Integer, ForeignKey("directors.id"), nullable=False)

    directors = relationship("Directors", back_populates="movies")  # odniesienie do atrybutu klasy


Base.metadata.create_all(engine)
