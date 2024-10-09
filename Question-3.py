# Question 3: By default do django signals run in the same database transaction as the caller? 
# Please support your answer with a code snippet that conclusively proves your stance. 
# The code does not need to be elegant and production ready, we just need to understand your logic

#Answer

#Yes, the django signals  do run in the same  database transaction as the caller i.e
#when transaction introduces some changes the database is also updated
#when transactions changes are rolled back the database changes are also reverted.
#To show that this is true we will make use of transactions.atomic() to make some changes 
#and then raise a exception to force a rollback to revert back the changes.
#Because the signals  run in the same database transaction as the caller the database changes
#are also rolled back.  


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

#the signal handler when called makes a change to the username 
#when save is called a databse change is updated 
@receiver(post_save,sender = User)
def signal_changes(sender,instance,**kwargs):
    instance.username = "make change to username"
    instance.save()

#in this code block some changes are made to the user and then rolled back.
#as the transaction.atomic() runs as a single code block when the changes are saved 
#the database is updated and then when we raise a exception and roll it back 
#the database changes are also rolled back.
try:
    with transaction.atomic():
        user = User(username = "original username")
        user.save
        raise Exception("reverse username change")
except:
    pass

#to check whether the changes that were made was rolled back or present
if User.objects.filter(username="make change to username").exists():
    print("username changes were saved")
else:
    print("username change were not saved")

#output
#username change were not saved

#from this we can infer that the  changes that were made by the signal handler
#were reverted when the transaction was also rolled back.

 