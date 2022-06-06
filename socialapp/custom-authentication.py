from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
class EmailAuthBackend(object):
     #Authenticate using an e-mail address
    def authenticate(self,request,username=None,password=None):  #here authenticate is used used to authenticate
        try:
            user=User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExit:
            return None
    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExit:
            return None