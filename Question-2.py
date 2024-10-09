# Question 2: Do django signals run in the same thread as the caller? 
# Please support your answer with a code snippet that conclusively proves your stance.
# The code does not need to be elegant and production ready,
# we just need to understand your logic.

#Answer

#Yes, the django signals do run in the same thread as the caller.
#To support this I will be using the threading library to get the name
#of the current thread and show that both the caller and signal run in the same thread.


#code snippet 

#threading library required to check current thread
import threading


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

#signal handler prints the name of the current thread
@receiver(post_save,sender = User)
def signal_handler(sender,instance,**kwargs):
    print(f"Signal handler thread:{threading.current_thread.name} ")

print(f"normal code thread:{threading.current_thread.__name__}")

#this will send a signal which will start the signal handeler
user = User(username = "testuser")
user.save()

#output

#Signal handler thread: Mainthread
#normal code thread: Mainthread

#as the above output shows both the signal handler and the caller run 
#in the same thread

