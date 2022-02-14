import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename,'w') as f:
    pass
 
  timestamp = os.path.getmtime(filename)
  tm = datetime.datetime.fromtimestamp(timestamp).date()
  # Convert the timestamp into a readable format, then into a string
  
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(tm))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
