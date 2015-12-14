import pexpect
ping = pexpect.spawn('ping -c 5 localhost')
ping.expect([pexpect.EOF,pexpect.TIMEOUT])
print(ping.before)
