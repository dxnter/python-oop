'''
Product

'''
class Product(object):
    def __init__(self, item_name, brand, price, weight):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'For sale'

    def sell(self):
        self.status = 'Sold'
        return self

    def add_tax(self, tax_rate):
        self.price = (self.price * tax_rate) + self.price
        return self

    def return_item(self, return_condition):
        return_condition = return_condition.lower()
        if return_condition == 'defective':
            self.status = 'Defective'
            self.price = 0
        elif return_condition == 'like new':
            self.status = 'For sale'
        elif return_condition == 'used':
            self.status = 'Used'
            self.price = self.price * .8
        return self

    def display_info(self):
        print 'Item Name:',self.item_name
        print 'Brand:',self.brand
        print 'Price: $',self.price
        print 'Weight:',self.weight,'lbs'
        print 'Status:',self.status
'''
Product Input - (Item Name, Brand, Price(int), Weight(int))
Return Condictions - Defective, Like New, Used
'''
bike = Product('Macbook Pro', 'Apple', 2000, 12)

bike.return_item('used').display_info()

