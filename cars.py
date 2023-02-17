car ={
    "model1" : "ford",
    "year" : "1998",
    "colour" : "blue",
    "country" : "kenya"
}



#accessing dictionaries items
print(car["country"])


profile ={}
profile["username"]  = "user123"
profile["age"] = 20


print(profile)

profile = {}


def register ():

    user_name = input("enter username")
    user_email = input("enter email")
    password = input("enter password")
    


    profile["username"]  = user_name
    profile["email"] = user_email
    profile["password"] = password




def get_profile():
    #print the user_profile
    print(profile)

def change_username():

    new_username = input("enter new username: ")
    profile ["username"] = new_username

register()
get_profile()  

change_username()
get_profile()


register()    
get_profile()



