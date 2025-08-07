import platform

def platform_info():
    user_os = platform.system()
    user_arch = platform.machine()
    user_python = platform.python_version()

    return f"OS: {user_os}, Architecture: {user_arch}, Python Version: {user_python}"

# This code retrieves and prints the platform information including OS, architecture, and Python version.
print(platform_info())



