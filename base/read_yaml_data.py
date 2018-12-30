import yaml, os
#读取yaml的数据
def read_yaml_data(file_name):
    with open("./data" + os.sep + file_name, "r",encoding="utf-8") as f:
        return yaml.load(f)
