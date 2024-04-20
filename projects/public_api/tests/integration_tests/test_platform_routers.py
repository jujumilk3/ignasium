def test_platform_crud(client):
    response = client.post(
        "/platform/",
        json={
            "name": "platform_name",
            "description": "platform_description",
        },
    )
