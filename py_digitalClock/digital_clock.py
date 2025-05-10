import sys 
import pyttsx3  # Add this import at the top of your file
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
import json  # Add this import at the top of your file

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        #self.reminders = self.loadReminders()  # Load reminders during initialization
        self.initUI()


    def loadReminders(self):
        # Load reminders from the JSON file
        try:
            with open('reminders.json', 'r') as file:
                reminders = json.load(file)
                print("Reminders loaded successfully:", reminders)
                return reminders
        except FileNotFoundError:
            print("reminders.json file not found. Please create the file with valid reminders.")
            return {}
        except json.JSONDecodeError:
            print("Error decoding reminders.json. Please ensure it contains valid JSON.")
            return {}
        except Exception as e:
            print(f"An error occurred while loading reminders: {e}")
            return {}
        

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 200, 100)

        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 150px; font-family: 'Courier New'; color: hsl(111, 100%, 50%);")
        self.setStyleSheet("background-color: black;")
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

        # Timer to update the clock every second
        timer = QTimer(self)
        timer.timeout.connect(self.updateClock)
        timer.start(1000)

        
        # Timer to check reminders every minute
        reminder_timer = QTimer(self)
        reminder_timer.timeout.connect(self.checkReminders)
        reminder_timer.start(60000)  # 60,000 milliseconds = 1 minute


        # Initial clock update
        self.updateClock()

    def updateClock(self):
        current_time = QTime.currentTime()
        time_string = current_time.toString('hh:mm:ss AP')
        self.label.setText(time_string)
        

    def checkReminders(self):
        # INCLUDE A dict which takes task name and time, description and reads out the description once the time is reached
        # This function can be implemented to check for reminders and notify the user
        # For now, it will just print a message
        # Example reminder check (this should be replaced with actual logic)
         self.reminders = self.loadReminders()  # Load reminders during initialization
         current_time = QTime.currentTime().toString('hh:mm AP')
         
         for task, time in self.reminders.items():
             #print(f"Checking reminder for {task} at {time}")
             # Check if the current time matches the reminder time
             if current_time == time:
                 
                 engine = pyttsx3.init()
                 message = f"Reminder: {task} at {time}"
                 print(message)
                 # Use the text-to-speech engine to read out the reminder
                 engine.say(message)
                 engine.runAndWait()
             else:
                 print(f"---------------------------------  No reminders at {current_time}")
                 pass
        # This is a placeholder for the reminder check logic
        # In a real application, you would check against a list of reminders and notify the user accordingly
        # For now, we will just print a message to the console
        # print("Checking reminders...")
        # This is a placeholder for the reminder check logic

        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
# This code creates a simple digital clock using PyQt5.