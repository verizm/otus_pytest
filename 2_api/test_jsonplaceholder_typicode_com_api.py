"""Модуль тестирования API https://jsonplaceholder.typicode.com/ """

import pytest
import requests

@pytest.mark.parametrize('post_id', ['1', '2', '3', '4'])
def test_get_posts(post_id):
    """Проверяем, что по id получаем нужный обьект
    с обязательными полями"""
    resp = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json; charset=utf-8'
    data = resp.json()
    assert int(post_id) == data['id']
    fields = ['userId', 'id', 'title', 'body']
    for element in fields:
        assert element in data

@pytest.mark.parametrize('user_id, user_name', [('1', 'Leanne Graham'),
                                                ('2', 'Ervin Howell'), ('3', 'Clementine Bauch')])
def test_get_users(user_id, user_name):
    """Проверяем, что в возвращаемом обьекте имя
     соответствует номеру"""
    resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json; charset=utf-8'
    data = resp.json()
    assert data['name'] == user_name

@pytest.mark.parametrize('photo_id', ['1', '2', '3'])
def test_get_photos(photo_id):
    """Проверяем, что в возвращаемом обьекте
    присутствуют обязательные поля,
    что картиныки загружаются"""
    resp = requests.get(f'https://jsonplaceholder.typicode.com/photos/{photo_id}')
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json; charset=utf-8'
    data = resp.json()
    fields = ['albumId', 'id', 'title', 'url', 'thumbnailUrl']
    for items in fields:
        assert items in data
    resp_img = requests.get(url=data['url'])
    resp_thu_img = requests.get(url=data['thumbnailUrl'])
    assert resp_img.status_code == 200
    assert resp_thu_img.status_code == 200


@pytest.mark.parametrize('comments_id', ['1', '2', '3'])
def test_get_comments(comments_id):
    """Проверяем, что в возвращаемом обьекте
    присутсвуют  обязательные поля"""
    url = (f"https://jsonplaceholder.typicode.com/comments/{comments_id}")
    resp = requests.get(url=url)
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json; charset=utf-8'
    data = resp.json()
    fields = ['postId', 'id', 'name', 'email', 'body']
    for element in data:
        assert isinstance((element), str)
        assert element in fields


@pytest.mark.parametrize('albums_id', ['1', '2', '3'])
def test_get_albums(albums_id):
    """Проверяем, что в возвращаемом обьекте
       присутсвуют  обязательные поля"""
    url = (f"https://jsonplaceholder.typicode.com/albums/{albums_id}")
    resp = requests.get(url=url)
    assert resp.status_code == 200
    assert resp.headers['content-type'] == 'application/json; charset=utf-8'
    data = resp.json()
    assert isinstance((data), dict)
    fields = ['id', 'userId', 'title']
    for element in data:
        assert isinstance((element), str)
        assert element in fields
