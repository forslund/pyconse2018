from os.path import dirname, join
from cffi import FFI


libdir = join(dirname(__file__), '../lib/')

ffi = FFI()
header = """
typedef struct {
    int *val;
    void *next;
} element_t;

element_t * new_element(void);

element_t * new_list(void);

void append_val(element_t *list, int val);

element_t *get_element_indexed(element_t * list, int index);
"""

ffi.cdef(header)

linked_list = ffi.dlopen(join(libdir, 'liblist.so'))
my_list = linked_list.new_list()

linked_list.append_val(my_list, 12)
linked_list.append_val(my_list, 5)
