import ctypes

#hllDll = ctypes.WinDLL("..\\volume_change\\Debug\\volume_change.dll")
#hllDll = ctypes.windll.LoadLibrary("..\\volume_change\\Debug\\volume_change.dll")
hllDll = ctypes.cdll.LoadLibrary("..\\volume_change\\Debug\\volume_change.dll")

print(hllDll.test_1())

data_1 = b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'
data_2 = b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'

volume_1 = 0.1
volume_2 = 0.1

buffer = b'\0' * (len(data_1))
buffer_c = ctypes.create_string_buffer(buffer)
buffer_size_c = ctypes.c_int()

volume_1_c = ctypes.c_float(volume_1)
volume_2_c = ctypes.c_float(volume_2)

hllDll.change_volume(data_1, data_2, len(data_1), volume_1_c, volume_2_c, buffer_c, buffer_size_c)