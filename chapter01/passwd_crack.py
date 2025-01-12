from crypt import crypt


def test_pass(crypt_pass):
    salt = crypt_pass[:2]
    print(salt)
    dict_file = open('dictionary.txt', 'r')

    for word in dict_file.readlines():
        crypt_word = crypt(word.strip('\n'), salt)
        print(crypt_word)
        if crypt_word == crypt_pass:
            print(f'[+] Found Password: {word}\n')
            return

    print('[-] Password Not Found.\n')
    return


if __name__ == '__main__':
    pass_file = open('passwords.txt')
    for line in pass_file.readlines():
        if ':' in line:
            # get username
            user = line.split(':')[0]
            # get hashed password
            _crypt_pass = line.split(':')[1].strip()
            print(f'[*] Cracking Password For: {user}')
            test_pass(_crypt_pass)
