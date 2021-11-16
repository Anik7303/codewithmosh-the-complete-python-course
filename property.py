class Product:
    def __init__(self, value):
        # self.set_price(value)
        self.price = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative')
        self.__price = value

    # price = property(get_price, set_price)


try:
    product = Product(10)
    print(product.price)
    product.price = 30
    print(product.price)
except Exception as error:
    print(error)
else:
    print('else block executed')
finally:
    print('try/catch block execution finished')
