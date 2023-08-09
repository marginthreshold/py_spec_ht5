str_path = '//C:/Users/user_name/python/some_file.txt'


def get_path_tuple_from_str_path(string_path: str) -> tuple[str]:
    *file_name, extention = string_path.split('.')
    *path, file1_name = file_name[0].split('/')
    return '/'.join(path), file1_name, extention


print(get_path_tuple_from_str_path(str_path))
