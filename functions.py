def func_test():
    print('test')

func_test()


def func_test_2(user):
    return f'Hi {user}'

print(func_test_2('Abhi'))



def test3(*args,**kwargs):
    print(args)
    print(kwargs)


test3(3,4,5,a=1,b=3)


def test4(*a,**b):
    print(a)
    print(b)
    print(b.items())
    for key,value in b.items():
        print(key,value)

test4(6,7,8,9,r=2,y=5)