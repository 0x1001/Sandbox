# Old class style
class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

class Foo(Borg):
    def __init__(self,aaa):
        Borg.__init__(self)
        self.aaa = aaa

# New class style
class BorgNew(object):
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

class FooNew(BorgNew):
    def __init__(self,aaa):
        super(FooNew,self).__init__()
        self.aaa = aaa

if __name__ == "__main__":
    print "Old class style:"
    foo = Foo("aaa")
    print foo.aaa
    foo2 = Foo("bbb")

    print foo.aaa
    print foo2.aaa

    print "New class style:"
    fooNew = FooNew("aaa")
    print fooNew.aaa
    fooNew2 = FooNew("bbb")

    print fooNew.aaa
    print fooNew2.aaa