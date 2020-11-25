import yaml


def ini_case():
    path = "C:\\Users\\liaobin20\\PycharmProjects\\apiAutoTestDemo\\tests\\testdatas\\demo.yaml"
    with open(path, 'r', encoding="utf-8") as f:
        res = yaml.safe_load(f)
    return res


if __name__ == '__main__':
    print(ini_case())