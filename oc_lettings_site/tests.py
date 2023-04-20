from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_index(client):
    #uri = reverse('oc_lettings_site:index')
    resp = client.get('/index')
    assert 'title' in str(resp.content)