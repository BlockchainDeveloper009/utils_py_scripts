import subprocess
"""
############################
# 
# Reference: https://stackoverflow.com/questions/37238645/how-to-open-external-programs-in-python
############################

"""
list_of_programs = [

'C:\Program Files\Mozi)lla Firefox\\firefox.exe',
''


]


subprocess.call(['C:\Program Files\Mozi)lla Firefox\\firefox.exe'])

subprocess.call()



def call_process_bacnkend():
    subprocess.Popen(['C:\Program Files\Mozilla Firefox\\firefox.exe', '-new-tab'])