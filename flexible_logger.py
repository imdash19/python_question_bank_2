# Create a “Logger” function that accepts a mandatory message string, followed by an unknown number of positional arguments (*args), and an unknown number of keyword arguments (**kwargs). The function should print the message, then list the extra arguments and metadata.

def logger(message, *args, **kwargs):
    print("Message:", message)

    print("Extra Arguments:")
    for arg in args:
        print(arg)

    print("Metadata:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


logger(
    "Application started",
    "User logged in",
    "Session active",
    user="Bibhuti",
    level="INFO",
    status="Success"
)
