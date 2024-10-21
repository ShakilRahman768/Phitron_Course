class Star_Cinema:
    hall_list = []
    def entry_hall(self, hall):
            self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        super().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        seat_serial = [['O' for i in range(self.__cols)] for i in range(self.__rows)]

        self.__show_list.append((id, movie_name, time))
        self.__seats[id] = seat_serial

    def book_seats(self, id, seat_list):
        if id not in self.__seats:
            print(f"'{id}' not found.")
            return

        seat_serial = self.__seats[id]

        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print(f"({row}, {col}) is not available.")
            elif seat_serial[row][col] == '1':
                print(f"({row}, {col}) is already booked.")
            else:
                seat_serial[row][col] = '1'

    def view_show_list(self):
        if not self.__show_list:
            print("No shows available.")
        else:
            for show in self.__show_list:
                print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id not in self.__seats:
            print(f"'{id}' not found.")
            return

        seat_serial = self.__seats[id]
        print(f"Available seats for show {id}:")
        for row_idx, row in enumerate(seat_serial):
            print(f"Row {row_idx}: {' '.join(row)}")


def cinema_system():
    hall_1 = Hall(5, 5, "Hall 1")
    hall_1.entry_show("101", "Jawan", "10:00 AM")
    hall_1.entry_show("102", "Toofan", "03:00 PM")
    hall_2 = Hall(4, 4, "Hall 2")
    hall_2.entry_show("201", "Aynabaji", "06:00 PM")

    while True:
        print("1. VIEW ALL SHOW TODAY")
        print("2. VIEW AVAILABLE SEATS")
        print("3. BOOK TICKET")
        print("4. Exit")
        choice = input("Enter OPTION: ")

        if choice == '1':
            for hall in Star_Cinema.hall_list:
                print(f"\nShows in {hall._Hall__hall_no}:")
                hall.view_show_list()

        elif choice == '2':
            show_id = input("Enter the Show ID: ")
            found = False
            for hall in Star_Cinema.hall_list:
                if show_id in hall._Hall__seats:
                    hall.view_available_seats(show_id)
                    found = True
                    break
            if not found:
                print(f"'{show_id}' not found in any hall.")

        elif choice == '3':
            show_id = input("Enter the Show ID: ")
            found = False
            for hall in Star_Cinema.hall_list:
                if show_id in hall._Hall__seats:
                    num_seats = int(input("How many seats do you want to book? "))
                    seats = []
                    for i in range(num_seats):
                        row = int(input("Enter seat row: "))
                        col = int(input("Enter seat column: "))
                        seats.append((row, col))
                    hall.book_seats(show_id, seats)
                    found = True
                    break
            if not found:
                print(f"'{show_id}' not found in any hall.")

        elif choice == '4':
            break

        else:
            print("Invalid OPTION.")

cinema_system()
