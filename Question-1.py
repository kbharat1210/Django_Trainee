#Question 1: By default are django signals executed synchronously or asynchronously? 
#Please support your answer with a code snippet that conclusively proves your stance. 
#The code does not need to be elegant and production ready, we just need to understand your logic.

#Answer

#By default django signals are executed synchronously i.e when a signal is sent the signal handler 
#is executed immediately and all the other processes wait for the signal handler to complete before 
#executing.

#In the below example I'm sending a signal and then having a time delay in it before it finishes
#After it i've written some random print whic when run will only execute after the signal handler 
#is executed

#code snippet

#importing required modules
from django.db.models.signals import post_save
from django.dispatch import receiver    
from django.contrib.auth.models import User

#used to initiate delay in the signal handler function
import time

#defining the signal receiver  and the basic function where a start signal is printed and then after a wait
#the finish signal is printed
@receiver(post_save,sender=User)
def signal_handler(user,instance,**kwargs):
    print("start signal handler")
    time.sleep(3)
    print("finish signal handler")


#a instance of the user is saved which will make a signal to be sent starting the signal handler
user = User(username = testuser)
user.save()

#this statement will only be printed after the the first two statements are printed with some delay 
#in between them
print('statement after save')

#the output statement should be 
#start signal handler
#3 sec delay
#finish signal handler
#statement after save

#this shows that the djnago signals are executed synchronously as the main print statement
#waits for the signal handler to be completed before being executed.

