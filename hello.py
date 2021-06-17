import cffi 

ffi = cffi.FFI() 
ffi.cdef("void cffi_hello(char *name);") 
C = ffi.dlopen("./libhello.so") 

def hello(name):
	C.cffi_hello(name) 


if __name__ == "__main__":
	hello("cffi")


