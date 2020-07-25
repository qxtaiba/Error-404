import webbrowser

try:
    # some code that will raise an exception
    raise ValueError('invalid syntax')

except Exception as e:
 
    webbrowser.open_new("http://stackoverflow.com/search?q=+"+ type(e).__name__ + " "+ e.message)
