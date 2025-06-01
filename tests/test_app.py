from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo
    - A: Act     - Executa a coisa (o SUI)
    - A: Assertr - Garanta que A é A
    """
    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}


def test_html_ola_mundo(client):
    response = client.get('/ola-mundo')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá mundo!</h1>' in response.text


def test_update_integrity_error(client, user, token):
    client.post(
        '/users',
        json={
            'username': 'fausto',
            'email': 'fausto@example.com',
            'password': 'secret',
        },
    )
    response = client.put = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'fausto',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Username or Email already exists'}
