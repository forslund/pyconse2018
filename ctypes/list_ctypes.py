import ctypes


class element(ctypes.Structure):
    pass

#Do this to be able to point to same type
element._fields_ = [
        ('value', ctypes.POINTER(ctypes.c_int)),
        ('next', ctypes.POINTER(element))
]


# Load the library
clist = ctypes.CDLL('../lib/liblinkedlist.so')

# Define returns and arguments for functions
clist.new_list.restype = ctypes.POINTER(element)
clist.append_val.argtypes = (ctypes.POINTER(element), ctypes.c_int)
clist.get_element_indexed.restype = ctypes.POINTER(element)


my_list = clist.new_list()
clist.append_val(my_list, 7)
clist.append_val(my_list, 17)
clist.append_val(my_list, 27)

print(clist.get_element_indexed(my_list, 2)[0].value[0])
