import time

import allure
import pytest


class Test_002:

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是放入截图的测试步骤")
    def test_add_png(self):
        print("我是截图")
        with open("C:\\Users\\86131\\Desktop\\sh-app8-day08-1\\images\\rooo.png", "rb") as f:
            allure.attach("我是超人{}".format(time.strftime('%Y%m%r_%H%M%S')), f.read(), allure.attach_type.PNG)
        assert True