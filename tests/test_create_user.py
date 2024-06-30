import pytest
from methods import Methods as method
from data_static import TextServerResponse as text
from helpers import TestCreatorData as data
import allure


@allure.suite('Проверка создания пользователя.')
class TestCreateUser:

    @allure.title('Проверка создания пользователя с полным набором валидных данных.')
    @allure.description('''Направляем запрос на создание пользователя с полным набором валидных данных, генерируемых helpers.
                        Созданного пользователя удаляем из базы после теста. В ответе проверяем код и тело ответа.''')
    def test_create_user_successful(self):
        response = method.create_user(data.data_user_full())

        assert response.status_code == 200 and text.TRUE in response.text

        method.delete_user(response)

    @allure.title('Проверка создания пользователя с неполным набором валидных данных.')
    @allure.description('''Направляем запрос на создание пользователя с неполным набором валидных данных, генерируемых helpers.
                        Используя параметризацию проверяем результат при отправке запроса без заполнения каждого из обязательных полей
                        В ответе проверяем код и тело ответа.''')
    @pytest.mark.parametrize('data_user', [data.data_user_without_email(),
                                           data.data_user_without_password(),
                                           data.data_user_without_name()])
    def test_create_user_without_nesessary_data_fail(self, data_user):
        response = method.create_user(data_user)

        assert response.status_code == 403
        assert text.FALSE in response.text and response.json()['message'] == text.NOT_NESESSARY_USER_DATA

    @allure.title('Проверка создания пользователя с данными, существующего пользователя.')
    @allure.description('''Поочередно направляем два запроса на создание пользователя с одинаковым набором валидных данных, генерируемых helpers.
                        Созданного первого пользователя удаляем из базы после теста. В ответе проверяем код и тело ответа.''')
    def test_create_exist_user_fail_fail(self):
        data_user = data.data_user_full()
        response_first_user = method.create_user(data_user)
        response_second_user = method.create_user(data_user)

        assert response_second_user.status_code == 403
        assert text.FALSE in response_second_user.text and response_second_user.json()['message'] == text.USER_ALREADY_EXISTS

        method.delete_user(response_first_user)
