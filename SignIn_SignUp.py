from tkinter import *
import csv
from tkinter import messagebox
from mainWin import main_page


"""
 Author : Amel Almuqqudami
 Application Goal : Book A date in Bank to withdraw Salary From The Bank
 Back Story : we have a liquidity crisis in libya makes a daily overcrowding in the banks and main streets
 
"""
# this time i will use CSV files as away to learn how to work with them ( better use is database) -> learn soon
PATH = 'userdata.csv'


# lay down the Canvas , App title , title Icon using Tkinter as my Module
root = Tk()
root.title("Book A Date To Withdraw Your Salary")  # give my Project window a title
root.geometry("500x500")  # window size
root.iconbitmap("Money.ico")  # icon beside the title


# Sign Up
def sign_up():
    """
    here i get the new User information
    name, phone number, bank name, bank account, password
    and update my database with new user (sign up form)
    """
    # set up a frame to contain my input fields
    signup_frame = LabelFrame(root, text="Sign Up Form", padx=5, pady=5, bd=3)
    signup_frame.grid(row=2, column=2, padx=130, pady=40,)

    # put my sign up filed names in list to loop through and make label and entry for each
    input_names = ["Full Name", "Bank Name", "Account Number", "Password"]
    entry_list = []
    for i in range(len(input_names)):
        make_label(signup_frame, input_names[i], i, 0)
        entry = make_entry(signup_frame,  20, i, 0, input_names)
        entry_list.append(entry)

    # sign up button
    make_button(signup_frame, "Sign Up", 30, 4, 0, 1, entry_list)


def sign_in():
    """
        here i get the  User information to sign in
        to check if the data is in my csv file i used in check_data_sign_in(entry)
    """
    # set up a frame to contain my input fields
    signup_frame = LabelFrame(root, text="Sign In Form", padx=5, pady=5, bd=3)
    signup_frame.grid(row=4, column=2, padx=130, pady=10, )

    # put my sign up filed names in list to loop through and make label and entry for each
    input_names = ["Full Name", "Password"]
    entry_list = []
    for i in range(len(input_names)):
        make_label(signup_frame, input_names[i], i, 0)
        entry = make_entry(signup_frame, 20, i, 0, input_names)
        entry_list.append(entry)

        # sign in button
    make_button(signup_frame, "Sign In", 30, 4, 0, 2, entry_list)



def make_label(parent, caption, row, column):
    """
        use function to make label and put it on window grid

    """
    input_title = Label(parent, text=caption)
    input_title.grid(row=row, column=column, padx=5, pady=5)


def make_entry(parent, width, row, column, input_names):
    """
            use function to make input filed and put it on window grid
    """
    input_filed = StringVar()
    if input_names[row] == "Password":  # if input filed is Password show * when typing
        data_entry = Entry(parent, width=width, show="*",  textvariable=input_filed)
    else:
        data_entry = Entry(parent, width=width,  textvariable=input_filed)
    data_entry.grid(row=row, column=column+1, padx=5, pady=5)
    return input_filed


def make_button(parent, caption, width, row, column, operation_code, entry):
    """
            use function to make buttons and put it on window grid
    """
    submit_data = Button(parent, text=caption, command=lambda: button_click(entry, operation_code),
                         padx=5, pady=5, width=width,)
    submit_data.grid(row=row, column=column, padx=5, pady=5, columnspan=2)
    return submit_data


def button_click(entry, operation_code):
    """
        this runs when click form button ( sign in or sign up)
        and use operation code to distinguish between which oprtation
        in this case 2 for sign in , 1 for sign up
    """
    if operation_code == 2:
        check_data_sign_in(entry)
    if operation_code == 1:
        add_data_sign_up(entry)
        clear_filed(entry)


def check_data_sign_in(entry):
    """
          this runs when you click on the sign in button
          it checks if the data is in the user data files
          if true it gives you acess to main application window
    """
    with open(PATH) as file:
        reader = csv.reader(file)
        for row in reader:
            user_name = row[0]
            password = row[1]
            if user_name == entry[0].get() and password == entry[1].get():
                root.destroy()
                main_page(entry[0].get())


def add_data_sign_up(entry):
    """
        adds new user to your user database and
         stores it  to csv file
    """

    with open(PATH, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([entry[0].get(), entry[3].get(), entry[1].get(), entry[2].get()])
        messagebox.showinfo("Completed", "You are Signed Up , You Can Sign Now")


sign_up()
sign_in()

root.mainloop()