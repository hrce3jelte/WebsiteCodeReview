import  json, os
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    #init method expects that all the varibales are valid
    def __init__(self, FirstName, LastName, Email, PassWord):
        self.Email = Email
        self.FirstName = FirstName
        self.LastName = LastName
        self.SetPassword(PassWord)

    def __repr__(self):
        return ("{}".format(self.Email))

    def WriteToFile(self):
        #adds a new user to the file
        User = [{"Email" : self.Email, "FirstName" : self.FirstName, "LastName" : self.LastName, "PassWord" : self.PWHash}]
        with open("Users.txt", "r+") as f:
            if(os.stat("Users.txt").st_size==0):
                #this is initial list so this won't glitch
                Jelte = [[{"Email" : self.Email, "FirstName" : self.FirstName, "LastName" : self.LastName, "PassWord" : self.PWHash}]]
            else:
                Users = json.load(f)
                print(Users)
                Jelte = Users
                Jelte.append(User)
                print(Jelte)

        with open("Users.txt", "w") as f:
            json.dump(Jelte, f)

    def SetPassword(self, PassWord):
        self.PWHash = generate_password_hash(PassWord)

    @classmethod
    def CheckPassword(cls, AccountPassWord, InputPassWord):
        return check_password_hash(AccountPassWord, InputPassWord)
    @classmethod
    def CheckForEmailLogin(self, Email):
        with open("Users.txt", "r") as f:
            if (os.stat("Users.txt").st_size == 0):
                return False
            JsonLoad = json.load(f)
            for User in JsonLoad:
                if (User[0]["Email"] == Email):
                    return User
            return False

    @classmethod
    def CheckIfEmailExists(cls, Email):
        with open("Users.txt", "r") as f:
            if(os.stat("Users.txt").st_size == 0):
                return True
            JsonLoad = json.load(f)
            for User in JsonLoad:
                if(User[0]["Email"] == Email):
                    return False
            return True

    @classmethod
    def LogIn(cls, PassWord, Email):
        User = cls.CheckForEmailLogin(Email)
        if(User):
            if(cls.CheckPassword(User[0]['PassWord'], PassWord)):
                return True
        return False

    @classmethod
    def GetUserByEmail(cls, Email):
        with open("Users.txt", "r")  as f:
            List = json.load(f)
            for SearchUser in List:
                if SearchUser[0]["Email"] == Email:
                    return User(SearchUser[0]["FirstName"], SearchUser[0]["LastName"], SearchUser[0 ]["Email"], "123")
