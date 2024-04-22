from fastapi import status


def test_platform_crud(client):
    # create
    response = client.post(
        "/ignasium/v1/platform/",
        json={
            "name": "platform_name",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["name"] == "platform_name"
    assert response.json()["id"] > 0
    just_created_id = response.json()["id"]

    # read by id
    response = client.get(
        f"/ignasium/v1/platform/{just_created_id}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == "platform_name"
    assert response.json()["id"] == just_created_id

    # read by name
    response = client.get(
        f"/ignasium/v1/platform/platform_name",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == "platform_name"
    assert response.json()["id"] == just_created_id

    # update
    response = client.patch(
        f"/ignasium/v1/platform/{just_created_id}",
        json={
            "name": "new_platform_name",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == "new_platform_name"
    assert response.json()["id"] == just_created_id

    # delete
    response = client.delete(
        f"/ignasium/v1/platform/{just_created_id}",
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # read again. it returns 404
    response = client.get(
        f"/ignasium/v1/platform/{just_created_id}",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Model not found"
