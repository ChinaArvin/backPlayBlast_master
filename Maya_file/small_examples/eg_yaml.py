import os, yaml , subprocess

def main():
    data = dict()
    with open('E:/pycharm_Code/Maya_file/config.yaml','r') as f:
        data = yaml.load(f)
        print data
    _env = os.environ.copy() # ENV_NAME:ENV_VALUE
    for e in data['Env']:
        if e['mode'] == 'over':
            _env[e['name']] = e['value']

        elif e['mode'] == 'pre':
            _env[e['name']] = e['value'] + ';' + os.environ.get(e['name'] , '')

        else:
            pass

    #subprocess.Popen(data['Exec'],env=_env)


if __name__ == '__main__':
    main()

