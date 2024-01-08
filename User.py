from datetime import datetime


class User:
    def __init__(self, id, email, password, creation_date, last_login, account_type):
        self.__user_id = id
        self.__email = email
        self.__password = password
        self.__creationDate = creation_date
        self.__lastLogin = last_login
        self.__account_type = account_type

    def get_user_id(self):
        return self.__user_id

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_last_login(self):
        return self.__lastLogin

    def get_account_type(self):
        return self.__account_type

    def get_creation_date(self):
        return self.__creationDate.strftime("%d/%m/%Y %H:%M:%S")

    def get_notifications(self):
        return self.__notifications

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_last_login(self, last_login):
        self.__lastLogin = last_login

    def set_account_type(self, account_type):
        self.__account_type = account_type

    def set_creation_date(self, creation_date):
        self.__creationDate = creation_date


class Customer(User):
    def __init__(self, id, firstname, lastname, email, password, dob, contactnumber):
        now = datetime.now()
        account_type = 'Customer'
        super().__init__(id, email, password, now, now, account_type)
        self.__firstName = firstname
        self.__lastName = lastname
        self.__points = 0
        self.__deliveryAddress = {}
        self.__billingAddress = {}
        self.__orders = []
        self.__cart = []
        self.__points = 0
        self.__dob = dob
        self.__contactnumber = contactnumber

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob

    def get_contactnumber(self):
        return self.__contactnumber

    def set_contactnumber(self, contactnumber):
        self.__contactnumber = contactnumber

    def get_first_name(self):
        return self.__firstName

    def set_first_name(self, firstname):
        self.__firstName = firstname

    def get_last_name(self):
        return self.__lastName

    def set_last_name(self, lastname):
        self.__lastName = lastname

    def get_points(self):
        return self.__points

    def set_points(self, points):
        self.__points = points

    def get_delivery_address(self):
        return self.__deliveryAddress

    def set_delivery_address(self, deliveryAddress):
        self.__deliveryAddress = deliveryAddress

    def get_billing_address(self):
        return self.__billingAddress

    def set_billing_address(self, billingAddress):
        self.__billingAddress = billingAddress

    def get_orders(self):
        return self.__orders

    def set_orders(self, orders):
        self.__orders = orders

    def get_cart(self):
        return self.__cart

    def set_cart(self, cart):
        self.__cart = cart

    def get_points(self):
        return self.__points

    def set_points(self, points):
        self.__points = points


class Admin(User):
    def __init__(self, id, email, password):
        now = datetime.now()
        account_type = 'Admin'
        super().__init__(id, email, password, now, now, account_type)


class Staff(User):
    def __init__(self, id, email, password):
        now = datetime.now()
        account_type = 'Staff'
        super().__init__(id, email, password, now, now, account_type)
