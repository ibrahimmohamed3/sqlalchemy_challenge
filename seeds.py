# Make the restaurant instances
restaurant1 = Restaurant(name="Kempinsky", price=2)
restaurant2 = Restaurant(name="Hilton", price=3)
restaurant3 = Restaurant(name ="Abondoz", price=7)
restaurant4 = Restaurant(name="Metlab", price=6)

session.add(restaurant1)
session.add(restaurant2)

# Create some customers instances
customer1 = Customer(first_name="Ibrahim", last_name="Moh")
customer2 = Customer(first_name="Zlatan", last_name="Admin")


#create the sessions
session.add(customer1)
session.add(customer2)

session.add(customer3)
session.add(customer4)

session.commit()
