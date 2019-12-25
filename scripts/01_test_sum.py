import sys,os
sys.path.append(os.getcwd())

from base.getData import GetData

import pytest,yaml


"""定义方法"""
def get_sum_data():
    # 定义存储数据列表
    sum_list = []
    # 读取数据文件
    # 解决路径问题  os.sep: 获取系统路径分隔符  因为Unix 分隔符为: "/"  Windows "\"
    # with open("./data"+ os.sep + "sum","r",encoding="utf-8") as f:
    #     # 解析数据
    #     data = yaml.safe_load(f)
    #     print("data:{}".format(data))
    #     for i in data.values():
    #         sum_list.append(tuple(i.values()))
    # return sum_list

    data = GetData().get_yml_data("sum")
    for i in data.values():
        sum_list.append(tuple(i.values()))
    return sum_list


"""
想要的数据类型: [(1,2,3),(3,4,7),(4,7,12)]

data:{
    'test_sum1': {'a': 1, 'b': 2, 'c': 3}, 
    'test_sum2': {'a': 3, 'b': 4, 'c': 7}, 
    'test_sum3': {'a': 4, 'b': 7, 'c': 12}}
0.定义空列表  sum_list= []

1.获取data的所有values
    data.values() ---> data_list = [{'a': 1, 'b': 2, 'c': 3},
                                    {'a': 3, 'b': 4, 'c': 7},
                                    {'a': 4, 'b': 7, 'c': 12}]
2.获取数据需要遍历列表取出每个字典, 获取字典中的每个值
    for i in data_list:  ---> {'a': 1, 'b': 2, 'c': 3},{'a': 3, 'b': 4, 'c': 7},{'a': 4, 'b': 7, 'c': 12}
        i.values() ---> [1,2,3]/[3,4,7]/[4,7,12]                    
        # 需要元组 ---> 转换类型
        tuple(i.values())  ---> (1,2,3)/(3,4,7)/(4,7,12)
        # 追加数据到列表
        sum_list.append(tuple(i.values()))
3.返回  sum_list
"""

class TestSum:
    @pytest.mark.parametrize("a,b,c",get_sum_data())
    def test_sum(self,a,b,c):
        """
        判断两个数之和 a + b = c
        :param a:
        :param b:
        :param c:
        :return:
        """
        print ("{}+{}={}".format(a,b,c))

        assert a + b == c
