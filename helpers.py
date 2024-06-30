from faker import Faker
import random
import string
import requests
from data_static import Urls as url


class TestCreatorData:

    # Создаем полный нвбор тестовых данных для регистрации пользователя
    @staticmethod
    def data_user_full():
        data_user = {
            'email': Faker().company_email(),
            'password': Faker().password(),
            'name': Faker(locale='ru_RU').first_name()}
        return data_user

    # Создаем нвбор тестовых данных для регистрации пользователя с пустым полем email
    @staticmethod
    def data_user_without_email():
        data_user = {
            'email': '',
            'password': Faker().password(),
            'name': Faker(locale='ru_RU').first_name()}
        return data_user

    # Создаем нвбор тестовых данных для регистрации пользователя с пустым полем password
    @staticmethod
    def data_user_without_password():
        data_user = {
            'email': Faker().company_email(),
            'password': '',
            'name': Faker(locale='ru_RU').first_name()}
        return data_user

    # Создаем нвбор тестовых данных для регистрации пользователя с пустым полем name
    @staticmethod
    def data_user_without_name():
        data_user = {
            'email': Faker().company_email(),
            'password': Faker().password(),
            'name': ''}
        return data_user

    # Создаем корректный набор тестовых данных для создания заказа
    @staticmethod
    def set_ingredients_with_correct_hash():
        ingredients = []
        response = requests.get(url.GET_INGREDIENTS)
        list = response.json()['data']
        for i in list:
            ingredients.append(i.get('_id'))
        last_index = len(ingredients) - 1
        first_ingredient = ingredients[random.randint(0, last_index)]
        second_ingredient = ingredients[random.randint(0, last_index)]
        correct_set = {"ingredients": [first_ingredient, second_ingredient]}
        return correct_set

    # Создаем набор тестовых данных для создания заказа с некорректным хэшем
    @staticmethod
    def set_ingredients_with_incorrect_hash():
        all_symbols = string.ascii_lowercase + string.digits
        first_hash_ingredient = ''.join(random.choice(all_symbols) for i in range(24))
        second_hash_ingredient = ''.join(random.choice(all_symbols) for i in range(24))
        incorrect_set = {"ingredients": [first_hash_ingredient, second_hash_ingredient]}
        return incorrect_set

    # Создаем пустой набор тестовых данных для создания заказа
    @staticmethod
    def empty_set_ingredients():
        empty_set = {"ingredients": ''}
        return empty_set
