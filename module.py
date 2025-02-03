customer_list = ["Temitayo AdeolaOluwa", "Mike Banning", "Adu Riverson", "Sean Mapeyinda"]
def add_new(name, id):
    customer_list.append(name)

def remove(name):
    customer_list.remove(name)

def all_customer():
    return len(customer_list)
def detailed_list():
    return customer_list