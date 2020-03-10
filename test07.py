#--coding utf-8 --
class Employee(object):
    def __init__(self,firstname,lastname,salary = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def __int__(self):
        return self.salary

    def __str__(self):
        return "full name:"+self.firstname+' ' +self.lastname



if __name__=='__main__':
    employee = Employee('peter','fei',20000)
    print(employee)
    print(int(employee))

