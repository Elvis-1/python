httpStatus = 503

if httpStatus == 200 or httpStatus == 201:
    print('Success')
elif httpStatus == 400:
    print('Bad Request')
elif httpStatus == 404:
    print('Not Found')
elif httpStatus == 500 | 501:
    print('Server Error')
else:
    print('Unknown Error')


# switch
match httpStatus:
    case 200 | 201:
      print('Success')
    case 400:
      print('Bad Request')
    case 404:
      print('Not Found')
    case 500 | 501:
      print('Server Error')
    case _:
      print('Unknown Error')


 

