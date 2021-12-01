import stonks

while True:
    text = input('stonks >>> ')
    if text.strip() == "": continue
    result, error = stonks.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(result.elements)
            print(repr(result))