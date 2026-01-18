'''
    @pytest.mark的使用：
        Mark装饰器实现对用例的标记分类操作管理
        Mark可以实现对同一个用例进行多个标签的标记。但是每个标记都是单独一行。
        Mark标签的名称，在取名的时候一定要尽可能简单直接。不要太复杂。
        mark装饰器的调用：可以支持到逻辑运算符的，也就是and or not三类条件的使用
            -m 标签名称 实现对用例的执行管理
            -m "hcc and login"  表示运行所有同时标记为hcc和login的测试用例
            -m "hcc or login"   表示运行所有标记为hcc或者login的测试用例
            -m "not hcc"    表示运行所有标记不为hcc的测试用例
        mark装饰器在调用-m指令的时候，请记得标签名称一定要用""括起来。这样可以避免出现意想不到的问题
'''
import pytest


@pytest.mark.login
def test_func01():
    print('这是01')


@pytest.mark.hcc
def test_func02():
    print('这是02')


# 多个mark在同一用例上
@pytest.mark.login
@pytest.mark.hcc
def test_func03():
    print('这是03')


def test_func04():
    print('这是04')


if __name__ == '__main__':
    # 推荐：将每个参数作为单独列表元素
    pytest.main(['-sv', 'test_mark.py', '-m login and hcc'])
    # 或者：将 -m 和表达式作为一个参数
    # pytest.main(['-sv', 'test_mark.py', '-m login and hcc'])
