class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >=3:
            self._name = name
        else: 
            raise ValueError("Coffee must be a string of at least 3 characters.")
        self._orders = []

    @property
    def name(self):
        return self._name
        
    def orders(self):
        return self._orders 
    
    def customers(self):
        return list({order.customer for order in self._orders})
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if len(self._orders) == 0:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders) 

class Customer:
    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        
    def orders(self):
        return self._orders
    
    def coffees(self):
        return list({order.coffee for order in self._orders})
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price 
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        if hasattr(customer, 'name') and isinstance(customer, Customer):
            self._customer = customer
        else:
            raise ValueError("Customer must be an instance of Customer.")
        if hasattr(coffee, 'name') and isinstance(coffee, Coffee):
            self._coffee = coffee 
        else:
            raise ValueError("Coffee musr be an instance of Coffee.")
        
        self._coffee._orders.append(self)
        self._customer._orders.append(self)
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
