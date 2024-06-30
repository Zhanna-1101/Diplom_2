class Urls:

    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = f'{MAIN_URL}/api/auth/register'
    LOGIN_USER = f'{MAIN_URL}/api/auth/login'
    CHANGE_USER_DATA = f'{MAIN_URL}/api/auth/user'
    DELETE_USER = f'{MAIN_URL}/api/auth/user'
    CREATE_ORDER = f'{MAIN_URL}/api/orders'
    GET_INGREDIENTS = f'{MAIN_URL}/api/ingredients'
    GET_USER_ORDERS = f'{MAIN_URL}/api/orders'


class TextServerResponse:

    TRUE = 'success":true'
    FALSE = '"success":false'
    USER_ALREADY_EXISTS = 'User already exists'
    INCORRECT_USER_DATA = 'email or password are incorrect'
    NOT_NESESSARY_USER_DATA = 'Email, password and name are required fields'
    UNAUTHORIZED_USER = 'You should be authorised'
    ORDER_WITHOUT_INGREDIENTS = 'Ingredient ids must be provided'
    INTERNAL_SERVER_ERROR = 'Internal Server Error'
