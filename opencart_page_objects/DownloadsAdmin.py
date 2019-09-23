"""
Модуль страницы с загрузки файла
в админке
"""

import os
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from opencart_locators import AdminMain

class DownloadsAdmin:
    """
    Класс загрузки файла
    """

    def __init__(self, driver):
        self.driver = driver

    def add_new(self):
        """
        Добавить новую загрузку
        """
        add_button_div = self.driver.find_element_by_css_selector(AdminMain.add_button_div)
        add_button = add_button_div.find_element_by_css_selector(AdminMain.add_button)
        add_button.click()

    def upload(self, fname, dirname, content_type):
        """
        Выполнить загрузку картинки
        """
        url = self.driver.current_url
        parts = url.split('=')
        token = parts[2]

        # наша картинка
        filepath = os.path.join(dirname, fname)

        # заполним имя
        field_name = self.driver.find_element_by_css_selector(AdminMain.field_name['css'])
        field_name.send_keys(fname)

        # вызываем магичекий JS code
        # Выгребаем картинку из base64 в FormData
        # загружаем ее на сервер через AJAX

        jstemplate = "\
// Функция создания блоба из base64\n\
function base64toBlob(base64Data, contentType) {\n\
    var sliceSize = 1024;\n\
    var byteCharacters = atob(base64Data);\n\
    var bytesLength = byteCharacters.length;\n\
    var slicesCount = Math.ceil(bytesLength / sliceSize);\n\
    var byteArrays = new Array(slicesCount);\n\
    for (var sliceIndex = 0; sliceIndex < slicesCount; ++sliceIndex) {\n\
        var begin = sliceIndex * sliceSize;\n\
        var end = Math.min(begin + sliceSize, bytesLength);\n\
        var bytes = new Array(end - begin);\n\
        for (var offset = begin, i = 0; offset < end; ++i, ++offset) {\n\
            bytes[i] = byteCharacters[offset].charCodeAt(0);\n\
        }\n\
        byteArrays[sliceIndex] = new Uint8Array(bytes);\n\
    }\n\
    return new Blob(byteArrays, {type: contentType});\n\
}\n\
// Создаем форму и запихиваем блоб с картинкой\n\
var contentType = '%s';\n\
var b64Data = '%s';\n\
var blob = base64toBlob(b64Data, contentType);\n\
var formData = new FormData();\n\
formData.append('file', blob, '%s');\n\
// А теперь выполним AJAX запрос к серверу и загрузим картинку\n\
// Незабываем про сессионную куку\n\
$.ajax({\n\
    url: 'index.php?route=catalog/download/upload&user_token=%s',\n\
    type: 'post',\n\
    dataType: 'json',\n\
    data: formData,\n\
    cache: false,\n\
    contentType: false,\n\
    processData: false,\n\
    beforeSend: function() {\n\
        $('#button-upload').button('loading');\n\
    },\n\
    complete: function() {\n\
        $('#button-upload').button('reset');\n\
    },\n\
    success: function(json) {\n\
        if (json['success']) {\n\
            $('input[name=\\'filename\\']').val(json['filename']);\n\
            $('input[name=\\'mask\\']').val(json['mask']);\n\
        }\n\
    },\n\
    error: function(xhr, ajaxOptions, thrownError) {\n\
    }\n\
});"

        image_file = open(filepath, "rb")
        encoded_string = base64.b64encode(image_file.read()).decode('ascii')

        js_code = jstemplate % (content_type, encoded_string, fname, token)
        #print(js_code)

        self.driver.execute_script(js_code)

        WebDriverWait(self.driver, 3).until(
            EC.text_to_be_present_in_element_value(
                (By.ID, AdminMain.field_mask['id']),
                fname)
        )

        button_save = self.driver.find_element_by_css_selector(AdminMain.button_save['css'])
        button_save.click()
