__author__ = 'aravindan'

"""All objects are refernce-counted,An object's referce count is increased whenever it's assigned to a new name or placed in a conatiner such as a list,tuple,or dict as shown below"""

a=37     #creates an object with value 37
b=a      #Increases reference count on 37
c=[]
c.append(b)  # increases reference count on 37