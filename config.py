from sqlalchemy import create_engine

database_url = "postgresql+psycopg://postgres:1234@localhost:5432/agristat"
engine = create_engine(database_url)