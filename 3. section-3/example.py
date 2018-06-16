# Garbage collection---------------------------------------------------
import ctypes, gc

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return 'Object exists'
    return 'Not Found'

class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))

gc.disable()    # Stopping the Garbage collector
my_var = A()

print(hex(id(my_var)))
print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))

a_id = id(my_var)
b_id = id(my_var.b)

print(ref_count(a_id)) # 1
print(ref_count(b_id)) # 1

print(object_by_id(a_id))  # 'Object exists'
print(object_by_id(b_id))  # 'Object exists'

my_var = None

print(ref_count(a_id)) # 1
print(ref_count(b_id)) # 1

print(object_by_id(a_id))  # 'Object exists'
print(object_by_id(b_id))  # 'Object exists'

gc.collect()

print(object_by_id(a_id))  # 'Not Found'
print(object_by_id(b_id))  # 'Not Found'

# ------------------------------------------------------------------------
