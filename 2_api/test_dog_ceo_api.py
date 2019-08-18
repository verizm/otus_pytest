""" Модуль тестирования API  https://dog.ceo/dog-api/ """

import pytest
import requests

BASE_URL_BREEDS = "https://dog.ceo/api/breeds/"
BASE_URL_BREED = "https://dog.ceo/api/breed/"

def test_list_of_breeds():
    """ Проверяем, что поле "message" словарь, что в данном словаре ключ - строка,
    а значение список, в списке значения содержатся строки """
    url = BASE_URL_BREEDS + 'list/all'
    resp = requests.get(url=url)
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json'
    data = resp.json()
    assert data['status'] == 'success'
    assert isinstance(data['message'], dict)
    for key, value in data['message'].items():
        assert isinstance(key, str)
        assert isinstance(value, list)
        for element in value:
            assert isinstance(element, str)

@pytest.mark.parametrize("breed", ["bulldog", "hound", "mastiff", "corgi",
                                   "terrier", "spaniel"])
def test_list_all_sub_breeds(breed):
    """Проверяем, что породы указанные в параметризации
    присутсвуют в списке пород являются ключем  и в значении
    содержится список"""
    url = BASE_URL_BREED + breed + '/list'
    resp = requests.get(url=url)
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json'
    data = resp.json()
    assert data['status'] == 'success'
    assert isinstance(data['message'], list)
    for element in data['message']:
        assert isinstance(element, str)

@pytest.mark.parametrize("breed,sub_breed", [
    ("hound", ["afghan", "basset", "blood", "english", "ibizan", "walker"]),
    ("corgi", ["cardigan"])])
def test_list_all_sub_breed_images(breed, sub_breed):
    """Получаем все фотографии пород хаунд и корги и их подпород,
       проверяем, что последнее фото из списка успешно загружено"""
    for sub in sub_breed:
        url = BASE_URL_BREED + breed + '/' + sub + '/images'
        resp = requests.get(url=url)
        assert resp.status_code == 200
        assert resp.headers['content-type'] == 'application/json'
        data = resp.json()
        assert data['status'] == 'success'
        assert isinstance(data['message'], list)
        for element in data['message']:
            assert isinstance(element, str)
        last_img = data['message'][len(data['message']) - 1]
        resp_img = requests.get(url=last_img)
        assert resp_img.status_code == 200

def test_random_image():
    """Получаем случайное фото, проверяем, что оно успешно загружено"""
    url = BASE_URL_BREEDS + 'image/random'
    resp = requests.get(url=url)
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json'
    data = resp.json()
    assert data['status'] == 'success'
    assert isinstance(data['message'], str)
    resp_img = requests.get(url=data['message'])
    assert resp_img.status_code == 200

@pytest.mark.parametrize("breed,sub_breed", [
    ("bulldog", ["boston", "english", "french"]),
    ("frise", ["bichon"])])
def test_list_all_sub_breed_images_random(breed, sub_breed):
    """Получаем случайное фото подпород бульдога и фрайза, проверяем,
     что фото успешно загружено"""
    for sub in sub_breed:
        url = BASE_URL_BREED + breed + "/" + sub + '/' + 'images/random'
        resp = requests.get(url=url)
        assert resp.status_code == 200
        assert resp.headers['content-type'] == 'application/json'
        data = resp.json()
        assert data['status'] == 'success'
        assert isinstance(data['message'], str)
        resp_img = requests.get(url=data['message'])
        assert resp_img.status_code == 200
@pytest.mark.parametrize("num", [1, 2, 3])
def test_multiple_images_for_a_sub_breed_collection(num):
    """Получаем, одну, две, три случайных фотографии породы корги кардиган,
     проверяем, что фото успешно загружены"""
    url = BASE_URL_BREED + "corgi/cardigan/images/random/" + str(num)
    resp = requests.get(url=url)
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json'
    data = resp.json()
    assert data['status'] == 'success'
    assert isinstance(data['message'], list)
    assert num == len(data['message'])
    for element in data['message']:
        assert isinstance(element, str)
