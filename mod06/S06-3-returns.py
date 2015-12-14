import pexpect

#-----------------------------------------------------------
# The following code connects to a device

def connect(dev_ip,username,password):

    print '--- attempting to: ssh '+username+'@'+dev_ip

    session = pexpect.spawn('ssh '+username+'@'+dev_ip, timeout=20)
    result = session.expect(['password:', pexpect.TIMEOUT])

    # Check for failure
    if result != 0:
        print '--- Timout or unexpected reply from device'
        return 0

    print '--- attempting to: password: '+password

    # Successfully got password prompt, logging in with password
    session.sendline(password)
    session.expect('#')

    return session  # return pexpect session object to caller

#-----------------------------------------------------------
# The following function gets and returns interface information

def show_int_brief(session):
    print '--- show interface brief command'
    session.sendline('show interface brief')
    result = session.expect('#')

    print '--- getting interface command output'
    show_int_brief_output = session.before

    return show_int_brief_output

#------------------------------------------------------------
# Main program: connect to device, show interface, display

session = connect('10.0.0.1','cisco','cisco')
if session == 0:
    print '--- Session attempt unsuccessful, exiting.'
    exit()

output_data = show_int_brief(session)

print ''
print 'Show Interface Output'
print '-----------------------------------------------------'
print ''

print output_data

session.sendline('quit')
session.kill(0)
