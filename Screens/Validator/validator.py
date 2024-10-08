# Date    : 28/09/22 9:06 pm
# Author  : Parmar Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0
import configure
from Screens.Refactor.customWidgets import CustomWidgets
from Screens.Validator.validatorLogic import Validator


def validate_email(**kwargs):
    """
    This is the function which is used to validate the email address when the focus pops out of the entry
    :return: None
    """
    if Validator.validate_email(kwargs['parent'].email_entry.get())[0]:
        # If the email is valid then remove the error label
        kwargs['parent'].email_error_label.destroy()
        # reset the color of the entry to default
        kwargs['parent'].email_entry.configure(border_color=configure.dark_gray)
        return True
    else:
        # checks if the error label is already present or not
        if kwargs['parent'].email_error_label.winfo_exists():
            # If the error label is already present then destroy it
            kwargs['parent'].email_error_label.destroy()
        # Create the custom error label
        kwargs['parent'].email_error_label = CustomWidgets.customErrorLabel(parent=kwargs['parent'].email_frame,
                                                                            error_text=Validator.validate_email(
                                                                                kwargs['parent'].email_entry.get())[1])
        # Place the error label in the grid layout
        kwargs['parent'].email_error_label.grid(row=1, column=0, columnspan=2)
        # Change the color of the entry to dominant color
        kwargs['parent'].email_entry.configure(border_color=configure.light_cyan)
        return False


def validate_enrollment(**kwargs):
    """
    This is the function which is used to validate the email address when the focus pops out of the entry
    :return: None
    """
    if 13 > len(kwargs['parent'].enrollment_entry.get()) > 0:
        # If the email is valid then remove the error label
        if kwargs['parent'].enrollment_error_label.winfo_exists():
            kwargs['parent'].enrollment_error_label.destroy()
        # reset the color of the entry to default
        kwargs['parent'].enrollment_entry.configure(border_color=configure.dark_gray)
        return True
    else:
        # checks if the error label is already present or not
        if kwargs['parent'].enrollment_error_label.winfo_exists():
            # If the error label is already present then destroy it
            kwargs['parent'].enrollment_error_label.destroy()
        # Create the custom error label
        kwargs['parent'].enrollment_error_label = CustomWidgets.customErrorLabel(
            parent=kwargs['parent'].enrollment_frame,
            error_text='Invalid Admin Code/\nApplication No./Enrollment No.')
        # Place the error label in the grid layout
        kwargs['parent'].enrollment_error_label.grid(row=1, column=0, columnspan=2)
        # Change the color of the entry to dominant color
        kwargs['parent'].enrollment_entry.configure(border_color=configure.light_cyan)
        return False


def validate_password(**kwargs):
    """
    This is the function which is used to validate the password when the focus pops out of the entry
    :return: None
    """
    if Validator.validate_password(kwargs['parent'].password_entry.get())[0]:
        # If the password is valid then remove the error label
        if kwargs['parent'].password_error_label.winfo_exists():
            kwargs['parent'].password_error_label.destroy()
        # reset the color of the entry to default
        kwargs['parent'].password_entry.configure(border_color=configure.dark_gray)
        return True
    else:
        # checks if the error label is already present or not
        if kwargs['parent'].password_error_label.winfo_exists():
            # If the error label is already present then destroy it
            kwargs['parent'].password_error_label.destroy()
        # Create the custom error label
        kwargs['parent'].password_error_label = CustomWidgets.customErrorLabel(parent=kwargs['parent'].password_frame,
                                                                               error_text=Validator.validate_password(
                                                                                   kwargs[
                                                                                       'parent'].password_entry.get())[
                                                                                   1])
        # Place the error label in the grid layout
        kwargs['parent'].password_error_label.grid(row=1, column=0, columnspan=2)
        # Change the color of the entry to dominant color
        kwargs['parent'].password_entry.configure(border_color=configure.light_cyan)
        return False
