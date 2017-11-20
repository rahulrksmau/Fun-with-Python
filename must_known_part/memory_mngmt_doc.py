#########------Memory Management of Python------------------#########
"""
    Object and instance are created in heap while variables and methods are created
    in Stack.
    
"""

""" Python is based on dynamic typed variable i.e. every variable declared in Python
    is reference to object.
    Dynamic typed means any variable can be reference to any typed value.
    variables need not to declaration before use this is saves
    lots of developers from getting any error. But have some value if varible is using.
    e.g.
""""

a = 10  #datatype not declared, a is referencing to 10(which is int type, located in heap)
print (id(a), type(a)) # (33977984, <type 'int'>) referencing to 10 int typed in memory

a = 'a' #now a is referencing to 'a' (which is string type, located to heap)
print (id(a), type(a)) # (34222904, <type 'str'>) referencing to 'a' string typed in memory

"""
    Python also save memory by referencing a value already present in memory.
"""

b = 10 # Since 10 int typed value already present in memory, So instead of creating another one
       # it will reference to previous location.
print (id(b), type(b)) # (33977984, <type 'int'>) referencing to 10 int typed in memory

"""
    Now one question arise that, if more than two variables are referencing to same location
    in memory and if value of one varible change than what will happend to anothers?
    So, if b,c are referencing to 10 and if b is incremented then it will refernce to another
    without any change to c.
"""
c = 10 # Since both c and b have same value , Python optimizer will reference to same location

print (id(c), type(c)) #id and type of c
print (id(b), type(b)) #id and type of b , both have same value
print (id(b)==id(c))
c += 10
print (id(c), type(c)) # Now c will refernce to another location in memory.
print (id(b)==id(c))

""" Automatic Garbage Collection in Python
    Python use an algorithm 'Reference counter' for garbage collection.
    It keep tracking the reference to value in memory. If any value reference become zero then
    Python delete the value this called memory delete.
"""




