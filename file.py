import sys
global stdout_backup
global log_file
def writeToFile(filename):
    global stdout_backup
    global log_file
    stdout_backup = sys.stdout
    log_file = open(filename, "w")
    sys.stdout = log_file
    
def closeFile():
    global stdout_backup
    global log_file
    log_file.close()
    sys.stdout = stdout_backup
