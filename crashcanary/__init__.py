def init(email):
    import sys

    def canaryexcepthook(exectype, value, tb):
        import traceback
        import urllib.request
        import urllib.parse

        data = {
            'email': email,
            'body': '\n'.join(traceback.format_exception(exectype, value, tb))
        }

        req = urllib.request.Request('http://server.crashcanary.org/crash', urllib.parse.urlencode(data).encode('ascii'))
        with urllib.request.urlopen(req) as response:
            pass

        sys.__excepthook__(exectype, value, tb)

    sys.excepthook = canaryexcepthook
