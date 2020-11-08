"""
import client session
"""
import pytest
from flask import session


@pytest.mark.run(order=6)
def test_update_item(client):
    """
    tests changing amount of item in cart
    """
    test_item = {
        'id': '123123123',
        'num_items': '5',
    }
    with client:
        client.post('/update_num_items', data=test_item, follow_redirects=True)
        for item in session['cart']:
            if item['id'] == '123123123':
                num_items = item['num_items']
                break


        assert num_items == '5'
