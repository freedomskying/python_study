from collections import OrderedDict

import json


class ComponetCheck:
    def __init__(self, data_dir):
        self.data_dir = data_dir

        self._extend_function_dic = OrderedDict({})

    def add_extend_function(self, function_name, *parameters):
        self._extend_function_dic[function_name] = parameters

    def _check_extend_function(self):
        for function_name, parameters in self._extend_function_dic.iteritems():
            if not apply(function_name, parameters):
                return False
        return True


class CheckFunctions:
    def __init__(self):
        pass

    def tollcost_check(data_path):
        toll_cost_path = os.path.join(data_path, Importer.DT_KOR_TOLL_COST)
        tollcost_component = ComponentCheck(toll_cost_path)
        tollcost_component.add_extend_function(tollcost_component.check_file_pattern_list_match,
                                               CheckFunctions.TOLL_COST_FILENAME_PATTERN)
        return tollcost_component


@staticmethod
def speed_camera_check(data_path):
    speed_camera_path = os.path.join(data_path, Importer.DT_SAFETY_CAMERA)
    speed_camera_component = ComponentCheck(speed_camera_path)
    speed_camera_component.add_extend_function(speed_camera_component.check_not_exist_empty_directory)
    return speed_camera_component


class Foo(object):
    def __init__(self):
        self.name = 'abc'

    def func(self):
        return 'ok'


if __name__ == '__main__':
    obj = Foo()
    ret = getattr(obj, 'func')
    r = ret()
    print(r)

    ret = hasattr(obj, 'func')
    print(ret)

    # 设置成员
    print(obj.name)  # 设置之前为:abc
    ret = setattr(obj, 'name', 19)
    print(obj.name)  # 设置之后为:19

    func_names = dir(Foo)
    print(func_names)

    dict_a = {'a': '1', 'b': {'b1', '21'}, 'b': {'b1', '22'}}

    print(dict_a)

    # Python 字典类型转换为 JSON 对象
    data1 = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com',
        'data': {
            'data1': {'a': 1, 'b': 2},
            'data2': {'a': 1, 'b': 2}
        }
    }

    print(data1['data'])
    print(len(data1['data']))
    print(type(data1['data']))

    for i in data1['data']:
        print(data1['data'][i])

    json_str = json.dumps(data1)
    print("Python 原始数据：", repr(data1))
    print("JSON 对象：", json_str)

    # 将 JSON 对象转换为 Python 字典
    data2 = json.loads(json_str)
    print("data2['name']: ", data2['name'])
    print("data2['url']: ", data2['url'])
