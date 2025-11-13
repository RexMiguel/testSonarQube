#!/usr/bin/env python3
import os
import sys
import subprocess

def unsafe_eval():
    # vulnerabilidad: eval de input sin sanitizar → RCE
    expr = input("Enter an expression to evaluate: ")
    result = eval(expr)
    print(f"Result: {result}")

def unsafe_command():
    # vulnerabilidad: construcción de comando con input directo → command injection
    user_dir = input("Enter directory to list: ")
    cmd = f"ls {user_dir}"
    subprocess.call(cmd, shell=True)
    print("Done listing")

def unsafe_file_read():
    # vulnerabilidad: path traversal posible
    file_path = input("Enter filename to view: ")
    with open(file_path, 'r') as f:
        data = f.read()
    print(data)

def main():
    print("Choose action:")
    print("1) Eval expression")
    print("2) List directory")
    print("3) Read file")
    choice = input("> ")
    if choice == '1':
        unsafe_eval()
    elif choice == '2':
        unsafe_command()
    elif choice == '3':
        unsafe_file_read()
    else:
        print("Unknown option")
        sys.exit(1)

if __name__ == "__main__":
    main()
