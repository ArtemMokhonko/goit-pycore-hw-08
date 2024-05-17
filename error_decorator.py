from custom_errors import BirthdayError, PhoneError, NameError

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == 'show_phone':
                return "Give me name"
            if func.__name__ == "add_birthday":
                return "Required name and date of birth"
            if func.__name__ == "show_birthday":
                return "Required name "
            else:
                return "Give me name and phone please"
        except KeyError:
            return "Contact not found."
        except BirthdayError as e:
            return e
        except PhoneError as phone:
            return phone
        except NameError as name:
            return name
        except Exception as error:
            return f"An unexpected error occurred: {error}"
    return inner