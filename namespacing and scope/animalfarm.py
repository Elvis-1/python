def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("Inside nexted function: " + animal)
    print("Before calling nexted funtion: "+ animal)
    e()
    print("After calling nexted function: " + animal)
animal = 'camel'
d()
print("Global variable: "+ animal)

