import sqlite3
from api.handlers.user_handler import UserHandler
from repository.user_sqlite_repository import UserSqliteRepository
from usecase.user_usecase import UserUseCase

con = sqlite3.connect('tmp/sqlite.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
               (id text, name text, email text, password text, created_at text, updated_at text, deleted_at text)''')
con.commit()


userMemoryRepositry = UserSqliteRepository(con)
userUseCase = UserUseCase(userMemoryRepositry)
userHandler = UserHandler(userUseCase)