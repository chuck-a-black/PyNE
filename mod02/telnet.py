import pexpect

# Define our telnet command prompt
session = pexpect.spawn('telnet 192.18.1.30', timeout=10)

# Tell pexpect that we expect a 'Username' prompt, or a timeout
result = session.expect(['Username:',pexpect.TIMEOUT])

# Check if something went wrong with our connection, probably timeout
if result != 0:
    print 'Telnet connection failed, expected Username.'
    exit()

# If we got the Username prompt, proceed to log in
session.sendline('cisco')      # username is 'cisco'
session.expect('Password:')    # expect device to ask for password
session.sendline('cisco')      # password is also 'cisco'
session.expect('#')            # prompt should be a '#'

print 'Telnet connection successful!'

