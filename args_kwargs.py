def argument_test(required, *args, **kwargs):
    print(required)

    if args:
        print(args)

    if kwargs:
        print(kwargs)

if __name__ == '__main__':
    # argument_test() # Error
    argument_test('args test', 1, 2, 3, 4)
    print("\n")
    argument_test('kwargs test', filename1='readme.txt', filename2='test.zip', filename3='deleteme.jpg')
    print("\n")
    argument_test('args and kwargs test', 1, 2, 3, 4, team_name='helloworld', team_code='9900', team_member=12)
