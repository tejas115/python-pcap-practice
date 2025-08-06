import platform

def ask_user_info(spec):
    # Dictionary to map user input to platform information
    info_map = {
        'os': platform.system(),
        'architecture': platform.machine(),
        'python': platform.python_version()
    }

    # Clean and normalize the input
    spec = spec.strip().lower()
    # Return the requested information or an error message
    if spec in info_map:
        return info_map[spec]() # Call the function to get the value
    else:
        return "Sorry we couldn't answer your query"
    
# This code retrieves and prints the platform information based on user input.
print("Depending on your input we can show relevant info")
inp = input("Enter one of the words in [OS, architecture, python]: ")
print(ask_user_info(inp))
