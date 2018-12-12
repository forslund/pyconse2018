from os.path import dirname, join, abspath
from cffi import FFI


ffi = FFI()

libdir = abspath(join(dirname(__file__), '../lib/'))

ffi.cdef(open(join(libdir, 'linked_list.h')).read())

ffi.set_source('llist._llist', '#include <linked_list.h>',
        library_dirs=[libdir],
        include_dirs=[libdir],
        libraries=['list'],
        runtime_library_dirs=[libdir])
ffi.compile(verbose=True)
