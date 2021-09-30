#classes created for customized exceptions/errors

class RangeError(Exception):		# The name RangeError can be changed, 
    pass				# but the rest MUST be written as is

tot=0
count=0
while True:
  try:
    #error handling for illegal int and
    #custom error handling for negative values
    num= int(input ("Enter a positive integer, 0 to quit: "))
    if num==0:
        break
    elif num<0:
        raise RangeError		# “calling” my custom exception
    else:
        tot+=num
        count+=1

  except ValueError:			# if the checked exception is raised (built-in Python exception)
    print ("Not an integer")
  except RangeError:			# for when my custom exception is raised
    print ("Not a POSITIVE integer")
  except Exception:
    print("Something else went wrong")

#error handling for a division by 0 error (count remains at 0)
try:
  print ("Average is",tot/count)
except ZeroDivisionError:		# another built-in (checked) exception
    print ("No numbers were entered")        
except Exception:
    print("Something else went wrong")


# Another separate example as a definition:
def getInt(prompt):
    while True:
        try:
            x=int(input(prompt))
            return x
        except ValueError:
            print("Not an integer, please try again")


num=getInt("Please enter an integer: ")
print ("Thanks")

