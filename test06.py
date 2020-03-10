#--coding utf-8--
class Data(object):
    def __init__(self):
        self.__education = "education "

    def getData(self):
        print("in Data")
class Time(object):
    def getTime(self):
        print("in Time")
class DataAndTime(Data,Time):
    pass


if __name__=='__main__':
    data = Data()
    #time = Time()
    #data.getData()
    #time.getTime()
    #time.getData()
    data_and_time = DataAndTime()
    data_and_time.getData()
    print(DataAndTime.mro())
    print(data._Data__education)
