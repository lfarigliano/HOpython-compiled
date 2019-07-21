import ctypes as C
import numpy as np
math = C.CDLL('./libdinpy.so')
math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]
print(math.add_float(3, 4))
tres = C.c_int(3)
cuatro = C.c_int(4)
res = C.c_int()
math.add_int_ref(C.byref(tres),C.byref(cuatro),C.byref(res))
print(res.value)
intp = C.POINTER(C.c_int)
in1 = np.array([1, 2, -5], dtype=C.c_int)
in2 = np.array([-1, 3, 3], dtype=C.c_int)
out = np.zeros(3, dtype=np.float16)
math.add_int_array(in1.ctypes.data_as(flp),in2.ctypes.data_as(flp),out.ctypes.data_as(flp),C.c_int(3))
print (array([ 0, 5, -2], dtype=int32))
