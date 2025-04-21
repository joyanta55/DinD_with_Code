import os

# Read the environment variable MY_VAR_B set from container B
my_var_value = os.getenv('MY_VAR_B', 'Default Value')  # Default if MY_VAR is not set

print(f"Container C: Hello from Python inside C! The value of MY_VAR_B is: {my_var_value}")

