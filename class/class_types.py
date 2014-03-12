class aaa: pass
class bbb(object): pass
class caa(aaa): pass
class dbb(bbb): pass

print caa is aaa

print type(caa)
print type(aaa)
print type(dbb)
print type(bbb)

print isinstance(caa,aaa)

print issubclass(caa,aaa)
print issubclass(dbb,bbb)

print issubclass(aaa,caa)