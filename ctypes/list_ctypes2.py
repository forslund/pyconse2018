import ctypes


class element(ctypes.Structure):
    pass

element._fields_ = [
        ('val', ctypes.POINTER(ctypes.c_int)),
        ('next', ctypes.POINTER(element))
    ]


clist = ctypes.CDLL('../lib/liblinkedlist.so')

# Define returns and arguments for functions
clist.new_list.restype = ctypes.POINTER(element)
clist.append_val.argtypes = (ctypes.POINTER(element), ctypes.c_int)
clist.get_element_indexed.argtypes = (ctypes.POINTER(element), ctypes.c_int)
clist.get_element_indexed.restype = ctypes.POINTER(element)


class CList():
    def __init__(self):
        self.l = clist.new_list()

    def append(self, integer):
        clist.append_val(self.l, integer)

    def __len__(self):
        length = 0
        e = self.l
        while e:
            e = e[0].next
            length = length + 1
        return length

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise IndexError('Index must be an integer')
        else:
            return clist.get_element_indexed(self.l, key)[0].val[0]

#   TODO
#    def __del__(self):

