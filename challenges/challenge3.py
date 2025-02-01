class ProtectedSection:
    exception = Exception(None)
    
    def __init__(self, log=(), suppress=()):
        self.log = log
        self.suppress = suppress

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            return True
        elif exc_type in self.log:
            self.exception = exc_val
            return True
        elif exc_type in self.suppress:
            return True
        return False

    

