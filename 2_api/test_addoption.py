"""Модуль для тестирования статуса ответа веб сайта """
import requests

def test_get(get_config):
    """Проверяем, что ответ сервера 200"""
    input_url = get_config.getoption('--url')
    print(f"GET: {input_url}")
    resp = requests.get(url=input_url)
    assert resp.status_code == 200
