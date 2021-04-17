import pytest
from test_calculate.calculate import Calculate


@pytest.fixture(scope='class')
def cal():
    print("开始测试计算器功能")
    calculate = Calculate()
    yield calculate
    print("结束测试计算器功能")


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
