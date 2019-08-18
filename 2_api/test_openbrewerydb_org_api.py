"""Модуль для тестирования API https://jsonplaceholder.typicode.com/"""

import pytest
import requests

@pytest.mark.parametrize("beer_id", [5494, 5497, 5499])
def test_get_brewery_by_id(beer_id):
    """Проверяем, что по id получаем нужный обьект
    и у обьекта присутствуют обязательные поля"""
    url = "https://api.openbrewerydb.org/breweries/" + str(beer_id)
    resp = requests.get(url=url)
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json; charset=utf-8'
    data = resp.json()
    assert beer_id == data['id']
    fields = [
        'name',
        'brewery_type',
        'street',
        'city',
        'state',
        'postal_code',
        'country',
        'longitude',
        'latitude',
        'phone',
        'website_url',
        'updated_at'
    ]
    for element in fields:
        assert element in data
    assert isinstance(data['tag_list'], list)
    for element in data['tag_list']:
        assert isinstance(element, str)

@pytest.mark.parametrize("state", ["California", "Aliaska"])
def test_get_brewery_by_state(state):
    """Проверяем, что  при поиске по названию штата у возращаемых обьектов
    значение поля state равно вводимому в запросе """
    url = "https://api.openbrewerydb.org/breweries?" + "by_state=" + state
    resp = requests.get(url=url)
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json; charset=utf-8'
    data = resp.json()
    assert isinstance((data), list)
    for element in data:
        assert isinstance(element, dict)
        assert element['state'] == state

def test_get_brewery_by_tag():
    """Проверяем, что при поиске по тегу обьект содержит поле
    tag_list, оно является списком в котором лежат теги указанные при запросе"""
    url = "https://api.openbrewerydb.org/breweries?" + "by_tag =" + "patio"
    resp = requests.get(url=url)
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json; charset=utf-8'
    data = resp.json()
    assert isinstance((data), list)
    for element in data:
        assert isinstance(element, dict)
        assert isinstance(element['tag_list'], list)
        for items in element['tag_list']:
            assert isinstance((items), str)
            assert "patio" in items

@pytest.mark.parametrize('word', ['dog', 'sea', 'fun'])
def test_get_name_by_autocomplite(word):
    """Проверяем, что у возвращаемых обьектов
    при поиске автокомплитом присутстуют поля
    имя и id"""
    resp = requests.get(f'https://api.openbrewerydb.org/breweries/autocomplete?query={word}')
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json; charset=utf-8'
    data = resp.json()
    assert isinstance((data), list)
    for element in data:
        assert isinstance(element, dict)
        assert 'id' in element
        assert 'name' in element

@pytest.mark.parametrize('name', ['rick', 'cross', 'cooperative'])
def test_get_brewery_by_name(name):
    """Проверяем, что у возвращемых обьектов
    при поиске по имени значение поля country - United States'"""
    resp = requests.get(f'https://api.openbrewerydb.org/breweries?by_name={name}')
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json; charset=utf-8'
    data = resp.json()
    for element in data:
        assert element['country'] == 'United States'
