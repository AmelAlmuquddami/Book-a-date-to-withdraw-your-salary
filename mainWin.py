from tkinter import *
from tkcalendar import *
import csv
from tkinter import messagebox
import shortuuid

# this time i will use CSV files as away to learn how to work with them ( better use is database) -> learn soon
# this file to save booked dates , date_user code (uuid number) , user name
PATH = "datescodes.csv"


def main_page(client_name):
    """
    # lay down the Canvas , window  title , title Icon using Tkinter as my Module
    # label to welcome th user , call the book date function

    """
    main_win = Tk()
    main_win.title("Book A Date To Withdraw Your Salary")
    main_win.geometry("500x500")
    main_win.iconbitmap("Money.ico")
    make_label(main_win, "Welcome {}.".format(client_name.capitalize()), 0, 0)
    book_date(main_win, client_name)
    main_win.mainloop()


def book_date(parent, client_name):
    """

    :param parent: tk window
    :param client_name: user name
    :return: put a date selector and button to book it
    """
    cal = Calendar(parent,selectmode="day", year=2020, month=5)
    cal.grid(row=2, column=2, padx=20, pady=40,)
    make_label(parent, "Select A date", 1, 2)
    make_button(parent, "Book A Date", 30, 3, 2, cal, client_name)


def make_label(parent, caption, row, column):
    """
            use function to make label and put it on window grid
    """
    input_title = Label(parent, text=caption)
    input_title.grid(row=row, column=column, padx=5, pady=5)


def make_button(parent, caption, width, row, column,  entry, client_name):
    """
            use function to make book date  buttons and put it on window grid
    """
    submit_data = Button(parent, text=caption, command=lambda: book_date_button(entry, parent, client_name),
                         padx=5, pady=5, width=width,)
    submit_data.grid(row=row, column=column, padx=5, pady=5, columnspan=2)
    return submit_data


def book_date_button(entry, parent, client_name):
    """
          this runs when you click on the book date button
          stores the picked date into a variable
          puts date and code on the window
          call generate code function
          call store date_and_code function
    """

    selected_date = entry.get_date()
    make_label(parent, "Your Next Date is : " + selected_date, 4, 2)
    withdraw_code = generate_code(selected_date)
    make_label(parent, "Your Identifier Code is : " + str(withdraw_code), 5, 2)
    store_date_and_code(selected_date, withdraw_code, client_name)


def store_date_and_code(selected_date, withdraw_code, client_name):
    """
    stores selected date , code , user name in csv file
    and show a message box giving the user his next date
    """
    with open(PATH, 'a', newline='') as file:
        if selected_date != '' and withdraw_code != '':
            writer = csv.writer(file)
            writer.writerow([selected_date, withdraw_code, client_name])
            messagebox.showinfo("Completed", "You book Your Next date on: " + str(selected_date))


def generate_code(d):
    """
    :param d: selected date to use it in generating date code
    :return: unique id (code)  of each booked date
    """
    date_to_string = str(d).replace('/', '')
    uuid_number = shortuuid.ShortUUID().random(length=10)
    final_id = date_to_string + uuid_number
    return final_id

