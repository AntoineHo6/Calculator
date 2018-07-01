"""
Calculator that makes basic equations

Author: Antoine Ho
Date: 2018/06/12

References: https://stackoverflow.com/questions/1740726/turn-string-into-operator
Icon link: http://www.iconarchive.com/show/ios7-icons-by-icons8/Science-Math-icon.html

"""
from tkinter import *

import operator

import py2exe


class MainWindow:
    """ This class is the calculator window that holds everything """

    def __init__(self, master):

        # Window Title
        master.title('Math')

        try:
            master.wm_iconbitmap('.\math.ico')
        except:
            pass

        self.display_font = ("Verdana", 20)
        self.font = ("Arial", 11)

        # String, that is displayed
        self.sDisplay_text = ""
        self.sNumbers = ["", ""]
        # Will be the operator on the two numbers in self.sNumbers
        self.sOperator = ""
        # Decides which of the two numbers in self.sNumbers the program has to configure
        # (number_1 refers to self.sNumbers[0])
        self.bChange_number_1 = True

        # Makes string type operators usable in mathematical equations
        self.ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

        # --- FRAMES IN MASTER ---

        # ** Frame to display **
        self.display_frame = Frame(master)
        self.display_frame.pack()
        # ** frame that holds all the buttons **
        self.buttons_frame = Frame(master)
        self.buttons_frame.pack()

        # --- DISPLAY ---

        # ** number display **
        self.display = Label(self.display_frame, text=self.sDisplay_text, width=16, height=5, wraplength=253)
        self.display.configure(relief=SUNKEN, font=self.display_font)
        self.display.pack()

        # --- BUTTONS ---

        # ** Number Buttons **
        button_0 = Button(self.buttons_frame, text="0", width=14, height=3)
        button_0.configure(bg="azure", font=self.font)
        button_0.bind("<Button-1>", self.build_number)
        button_0.grid(row=4, columnspan=2)

        button_1 = Button(self.buttons_frame, text="1", width=6, height=3)
        button_1.configure(bg="azure", font=self.font)
        button_1.bind("<Button-1>", self.build_number)
        button_1.grid(row=3, column=0)

        button_2 = Button(self.buttons_frame, text="2", width=6, height=3)
        button_2.configure(bg="azure", font=self.font)
        button_2.bind("<Button-1>", self.build_number)
        button_2.grid(row=3, column=1)

        button_3 = Button(self.buttons_frame, text="3", width=6, height=3)
        button_3.configure(bg="azure", font=self.font)
        button_3.bind("<Button-1>", self.build_number)
        button_3.grid(row=3, column=2)

        button_4 = Button(self.buttons_frame, text="4", width=6, height=3)
        button_4.configure(bg="azure", font=self.font)
        button_4.bind("<Button-1>", self.build_number)
        button_4.grid(row=2, column=0)

        button_5 = Button(self.buttons_frame, text="5", width=6, height=3)
        button_5.configure(bg="azure", font=self.font)
        button_5.bind("<Button-1>", self.build_number)
        button_5.grid(row=2, column=1)

        button_6 = Button(self.buttons_frame, text="6", width=6, height=3)
        button_6.configure(bg="azure", font=self.font)
        button_6.bind("<Button-1>", self.build_number)
        button_6.grid(row=2, column=2)

        button_7 = Button(self.buttons_frame, text="7", width=6, height=3)
        button_7.configure(bg="azure", font=self.font)
        button_7.bind("<Button-1>", self.build_number)
        button_7.grid(row=1, column=0)

        button_8 = Button(self.buttons_frame, text="8", width=6, height=3)
        button_8.configure(bg="azure", font=self.font)
        button_8.bind("<Button-1>", self.build_number)
        button_8.grid(row=1, column=1)

        button_9 = Button(self.buttons_frame, text="9", width=6, height=3)
        button_9.configure(bg="azure", font=self.font)
        button_9.bind("<Button-1>", self.build_number)
        button_9.grid(row=1, column=2)

        # ** Decimal point Button **
        button_dot = Button(self.buttons_frame, text=".", width=6, height=3)
        button_dot.configure(bg="honeydew", font=self.font)
        button_dot.bind("<Button-1>", self.build_number)
        button_dot.grid(row=4, column=2)

        # ** Clear buttons **
        button_c = Button(self.buttons_frame, command=self.clear, text="C", width=14, height=3)
        button_c.configure(bg="cornsilk", font=self.font)
        button_c.grid(row=0, columnspan=2)

        button_ce = Button(self.buttons_frame, command=self.clear_ce, text="CE", width=6, height=3)
        button_ce.configure(bg="cornsilk", font=self.font)
        button_ce.grid(row=0, column=2)

        # ** Equals button **
        button_equ = Button(self.buttons_frame, command=self.calculate, text="=", width=6, height=3)
        button_equ.configure(bg="alice blue", font=self.font)
        button_equ.grid(row=4, column=3)

        # ** Operator Buttons **
        button_add = Button(self.buttons_frame, text="+", width=6, height=3)
        button_add.configure(bg="linen", font=self.font)
        button_add.bind("<Button-1>", self.build_operator)
        button_add.grid(row=3, column=3)

        button_sub = Button(self.buttons_frame, text="-", width=6, height=3)
        button_sub.configure(bg="linen", font=self.font)
        button_sub.bind("<Button-1>", self.build_operator)
        button_sub.grid(row=2, column=3)

        button_mul = Button(self.buttons_frame, text="*", width=6, height=3)
        button_mul.configure(bg="linen", font=self.font)
        button_mul.bind("<Button-1>", self.build_operator)
        button_mul.grid(row=1, column=3)

        button_div = Button(self.buttons_frame, text="/", width=6, height=3)
        button_div.configure(bg="linen", font=self.font)
        button_div.bind("<Button-1>", self.build_operator)
        button_div.grid(row=0, column=3)

    def replace_display(self, new_display):
        """
        Replaces the string displayed with the argument

        :param new_display:
        :return: None
        """
        self.sDisplay_text = new_display

        # Updates the display
        self.display.config(text=self.sDisplay_text)

    def append_display(self, display_char):
        """
        Appends the argument to the string displayed

        :param display_char:
        :return: None
        """
        self.sDisplay_text += display_char

        # Updates the display
        self.display.config(text=self.sDisplay_text)

    def del_current_number_display(self):
        """
        Deletes the current number that the user is "building" so he can start over from the display

        :return: None
        """
        # Removes the last character of the display str on loop until it hits anything but a number or a decimal point
        while True:
            if self.sDisplay_text[-1:].isdigit() or self.sDisplay_text[-1:] == '.':
                self.sDisplay_text = self.sDisplay_text[:-1]
            else:
                break

        # Updates the display
        self.display.config(text=self.sDisplay_text)

    def build_number(self, event):
        """
        Updates one of the two number variables(self.sNumbers[0]/self.sNumbers[1]) when the user either presses
        on the number buttons or the decimal point button

        :param event:
        :return: None
        """
        # Retrieves the button name(text)
        button_value = event.widget.cget('text')

        if self.bChange_number_1:
            # If user enters decimal point first
            if (self.sNumbers[0] == "" or self.sNumbers[0] == "-") and button_value == ".":
                self.sNumbers[0] += "0."
                self.append_display("0.")
            # This condition avoids duplicate decimal points
            elif "." not in self.sNumbers[0] or button_value != ".":
                self.sNumbers[0] += button_value
                self.append_display(button_value)

        # Does the same things but for the second number variable(self.sNumbers[1])
        else:
            if (self.sNumbers[1] == "" or self.sNumbers[1] == "-") and button_value == ".":
                self.sNumbers[1] += "0."
                self.append_display("0.")
            elif "." not in self.sNumbers[1] or button_value != ".":
                self.sNumbers[1] += button_value
                self.append_display(button_value)

    def build_operator(self, event):
        """
        Deals with operators in a number of ways to create a final comprehensible equation

        :param event:
        :return: None
        """
        # Retrieves the button name(text)
        button_value = event.widget.cget('text')

        # User wants his first number to be negative
        if self.sNumbers[0] == "" and button_value == "-":
            self.sNumbers[0] += "-"
            self.append_display(button_value)
        # Changes the equation operator
        elif (self.sNumbers[0] != "" and self.sNumbers[0] != "-") and self.sNumbers[1] == "":
            # Replaces the current equation operator with the one user just clicked
            if self.sOperator != "":
                self.sDisplay_text = self.sDisplay_text[:-1]
                self.sOperator = button_value
                self.append_display(button_value)
            # Simply adds an operator to the equation because there was none
            else:
                self.bChange_number_1 = False
                self.sOperator = button_value
                self.append_display(button_value)

        # Calculates the equation and adds the operator to the final result
        if self.sOperator != "" and (self.sNumbers[0] != "" and self.sNumbers[1] != ""):
            self.calculate()
            self.sOperator = button_value
            self.append_display(button_value)
            self.bChange_number_1 = False

    def calculate(self):
        """
        Calculates a result with the two number variables(self.sNumbers[0]/self.sNumbers[1])

        :return: None
        """
        numbers = [0, 0]

        try:
            # Removes decimal points from the sNumbers if nothing comes after them ex: "3." become "3"
            for index in range(2):
                if self.sNumbers[index][-1:] == ".":
                    self.sNumbers[index] = self.sNumbers[index][:-1]

                # Store the sNumbers as either int or float
                try:
                    numbers[index] = int(self.sNumbers[index])
                except ValueError:
                    numbers[index] = float(self.sNumbers[index])

            # Calculates the equation
            try:
                result = self.ops[self.sOperator](numbers[0], numbers[1])
                self.clear()
                self.replace_display(str(result))

                # Sets the first index to the result if the user wants to continue to operate on the result
                self.sNumbers[0] = str(result)
            except ZeroDivisionError:
                self.clear()
                self.replace_display("ERROR")

        except ValueError:
            # Here because equation is not complete
            # Equals button will end up doing nothing
            pass

    def clear(self):
        """
        Clears everything back to default values

        :return: None
        """
        self.replace_display("")
        self.sOperator = ""
        self.bChange_number_1 = True

        # Clear sNumbers list
        for index in range(2):
            self.sNumbers[index] = ""

    def clear_ce(self):
        """
        Deletes the current number that the user is "building" so that he can start over

        :return: None
        """
        if self.bChange_number_1:
            self.sNumbers[0] = ""
            self.del_current_number_display()
        else:
            self.sNumbers[1] = ""
            self.del_current_number_display()


root = Tk()

calc_window = MainWindow(root)

root.mainloop()
