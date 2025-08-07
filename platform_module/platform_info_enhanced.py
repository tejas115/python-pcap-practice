import platform

def ask_user_info(spec):
    info_map = {
        'os': ('Operating System', platform.system),
        'architecture': ('Architecture', platform.machine),
        'python': ('Python Version', platform.python_version)
    }
    
    spec = spec.strip().lower()
    
    if spec in info_map:
        label, func = info_map[spec]
        return f"{label}: {func()}"
    else:
        available = ', '.join(info_map.keys())
        return f"Invalid input. Available options: {available}"

def main():
    print("System Information Tool")
    print("-" * 30)
    
    while True:
        inp = input("Enter [OS, architecture, python] or 'quit' to exit: ")
        
        if inp.lower() == 'quit':
            print("Goodbye!")
            break
            
        result = ask_user_info(inp)
        print(result)
        print()  # Empty line for better readability

if __name__ == "__main__":
    main()