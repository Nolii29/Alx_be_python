#!/usr/bin/env python3

# daily_reminder.py

# Loop to validate user input
while True:
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Validate priority
    if priority not in ("high", "medium", "low"):
        print("Invalid priority. Please enter high, medium, or low.")
        continue

    # Validate time-bound input
    if time_bound not in ("yes", "no"):
        print("Invalid time-bound response. Please enter yes or no.")
        continue

    # Match-case for priority (Python 3.10+)
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a high priority task. Try to complete it as soon as possible.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires attention today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Schedule it when convenient.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task, but it's time-sensitive. Don't delay!")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

    break  # Exit loop after successful input
