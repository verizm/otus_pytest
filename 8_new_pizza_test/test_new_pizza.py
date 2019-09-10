

def test_get_all_courses_page(get_driver_pizza):
    driver = get_driver_pizza
    driver.get("https://virtuozy-msk.ru/")
    courses_page = driver.find_element_by_css_selector("nav#main-nav li:nth-of-type(1)")
    courses_page.click()
    driver.find_element_by_css_selector("h1.page-title2")
    all_courses = driver.find_element_by_css_selector("nav.list li[data-group='all'")
    #background_all_courses = all_courses.get_property("'background = '#3f9b26'")
    #assert background_all_courses == "#3f9b26"
    all_courses_text = all_courses.text
    assert all_courses_text == 'ВСЕ КУРСЫ'

def test_get_skripka_courses(get_driver_pizza):
    driver = get_driver_pizza
    driver.get("https://virtuozy-msk.ru/")
    courses_page = driver.find_element_by_css_selector("nav#main-nav li:nth-of-type(1)")
    courses_page.click()
    skripka_courses = driver.find_element_by_css_selector("nav.list li[data-group='skripka'")
    skripka_courses.click()
    chamber_orcestra = driver.find_element_by_css_selector("article > button[data-value-tool^='Камерный оркестр']")
    alone = driver.find_element_by_css_selector("section.group button[data-value-tool^='Скрипка']")
    child = driver.find_element_by_css_selector("article > button[data-value-tool^='Обучение детей']")
    for element in [chamber_orcestra, alone, child]:
        assert element.text == "ЗАПИСАТЬСЯ"

def test_add_manual():
    driver = webdriver.Firefox()
    driver.maximize_window()

    # логинимся в админку
    driver.get("http://192.168.88.215/admin/")
    search_input_login = driver.find_element_by_id("input-username")
    search_input_login.send_keys("admin")
    search_input_password = driver.find_element_by_id("input-password")
    search_input_password.send_keys("admin")
    search_button = driver.find_element_by_class_name("btn-primary")
    search_button.click()

    # открываем продукты
    wait = WebDriverWait(driver, 10)
    search_catalog_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-catalog")))
    search_catalog_button.click()
    search_product_button = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Products")))
    search_product_button.click()

    # заполняем наше творение
    #div_with_buttons = driver.find_element_by_class_name("pull-right")
    add_button = driver.find_element_by_css_selector("a[data-original-title='Add New']")
    add_button.click()

    product_name = "III_DEVICE1"
    product_module = "III_MODULE1"

    driver.refresh()

    # заполненение полей 1 страница
    input_product_name_field = driver.find_element_by_id("input-name1")
    input_product_name_field.send_keys(product_name)
    input_meta_title_field = driver.find_element_by_id("input-meta-title1")
    input_meta_title_field.send_keys("Meta " + product_name)

    # заполнение полей 2 страница
    search_data_page = driver.find_element_by_partial_link_text("Data")
    search_data_page.click()
    input_model_field = driver.find_element_by_id("input-model")
    input_model_field.send_keys(product_module)

    # сохранение
    save_button = driver.find_element_by_css_selector("button[data-original-title='Save']")
    time.sleep(1)
    save_button.click()








