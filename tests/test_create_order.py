from methods import Methods as method
from data_static import TextServerResponse as text
from helpers import TestCreatorData as data
import allure


@allure.suite('Создание заказа')
class TestCreateOrders:

    @allure.title('Проверка создания заказа авторизованным пользователем с полным набором валидных данных.')
    @allure.description('''Направляем запрос на создание и авторизацию пользователя. Получив токен авторизации, направляем запрос
                        на создание заказа с полным набором валидных данных (хэш ингредиентов), генерируемых helpers.
                        Созданного пользователя удаляем из базы после теста. В ответе проверяем код и тело ответа.''')
    def test_create_order_by_authorized_user_successful(self):
        response_user = method.create_and_login_user()
        token = {"Authorization": response_user.json()['accessToken']}
        response = method.create_order(data.set_ingredients_with_correct_hash(), token)

        assert response.status_code == 200 and text.TRUE in response.text

        method.delete_user(response_user)

    @allure.title('Проверка создания заказа неавторизованным пользователем с полным набором валидных данных.')
    @allure.description('''Направляем запрос на создание заказа с полным набором валидных данных (хэш ингредиентов),
                        генерируемых helpers, без токена авторизации. В ответе проверяем код и тело ответа.''')
    def test_create_order_by_unauthorized_user_successful(self):
        token = None
        response = method.create_order(data.set_ingredients_with_correct_hash(), token)

        assert response.status_code == 200 and text.TRUE in response.text

    @allure.title('Проверка создания заказа с набором невалидных данных.')
    @allure.description('''Направляем запрос на создание заказа с набором невалидных данных (хэш ингредиентов),
                        генерируемых helpers. В ответе проверяем код и тело ответа.''')
    def test_create_order_with_invalid_hash_ingredients_fail(self):
        token = None
        response = method.create_order(data.set_ingredients_with_incorrect_hash(), token)

        assert response.status_code == 500 and text.INTERNAL_SERVER_ERROR in response.text

    @allure.title('Проверка создания заказа без данных.')
    @allure.description('''Направляем запрос на создание заказа без данных данных (без указания хэша ингредиентов),
                        генерируемых helpers. В ответе проверяем код и тело ответа.''')
    def test_create_order_without_hash_ingredients_fail(self):
        token = None
        response = method.create_order(data.empty_set_ingredients(), token)

        assert response.status_code == 400
        assert text.FALSE in response.text and response.json()['message'] == text.ORDER_WITHOUT_INGREDIENTS
