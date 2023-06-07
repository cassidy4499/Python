hour = int(input("Starting time (hour): ")) 
mins = int(input("Starting time (minutes): ")) 
duration = int(input("Event duration (minutes): "))

mins = mins + duration # find a total of all minutes 
hour = hour + (mins // 60) # add how many hrs in the new mins var
mins = mins % 60 # make minutes fall b/t 0 and 59
hour = hour % 24 # make hours fall b/t 0 and 23

print(hour, ":", mins, sep='')
