#!/usr/bin/env python3
import subprocess
import os
import tempfile

# VULNERABILITY: Hard-coded secret → regla python:S6418 (Hard-coded secrets are security-sensitive) :contentReference[oaicite:3]{index=3}
API_KEY = "SECRET_API_KEY_12345"

def insecure_eval(user_input):
    # VULNERABILITY: dynamic code execution / injection → regla “Dynamic code execution should not be vulnerable to injection attacks” :contentReference[oaicite:4]{index=4}
    result = eval(user_input)
    print("Eval result:", result)

def insecure_command(user_dir):
    # VULNERABILITY: OS command injection via shell=True → regla “OS commands should not be vulnerable to command injection attacks” :contentReference[oaicite:5]{index=5}
    subprocess.run(f"ls {user_dir}", shell=True)

def insecure_tempfile():
    # VULNERABILITY: insecure temporary file creation without atomic mechanism → I/O path injection / temp file issue :contentReference[oaicite:6]{index=6}
    tempname = os.path.join(tempfile.gettempdir(), "mytmpfile.txt")
    with open(tempname, "w") as f:
        f.write("data")
    print("Created temp file:", tempname)

def path_traversal(file_path):
    # VULNERABILITY: Path injection/traversal via open() → regla “I/O function calls should not be vulnerable to path injection attacks” :contentReference[oaicite:7]{index=7}
    with open(file_path, "r") as f:
        print(f.read())

def main():
    print("Choose option:")
    print("1) eval user input")
    print("2) list directory via insecure command")
    print("3) insecure create tempfile")
    print("4) read file via path traversal")
    choice = input("> ").strip()
    if choice == "1":
        insecure_eval(input("Enter expression: "))
    elif choice == "2":
        insecure_command(input("Enter directory path: "))
    elif choice == "3":
        insecure_tempfile()
    elif choice == "4":
        path_traversal(input("Enter file path: "))
    else:
        print("Unknown option")

if __name__ == "__main__":
    main()
