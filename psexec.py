from pypsexec.client import Client
import sys
from maskpass import askpass

if len(sys.argv) < 5:
    print("Usage: psexec.py [server] [executable] [arguments] [username]")
    sys.exit(0)

server = sys.argv[1]
executable = sys.argv[2]
username = sys.argv[4]
arguments = sys.argv[3]
password = askpass(prompt = "Enter your Password: ", mask = '*')

#commandlist = command.split(" ")

#server = "pek1-gpcmg-001.gopaycorp.com.cn"
#username = "micshi"
#password = ''
#executable = "whoami.exe"
#arguments = "/all"

c = Client(server, username=username, password=password,
           encrypt=True)

c.connect()
try:
    c.create_service()
    if arguments != "null":
        result = c.run_executable(executable, arguments=arguments)
    elif arguments == "null":
        result = c.run_executable(executable)
finally:
    c.remove_service()
    c.disconnect()

print("STDOUT:\n%s" % result[0].decode('utf-8') if result[0] else "")
print("STDERR:\n%s" % result[1].decode('utf-8') if result[1] else "")
print("RC: %d" % result[2])