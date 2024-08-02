

import os

path = "host_vars"
dir_list = os.listdir(path)


for file in dir_list:
    file = file.split(".")[0]
    print(f"  - fqdn: {file}")
    print(f"    parentContainerName: Region2")
    print(f"    configlets:")
    print(f"      - 'Underlay_{file}'")


# for file in dir_list:
#     file = file.split(".")[0]
#     print(f"  Underlay_{file}: \"{{{{ lookup('file', '../intended/configs/{file}.cfg') }}}}\"")
