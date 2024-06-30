from methods import Methods as method
from data_static import TextServerResponse as text
from helpers import TestCreatorData as data
import allure


@allure.suite('Авторизация пользователя')
class TestLoginUser:

    @allure.title('Проверка успешной авторизации пользователя с валидными данными.')
    @allure.description('''Направляем запрос на создание пользователя пользователя с валидными данными, генерируемыми helpers,
                        далее направляем запрос на авторизацию этого пользователя.
                        Созданного пользователя удаляем из базы после теста.
                        В ответе проверяем код и тело ответа.''')
    def test_login_user_successful(self):
        data_user = data.data_user_full()
        response_user = method.create_user(data_user)
        response = method.login_user(data_user)
        assert response.status_code == 200 and text.TRUE in response.text
        method.delete_user(response_user)

    @allure.title('Проверка невозможности авторизации пользователя с неверными данными.')
    @allure.description('''Без предварительной регистрации пользователя, направляем запрос на авторизацию пользователя
                        с данными, генерируемыми helpers. В ответе проверяем код и тело ответа.''')
    def test_login_with_wrong_data_fail(self):
        response = method.login_user(data.data_user_without_name())
        assert response.status_code == 401
        assert text.FALSE in response.text and response.json()['message'] == text.INCORRECT_USER_DATA
