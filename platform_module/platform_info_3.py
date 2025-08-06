import platform

def ask_user_info(spec):
    info_map = {
        'os': platform.system,
        'architecture': platform.machine, 
        'python': platform.python_version
    }
    
    spec = spec.strip().lower()
    
    # ✅ Check if key exists BEFORE accessing
    if spec in info_map:
        return info_map[spec]()  # Safe to call now
    else:
        return "Sorry we couldn't answer your query"

print("Depending on your input we can show relevant info")
inp = input("Enter one of the words [OS, architecture, python]: ")
print(ask_user_info(inp))
