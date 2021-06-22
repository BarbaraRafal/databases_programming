from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("postgresql://postgres:password@localhost:5432/film")
Base = declarative_base()


class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    rating = Column(Integer, nullable=False)
    movies = relationship("Movie", back_populates="director")

    def __repr__(self):
        return self.name + " " + self.surname


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), nullable=False)
    category = Column(String(30), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    director_id = Column(Integer, ForeignKey("directors.id", ondelete="CASCADE"), nullable=False)
    director = relationship("Director", back_populates="movies")


Base.metadata.create_all(engine)
