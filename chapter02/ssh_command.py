import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before.decode('utf-8'))


def connect(host, user, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    conn_str = f'ssh {user}@{host}'
    child = pexpect.spawn(conn_str)
    print(f'Connecting...')
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])

    if not ret:
        print('[-] Error Connecting')
        return
    else:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
        if not ret:
            print('[-] Error Connecting')
            return
    print(f'Sending Password...')
    child.sendline(password)
    child.expect(PROMPT)
    print(f'Sending Command...')
    return child


if __name__ == '__main__':
    tgt_host = 'localhost'
    tgt_user = 'parsa'
    tgt_passwd = '1234'

    conn = connect(tgt_host, tgt_user, tgt_passwd)
    # destruct the remote using alias cd=rm -rf if needed
    send_command(conn, """echo "alias cd='echo what if i set rm -rf as an alias for cd?, kidding i would never do that'" >> ~/.bashrc && source ~/.bashrc""")
    # remember to use "unalias cd" after this practice to regain normal cd usage