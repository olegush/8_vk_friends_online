import vk
import getpass


APP_ID = 6729213
APP_V = 5.87


def get_user_login():
    return input('Login: ')


def get_user_password():
    return getpass.getpass(prompt='Password: ', stream=None)


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, v=APP_V)
    friends_online = api.users.get(user_ids=api.friends.getOnline())
    return friends_online


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print('{} {}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    print('Your friends online:')
    output_friends_to_console(friends_online)
