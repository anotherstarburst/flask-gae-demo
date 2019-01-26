# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def app():
    import main
    main.app.testing = True
    return main.app.test_client()


def test_form(app):
    r = app.get('/form')
    assert r.status_code == 200
    assert 'Submit a form' in r.data.decode('utf-8')
