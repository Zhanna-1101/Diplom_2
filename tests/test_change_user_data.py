import pytest
from methods import Methods as method
from data_static import TextServerResponse as text
from helpers import TestCreatorData as data
import allure


@allure.suite('Изменение данных пользователя')
class TestChangeUserData:

    @allure.title('Проверка успешного изменения данных пользователя авторизованным пользователем.')
    @allure.description('''Направляем запрос на создание и авторизацию пользователя. Получив токен авторизации,
                        с помощию параметризации проверяем возможность изменения данных пользователя в полях:
                        'email', 'password', 'name'. Созданного пользователя удаляем из базы после теста.
                        В ответе проверяем код и тело ответа.''')
    @pytest.mark.parametrize('data_user', [{'email': data.data_user_full()['email']},
                                           {'password': data.data_user_full()['password']},
                                           {'name': data.data_user_full()['name']}])
    def test_change_user_data_by_authorized_user_successful(self, data_user):
        response_user = method.create_and_login_user()
        token = {"Authorization": response_user.json()['accessToken']}
        response = method.change_user_data(data_user, token)

        assert response.status_code == 200 and text.TRUE in response.text

        method.delete_user(response_user)

    @allure.title('Проверка невозможности изменения данных пользователя неавторизованным пользователем.')
    @allure.description('''Направляем запрос на  изменения данных пользователя в полях: 'email', 'password', 'name'.
                        В ответе проверяем код и тело ответа.''')
    @pytest.mark.parametrize('data_user', [{'email': data.data_user_full()['email']},
                                           {'password': data.data_user_full()['password']},
                                           {'name': data.data_user_full()['name']}])
    def test_change_user_data_by_unauthorized_user_fail(self, data_user):
        token = None
        response = method.change_user_data(data_user, token)

        assert response.status_code == 401
        assert text.FALSE in response.text and response.json()['message'] == text.UNAUTHORIZED_USER
