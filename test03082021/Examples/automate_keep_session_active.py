import pywinauto

x=50
y=50
app = pywinauto.Application().connect(path='chrome.exe')
app.MainDialog.click_input(coords=(x, y))