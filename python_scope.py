#global scope
my_global = 10

def fn1():
    local_v = 5
    print('Access to global', my_global)

# print('Can\'t access local scope ', local_v)
# fn1()


def fn2():
    enclosed_v = 6
    def fn3():
        local_v = 4
        print("Access to Global variable ", my_global)
        print('Access to enclosed', enclosed_v)

    fn3()

fn2()