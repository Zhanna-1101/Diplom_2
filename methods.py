import requests
from helpers import TestCreatorData as data
from data_static import Urls as url
import allure


class Methods:

    @staticmethod
    @allure.step('Создание и авторизация пользователя')
    def create_and_login_user():
        payload = data.data_user_full()
        requests.post(url.CREATE_USER, data=payload)
        del payload['name']
        response = requests.post(url.LOGIN_USER, data=payload)
        return response

    @staticmethod
    @allure.step('Создание пользователя')
    def create_user(data_user):
        payload = data_user
        response = requests.post(url.CREATE_USER, data=payload)
        return response

    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_user(data_user):
        payload = data_user
        del payload['name']
        response = requests.post(url.LOGIN_USER, data=payload)
        return response

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(response):
        token = {"Authorization": response.json()['accessToken']}
        requests.delete(url.DELETE_USER, headers=token)

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(data_order, token):
        payload = data_order
        response = requests.post(url.CREATE_ORDER, headers=token, data=payload)
        return response

    @staticmethod
    @allure.step('Изменение данных пользователя')
    def change_user_data(data_user, token):
        payload = data_user
        response = requests.patch(url.CHANGE_USER_DATA, headers=token, data=payload)
        return response

    @staticmethod
    @allure.step('Получение заказов пользователя')
    def get_user_orders(token):
        response = requests.get(url.GET_USER_ORDERS, headers=token)
        return response
