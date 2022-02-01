from xml.dom import NotFoundErr
from domain.user import User
from usecase.user_interface import UserRepositoryInteface
from exceptions.not_found_exception import NotFoundException


class UserSqliteRepository(UserRepositoryInteface):

    def __init__(self, con) -> None:
        self.con = con
        super().__init__()

    def create(self,user: User) -> User:
        cur = self.con.cursor()
        cur.execute("INSERT INTO users VALUES ('"+user.id+"','"+user.name+"','"+user.email+"','"+user.password+"','"+user.created_at+"','"+user.created_at+"','"+user.deleted_at+"')")
        self.con.commit()
        return user

    def list(self):
        users = []
        cur = self.con.cursor()
        for user in cur.execute("SELECT * FROM users"):
            userDomain = User()
            userDomain.id = user[0]
            userDomain.name = user[1]
            userDomain.email = user[2]
            userDomain.created_at = user[4]
            userDomain.updated_at = user[5]
            userDomain.deleted_at = user[6]
            users.append(userDomain)
        self.con.commit()
        return users
    
    def get_by_id(self,user_id: str) -> User:
        #ajustar
        raise NotFoundException("user not found")

    def get_by_email(self,email: str) -> User:
        #ajustar
        raise NotFoundException("user not found")
