# 1. Action Function
# alternative names
# Side Effect funtion
# Command Function
# Handler Funtion
# Service Funtion


# TASK - 1
print("*" * 30)
print("--------TASK - 1 --------")
# stores application log messages in a file whenever an event occurs


def write_log(message):
    with open("CHAPTER-8_python-functions/app.log", "a") as file:
        file.write(message + "\n")


write_log("App Started")
write_log("user logged in")
write_log("App Stopped")
