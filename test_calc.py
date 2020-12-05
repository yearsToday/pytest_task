import pytest
import yaml
from python_code.calc import Calculator


def test_a():
    print("测试用例a")


# 加载.yaml文件中的数据
with open("./datas/calc.yaml") as f:
    # 读取add中的内容
    datas = yaml.safe_load(f)['add']
    #print("add中的内容", datas)
    # 读取datas中的内容
    add_datas = datas['datas']
    #print("datas中的内容", add_datas)
    #读取myid内容
    myid = datas['myid']


    # 加载.yaml文件中的数据
with open("./datas/calc_div.yaml") as f:
    #读取div中的内容
    div = yaml.safe_load(f)['div']
    #读取div_datas中的内容
    div_datas = div['div-datas']
    #读取div_myid中的内容
    div_myid = div['div-myid']

class TestCalc:
    def setup_class(self):
        # 实例化计算器的类
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("计算结束")

    # @pytest.mark.parametrize():装饰器
    # 以（key，valuse）的方式定义方法中的参数及参数值
    #     ( "a,b,expect",
    #     [
    #         (1, 1, 2),
    #         (2, 2, 4),
    #         (3, 3, 6),
    #     ], ids = ['1', '2', '3'])

    @pytest.mark.parametrize(
        "a,b,expect",
        add_datas,ids=myid
    )
    #加法
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        # 得到结果之后，需要写断言
        # round(变量，2）  保留2位小数
        # if isinstance(result,float) 判断如果结果是小数，将进入round方法中
        if isinstance(result, float):
            result = round(result, 2)
        print(result)
        assert result, 2 == expect

    @pytest.mark.parametrize(
        "a,b,expect",
        div_datas,ids=div_myid
    )
    #除法
    def test_div(self,a,b,expect):
        result_div = self.calc.div(a,b)
        assert result_div == expect



