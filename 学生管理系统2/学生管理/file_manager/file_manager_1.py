base_dir = '../file/'


def wirter_json(file_name, data):
    with open(base_dir + file_name, mode='w') as a:
        import json
        json.dump(data, a)


def read_json(file_name, default_data):
    try:
        with open(base_dir + '/' + file_name, mode='r') as b:
            import json
            return json.load(b)
    except FileNotFoundError:
        print('file is no found')
        return default_data


def reder_file(file_name):
    try:
        with open(base_dir + file_name, mode='r', encoding='utf8') as stream:
            content = stream.read()
            return content
    except FileNotFoundError:
        print('文件为找到')
