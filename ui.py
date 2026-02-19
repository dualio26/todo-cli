import os

def clear_screen():
    print("\033[2J", end="")
    print("\033[H", end="")

def save_cursor():
    print("\033[s", end="")

def restore_cursor():
    print("\033[u", end="")

def move_cursor(row, col):
    print(f"\033[{row};{col}H", end="")

