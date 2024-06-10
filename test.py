from datetime import datetime 

now = datetime.now() 

current_time = now.strftime("%H:%M:%S") 
print("Время сейчас =", current_time)
