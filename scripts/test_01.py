import allure

from base.get_driver import get_phone_driver
from base.page import Page


class TestHslOpen:

    def setup_class(self):
        self.driver = get_phone_driver("com.hsl.stock", ".module.main.StartV2Activity")
        self.page = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()


    def test_01(self):
        self.page.open_hsl().open_rules_click_agrees()
        ass = self.page.open_hsl().get_result()
        assert ass == "兔子人"
        # ass = self.page.open_hsl().get_result()
        # assert ass == "涨停成功率"

    def test_02(self):
        pass
