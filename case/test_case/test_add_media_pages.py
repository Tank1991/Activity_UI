from pages.add_media_pages import Add_media_pages
from pages.media_list_pages import Meida_list_pages
def add_media(driver):
    add_media_page = Add_media_pages(driver)
    media_list_page = Meida_list_pages(driver)

    media_list_page.click_newActive()
    add_media_page.act_name_input()
    # add_media_page.mudi()
    add_media_page.chexi_select()
    add_media_page.input_time()
    add_media_page.first_select()















