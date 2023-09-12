import sqlalchemy

metadata = sqlalchemy.MetaData()  # create a metadata object

# Define a table (name of the table, followed by the metadata object)
# Then we list all the columns
post = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("publication_date", sqlalchemy.DateTime(), nullable=False),
    sqlalchemy.Column("title", sqlalchemy.String(length=255), nullable=False),
    sqlalchemy.Column("content", sqlalchemy.Text(), nullable=False),
)
