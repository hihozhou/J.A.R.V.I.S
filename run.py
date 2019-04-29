def run():
    while True:
        say = input('I ：')
        if say == 'quiet':
            print('Jarvis program exit.')
            break
        else:
            print('J.A.R.V.I.S : Reply "' + say + '"')


if __name__=='__main__':
    run()