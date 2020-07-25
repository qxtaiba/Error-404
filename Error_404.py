import webbrowser

try:
    raise ValueError('invalid syntax')xw
except Exception as exception:
 
    webbrowser.open_new("http://stackoverflow.com/search?q=+"+ type(exception).__name__ + " "+ exception.message)
