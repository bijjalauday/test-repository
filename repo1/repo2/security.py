from user1 import User




def authenticate(username,password):
    user=User.findbyusername(username)
    if user and user.password==password:
        return user
def identity(payload):
    userid=payload['identity']
    return User.findbyid(userid)