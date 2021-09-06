class Airline:
    __destination= ' '
    __flight_number= ' '
    __airplane= ' '
    __departure_time= ' '
    __day= ' '

    def __init__(self, destination0, flight_number0, airplane0, departure_time0, day0):
        self.__destination = destination0
        self.__flight_number = flight_number0
        self.__airplane = airplane0
        self.__departure_time = departure_time0
        self.__day = day0
        print ('New object created!')


    def get_destination(self):
        return self.__destination
    def get_flight_number(self):
        return self.__flight_number
    def get_airplane(self):
        return self.__airplane
    def get_departure_time(self):
        return self.__departure_time
    def get_day(self):
        return self.__day

    def flight_list_for_destination(i):
        print ('destination: ' + flight_list[i].get_destination())
        print ('flight_number: ' + flight_list[i].get_flight_number())
        print ('airplane: ' + flight_list[i].get_airplane())
        print ('departure_time: ' + flight_list[i].get_departure_time())
        print ('day: ' + flight_list[i].get_day())
        print ('----------------')

i=0
flight_list = [Flight ('Berlin', '1212', 'Boeing-747', '09:00', 'Monday'),
               Flight ('Minsk', '1313', 'Boeing-747', '09:30', 'Monday'),
               Flight ('Moskau', '1414', 'Boeing-777', '09:00', 'Sunday'),
               Flight ('Kiev', '1515', 'Boeing-777', '09:30', 'Sunday'),
               Flight ('Francfurt', '2121', 'Airbus A310', '10:00', 'Wednesday'),
               Flight ('Berlin', '1616', 'Airbus A310' '10:00', 'Wednesday'),
               Flight ('St.Peterburg', '1717', 'Boeing-747', '10:30', 'Friday'),
               Flight ('Kiev', '1818', 'Boeing-747', '10:15', 'Friday'),
               Flight ('London', '1919', 'Airbus A320', '10:15', 'Friday'),
               Flight ('Berlin', '1111', 'Airbus A310', '09:00', 'Thursday'),
               Flight ('London', '1010', 'Boeing-747', '12:30', 'Monday')


destination = int(input('Введите пункт назначения: \n') # с этого момента почему-то ошибка
                  
while i < len(flight_list):
    if flight_list[i].get_destination() == destination:
        flight_list_for_destination(i)
        i +=1

day = input('Введите день недели: \n')
                  
while i < len(flight_list):
    if flight_list[i].get_day() == day:
        flight_list_for_day(i)
        i +=1
