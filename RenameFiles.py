import os

path = r"/Users/gaurav1.kamboj/Desktop/GitLeetCode"

for subfolder_name in os.listdir(path):
    subfolder_path = os.path.join(path, subfolder_name)

    if os.path.isdir(subfolder_path) and subfolder_name[0].isdigit():
        current_number = subfolder_name.split('-')[0].strip()
        new_name = f'{current_number.zfill(4)}-{subfolder_name.split("-", 1)[1].strip()}'

        new_subfolder_path = os.path.join(path, new_name)
        os.rename(subfolder_path, new_subfolder_path)
        print(f'Renamed "{subfolder_name}" to "{new_name}"')

print("Folders renamed!")
