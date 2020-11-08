'''
import User from models and pytest
'''
import pytest
from flask import session
from models import User # pylint: disable=import-error


@pytest.mark.run(order=3)
def test_logout_user(client):
    '''
    tests login the user that was registered in last test to the database
    '''
    with client:
        user = User.query.filter(User.email == 'aryehlevklein@gmail.com').first()
        client.post('/logout', follow_redirects=True)
        assert user.is_authenticated is False
        
