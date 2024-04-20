from fastapi import status
from shared.constants.configs import configs


def test_router_basis(client):
    response = client.get(
        "/test_only/test_string",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "hello world"

    response = client.get(
        "/test_only/test_dict",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"hello": "world"}

    response = client.get(
        "/test_only/test_query?msg=hello",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "hello"}

    response = client.post(
        "/test_only/test_post",
        json={
            "title": "title",
            "content": "content",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "title": "response: title",
        "content": "response: content",
    }

    response = client.patch(
        "/test_only/test_patch",
        json={
            "title": "title",
            "content": "content",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "title": "response: title",
        "content": "response: content",
    }

    response = client.delete(
        "/test_only/test_delete",
        params={
            "title": "title",
            "content": "content",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "title": "response: title",
        "content": "response: content",
    }

    response = client.post(
        "/test_only/test_post_form",
        data={
            "title": "title",
            "content": "content",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "title": "response: title",
        "content": "response: content",
    }

    response = client.post(
        "/test_only/complex_case_post",
        params={
            "item_id": 1,
        },
        json={
            "title": "title",
            "content": "content",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "title": "response: title",
        "item_id": 1,
        "content": "response: content",
    }

    response = client.post(
        "/test_only/complex_case_form",
        params={
            "item_id": 1,
        },
        data={
            "title": "title",
            "content": "content",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "title": "response: title",
        "item_id": 1,
        "content": "response: content",
    }

    response = client.post(
        "/test_only/complex_case_form_and_body",
        params={
            "item_id": 1,
        },
        data={
            "title": "title",
            "content": "content",
        },
        json={
            "body": "body",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "title": "response: title",
        "item_id": 1,
        "content": "response: content",
        "body": "response: body",
    }

    response = client.post(
        "/test_only/test_upload_file",
        files={
            "file": ("test.txt", b"some file data"),
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "file_name": "test.txt",
        "file_content": "some file data",
    }


def test_doc_as_html(client):
    response = client.get(
        f"/{configs.ROOT_API_PREFIX}/docs",
    )
    assert response.status_code == status.HTTP_200_OK
    assert "Swagger UI" in response.text


def test_redoc_as_html(client):
    response = client.get(
        f"/{configs.ROOT_API_PREFIX}/redoc",
    )
    assert response.status_code == status.HTTP_200_OK
    assert "ReDoc" in response.text


def test_openapi_schema(client):
    response = client.get(
        f"/{configs.ROOT_API_PREFIX}/openapi.json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["info"]["title"] == configs.PROJECT_NAME


def test_healthcheck(client):
    response = client.get(
        f"/{configs.ROOT_API_PREFIX}/healthcheck",
    )
    assert response.status_code == status.HTTP_200_OK
