# Задание 1

import os

starter = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in starter.items():
    if os.path.exists(root):
        print(root)
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            os.makedirs(cur_dir)
print(starter)