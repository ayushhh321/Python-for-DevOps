import os  
import datetime  
import shutil  

def backup(source, destination):
    # """
    # Creates a compressed backup of the source directory and saves it in the destination.
    # """
    today = datetime.date.today()  # Get today's date
    backup_file_name = os.path.join(destination, f"backup_{today}")   # backup file ka name will ne destination folder ka name and date and time today ka

    shutil.make_archive(backup_file_name, "zip", source)  # make_archive compress the backup file

# Corrected Paths
source = r"D:\folders\Python for DevOps"  
destination = r"D:\folders\Python for DevOps\backups"  

backup(source, destination)  # Call the function
