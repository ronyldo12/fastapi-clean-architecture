import argparse
from application.appllication import userUseCase
from domain.user_create_parameters import UserCreateParamaters

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--name', action='store', type=str, required=True)
my_parser.add_argument('--email', action='store', type=str, required=True)
my_parser.add_argument('--password', action='store', type=str, required=True)

args = my_parser.parse_args()

userCreateParameters = UserCreateParamaters()

userCreateParameters.name = args.name
userCreateParameters.email = args.email
userCreateParameters.password = args.password

user = userUseCase.create(userCreateParameters)
print(user.id)