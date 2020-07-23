#CSC121-0001
#Class Project (main module)
#Austin Willoughby

from customer import Customer

def main():
    print('Customer 1')
    email = input('Enter email address: ')
    customer1 = Customer(email)
    customer1.input_info()
    customer1.verify_info()
    output_file = open('customers.txt', 'w')
    output = customer1.__str__()
    output_file.write(output)


    print('Customer 2')
    email = input('Enter email address: ')
    customer2 = Customer(email)
    customer2.input_info()
    customer2.verify_info()
    output_file = open('customers.txt', 'a')
    output = customer2.__str__()
    output_file.write(output)
    print("Data of two customers written to the file 'customers.txt'.")





main()