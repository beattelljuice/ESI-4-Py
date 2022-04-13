from ESI4Py import esiobject_base
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def example():

    input(" - Press Enter To Start - ")
    print("Lets Define Some Variables:")
    ClientID = ""
    SecretKey = ""
    CallbackURL = ""
    Scopes = ""
    ValidationState = ""
    print("Variables Defined")

    # Define the base object
    print("Lets call the object and start")
    input(" - Press Enter To Continue - ")
    ESI_OBJECT_BASE = esiobject_base(ClientID, SecretKey, CallbackURL, Scopes, ValidationState)
    print("Object has been called!")

    # Load From already obtained refresh token - UNCOMMENT BELOW TO ENABLE
    #My_Refresh_Token = "cmduaac5OEStLj78ZcFIhQ==" # fill out if you have a refresh token on hand; used to illustrate Refresh token loading
    #print("Lets Manually load in a refresh token")
    #input(" - Press Enter To Continue - ")
    #ESI_OBJECT_BASE.LOADRefreshToken(My_Refresh_Token)

    # Get and set auth Code
    print("Go to the link below and get your auth code (From the code parameter in your url)")
    print(ESI_OBJECT_BASE.returnRedirectURL())
    print(ESI_OBJECT_BASE.analyse_auth_code(input(" Enter Code >>>")))

    input(" - Press Enter To Continue - ")

    # Test out retreiving the access token
    print("Retreiving the access token")
    input(" - Press Enter To Continue - ")
    print(ESI_OBJECT_BASE.retreive_access_token())

    print("Lets repeat it to see if we get a different access code if we try again")
    input(" - Press Enter To Continue - ")
    print(ESI_OBJECT_BASE.retreive_access_token())

    print("What? We didnt get a new access code! That was because of the builtin feature detecting we still had a valid token stored, lets reset that real quick")
    input(" - Press Enter To Continue - ")
    ESI_OBJECT_BASE.manual_reset_access_token_expiry_time()

    print("We just reset the expiry time to 10 secconds (roughly) in the past. Now the program will thing the token has expired and generate a new one")
    input(" - Press Enter To Continue - ")
    print(ESI_OBJECT_BASE.retreive_access_token())

    print("Lets repeat that for consistency!")
    input(" - Press Enter To Continue - ")
    print(ESI_OBJECT_BASE.retreive_access_token())

    print("Is this token Valid? "+str(ESI_OBJECT_BASE.is_access_token_valid()))
    input(" - Press Enter To Continue - ")

    print("Lets decode the access token to retreive more information")
    input(" - Press Enter To Continue - ")
    print(ESI_OBJECT_BASE.decode_jwt())

    print("Tutorial Finished!")
    input(" - Press Enter To Finish - ")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    example()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
