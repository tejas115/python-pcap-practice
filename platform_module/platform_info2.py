import platform

def ask_user_info(spec):
    # clean and normalize the input
    spec = spec.strip().lower()

    if spec == 'os': 
        return (platform.system())
    elif spec == 'architecture':
        return (platform.machine())
    elif spec == 'python':
        return (platform.python_version())
    else:
        return "Sorry we couldn't answer your query"

print("Depending on your input we can show relevant info")
inp = input("Enter one of the words in [OS, architecture, python]: ")
print(ask_user_info(inp))
