potery add alembic
poetry  add psycopg2-binary
poetry run alembic init alembic
model define / scema define 
alembic ini file key add 
env.py set matadata and import

uv run alembic revision --autogenerate -m "create todos table"
uv run alembic upgrade head