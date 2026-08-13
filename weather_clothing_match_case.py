# Write a Python program using match-case to suggest what to wear based on the weather.
# If the weather is hot, suggest light clothes.
# If the weather is cold, suggest wearing a jacket.
# If the weather is rainy, suggest carrying an umbrella.

weather = input().lower()

match weather:
    case "hot":
        print("Wear light clothes.")
    case "cold":
        print("Wear a jacket.")
    case "rainy":
        print("Carry an umbrella.")
    case _:
        print("Weather not recognized.")
