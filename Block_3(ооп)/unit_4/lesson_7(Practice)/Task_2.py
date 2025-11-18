# Напишите декоратор obfuscator
def obfuscator(func):
    def wraper():
        result = dict(func())
        result['name'] = result['name'][0] + '*'*len(result['name'][1:-1]) + result['name'][-1]
        result['password'] = '*'*len(result['password'])
        return result
    return wraper


@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())