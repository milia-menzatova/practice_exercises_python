def exceptionHandling():
    try:
       car = {'make': 'bmw', 'model': '550j', 'year': '2016'}
       print(car["color"])
    except:
       print("Key not found")
    finally:
       print("Please try a different key")

exceptionHandling()