import datetime

def generate_bat_file(servers):
    today = datetime.datetime.now().strftime("%d%m%Y")
    output_file = f"Monitoring_{today}.bat"
    bat_content = f"""@echo off
setlocal

rem Get the current date in DDMMYYYY format
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (
    set DAY=%%a
    set MONTH=%%b
    set YEAR=%%c
)
set DATE=%DAY%%MONTH%%YEAR%

rem Define output file with date
set OUTPUT_FILE=MONITORING_%DATE%.txt

"""

    for i, server in enumerate(servers, start=1):
        bat_content += f"""
rem Define variables for Server {i}
set SSH_USER{i}={server['user']}
set SSH_PASSWORD{i}={server['password']}
set SSH_HOST{i}={server['host']}
set SSH_COMMAND{i}="{server['command']}"

rem Write information to output file
echo Server IP: %SSH_HOST{i}% >> %OUTPUT_FILE%
echo ================================================= >> %OUTPUT_FILE%
echo. >> %OUTPUT_FILE%
echo Output of %SSH_COMMAND{i}% command: >> %OUTPUT_FILE%
echo ================================================= >> %OUTPUT_FILE%
echo. >> %OUTPUT_FILE%
plink -batch -ssh %SSH_USER{i}%@%SSH_HOST{i}% -pw %SSH_PASSWORD{i}% %SSH_COMMAND{i}% >> %OUTPUT_FILE%
echo ================================================= >> %OUTPUT_FILE%
echo. >> %OUTPUT_FILE%
echo Output saved to %OUTPUT_FILE%.
"""

    bat_content += """
endlocal
"""
    with open(output_file, 'w') as file:
        file.write(bat_content)
    print(f"Batch file '{output_file}' has been created.")

# Ask user for number of iterations
iterations = int(input("Enter the number of iterations: "))

# Collect input for each iteration
servers = []
for i in range(1, iterations + 1):
    print(f"Enter details for server {i}:")
    ssh_user = input("Enter SSH username: ")
    ssh_password = input("Enter SSH password: ")
    ssh_host = input("Enter SSH host: ")
    ssh_command = input("Enter SSH tail command: ")
    servers.append({
        "user": ssh_user,
        "password": ssh_password,
        "host": ssh_host,
        "command": ssh_command
    })

# Generate the batch file
generate_bat_file(servers)
