from .Pages.product_page import ProductPage
import pytest
from .Pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    # Ссылка для проверки правильности имени и цены, после добавления в корзину
    # link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    # Ссылка для добавления в конзину и рассчета значения. Снять коммент у метода "page.solve_quiz_and_get_code()"
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name()
    page.should_be_correct_price()
