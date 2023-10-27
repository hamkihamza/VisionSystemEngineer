# Let's do a live exercise. Share your screen so we can see your process as you go. 
# In whatever editing tool you like, in whatever programming language or pseudocode you like, write out a process, a description, of how you would read a file, use it to update
#  a DB table, and then provide a summary report at the end. You can use any resources you like, outside of "phone a friend" ;-). You can ask me any questions you like - I know what I want this process to do, but I haven't given you enough details so far.
# As you write this up, talk about your process - what your questions are, where you can look up previous examples - either your own or others - to copy from. Comment your code, making notes to indicate where you're weaker and where you're stronger, what
#  you're confident about, where you're guessing.
# Ground rules/expectations/limitations: I'm not expecting a working product at the end - there may not even be any lines of working code. But I'd like to see a high-level view of what should be done and what risk areas you see in the task. I realize you've
#  had zero time to prepare for this, so you're not losing any points because you haven't prepared for some part of this. And I'm not really interested in the syntax of any code lines you write - better syntax is better, but I'm giving lots of points for getting
#  close.
# This exercise is time-limited, so we're just going to keep working on it for 15 minutes. However detailed we get during that time, that's how deep we get, and no further. After that, if you'll email Danny with whatever you have written up, good, bad, or
#  indifferent, right after the interview.
 

# CSV of shares and metadata about them: network path to the share, 
# share name, server on which the share lives, GB of data stored in the share, # of files in the share



# CREATE table and Define each Column that is expected to have the data (Network Path, Share Name, Server, GB of Data , # of files)
# Open CSV file
# Use pandas to read contents of the file
# For loop throuhg the CSV file and extract the share
# If Statement, if the share name is in the DB already UPDATE or CREATE a new row for the entry keeping track of the dates Updated
# Break down the share into Network Path, Share Name, Server, GB of Data , # of files 
# Input the Data into the respective SQL, "INSERT" 
# DB.orm("INSERT {localhost/, share#1, Server1, 20GB , 231 Files}")
# write .excel pandas.rows(Field names) pd.Dataseries(Network Path, Share Name, Server, GB of Data , # of files)
# Column Headers : field names
# Rows output: full contents of the database table 
