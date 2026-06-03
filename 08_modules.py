


# operating system interaction

# print(os.getcwd())
# print(os.listdir())

# if os.path.exists("manage.py"):
#     print("manage.py exists")
#     print(os.path.getsize("manage.py"))
# else:
#     print("manage.py does not exist")

import os
#
# def total_size_of_files(folder):
#     total = 0
#     for name in os.listdir(folder):
#         path = os.path.join(folder, name)
#         if os.path.isfile(path):
#             total += os.path.getsize(path)
#     return total
#
# print(total_size_of_files(r"D:\programare\PROGRAMARE - PYTHON GR. 27\Python-Gr.-27"))

def total_files_size():
    """Function that returns total file size for all files in root level
directory.
:return: total file size, in KB"""
    files = os.listdir()
    total = 0
    for f in files:
        if os.path.isfile(f):
            size = os.path.getsize(f)
            total += size
    return total/1024
print(total_files_size())

