from methods import Methods as method
from data_static import TextServerResponse as text
from helpers import TestCreatorData as data
import allure


@allure.suite('Получение заказов пользователя')
class TestGetOrder:

    @allure.title('Проверка получения заказов пользователя авторизованным пользователем.')
    @allure.description('''Направляем запрос на создание и авторизацию пользователя. Получив токен авторизации, направляем запрос
                        на создание заказа. После чего, с тем же токеном авторизации, направляем запрос на получение заказов пользователя. 
                        Созданного пользователя удаляем из базы после теста. В ответе проверяем код и тело ответа.''')
    def test_get_orders_by_authorized_user(self):
        response_user = method.create_and_login_user()
        token = {"Authorization": response_user.json()['accessToken']}
        response_order = method.create_order(data.set_ingredients_with_correct_hash(), token)
        response = method.get_user_orders(token)

        assert response.status_code == 200
        assert response_order.json()['order']['number'] == response.json()['orders'][0]['number']

        method.delete_user(response_user)

    @allure.title('Проверка невозможности получения заказов пользователя не авторизованным пользователем.')
    @allure.description('''Направляем запрос на  на получение заказов пользователя без указания токена авторизации. 
                        В ответе проверяем код и тело ответа.''')
    def test_get_orders_by_unauthorized_user(self):
        response = method.get_user_orders(token=None)
        assert response.status_code == 401 and response.json()['message'] == text.UNAUTHORIZED_USER
