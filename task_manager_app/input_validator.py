def get_valid_string(prompt):
    value = input(prompt).strip()
    while not value:
        print("Input cannot be empty. Please try again.")
        value = input(prompt).strip()
    return value

def get_valid_priority():
    priorities = ["low", "medium", "high"]
    value = input("Enter priority (low/medium/high): ").strip().lower()
    while value not in priorities:
        print("Invalid priority! Please enter low, medium, or high.")
        value = input("Enter priority (low/medium/high): ").strip().lower()
    return value
