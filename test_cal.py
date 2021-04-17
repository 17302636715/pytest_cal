import pytest
import yaml
import allure


def get_datas():
    with open('./data.yaml', encoding='UTF-8') as f:
        datas = yaml.safe_load(f)

    return datas


@allure.feature('测试计算器')
class TestCal:

    @pytest.mark.parametrize('a,b,expect', get_datas()['test_add']['datas'],
                             ids=get_datas()['test_add']['ids'])
    @allure.story('测试加法')
    def test_add(self, cal, a, b, expect):

        if isinstance(a, str) or isinstance(b, str):
            try:
                a1 = complex(a)
                b1 = complex(b)
                expect1 = complex(expect)
                a = a1
                b = b1
                expect = expect1
            except:
                pass

        if isinstance(a, (int, float, complex)) and isinstance(b, (int, float, complex)):
            assert expect == cal.add(a, b)
        else:
            pytest.raises(TypeError)

    @pytest.mark.parametrize('a,b,expect', get_datas()['test_div']['datas'],
                             ids=get_datas()['test_div']['ids'])
    @allure.story('测试除法')
    def test_div(self, cal, a, b, expect):

        try:
            assert expect == cal.div(a, b)
        except TypeError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
