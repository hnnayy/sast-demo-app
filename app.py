import subprocess
def greet(name):
    print(f"Hello, {name}!")
    
# Lebih aman menggunakan subprocess tanpa shell=True
def run_command(cmd_args):
    try:
        subprocess.run(cmd_args, shell=False, check=True)
    except subprocess.SubprocessError as e:
        print(f"Error executing command: {e}")

if __name__ == "__main__":  # Perbaiki sintaksis
    name = input("Enter your name: ")
    greet(name)
    
    # Validasi atau batasi perintah yang dijalankan
    # Ini hanya contoh, Anda perlu implementasi yang lebih aman
    allowed_commands = ["ls", "dir", "echo"]
    cmd = input("Enter a command to run (only 'ls', 'dir', or 'echo' allowed): ")
    if cmd.split()[0] in allowed_commands:
        run_command(cmd.split())
    else:
        print("Command not allowed")
