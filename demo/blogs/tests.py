import pytest
import datetime

from . import models

pytestmark = pytest.mark.django_db

def test_post_without_author():
    dt = datetime.datetime.now()
    post = models.Post(title='awesome title', date_time=dt)

    assert str(post) == f'[{dt.isoformat()}] awesome title (N/A)'

def test_post_with_author():
    dt = datetime.datetime.now()
    author = models.Author.objects.create(nickname='foo', first_name='Massimo', last_name='Costa')
    post = models.Post(title='awesome title', date_time=dt, author=author)

    assert str(post) == f'[{dt.isoformat()}] awesome title (foo)'