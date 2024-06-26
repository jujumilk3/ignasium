from fastapi import APIRouter, Body, File, Form, Query, UploadFile

router = APIRouter()


@router.get("/test_string")
async def get_string():
    return "hello world"


@router.get("/test_dict")
async def get_dict():
    return {"hello": "world"}


@router.get("/test_query")
async def get_query(
    msg: str = Query("hello", description="hello"),
):
    return {"msg": msg}


@router.post("/test_post")
async def post(
    title: str = Body("title", description="title", examples=["title"], embed=True),
    content: str = Body(
        "content", description="content", examples=["content"], embed=True
    ),
):
    return {
        "title": f"response: {title}",
        "content": f"response: {content}",
    }


@router.patch("/test_patch")
async def patch(
    title: str = Body("title", description="title", examples=["title"], embed=True),
    content: str = Body(
        "content", description="content", examples=["content"], embed=True
    ),
):
    return {
        "title": f"response: {title}",
        "content": f"response: {content}",
    }


@router.delete("/test_delete")
async def delete(
    title: str = Query("title", description="title", examples=["title"], embed=True),
    content: str = Query(
        "content", description="content", examples=["content"], embed=True
    ),
):
    return {
        "title": f"response: {title}",
        "content": f"response: {content}",
    }


@router.post("/test_post_form")
async def post_form(
    title: str = Form("title", description="title", examples=["title"]),
    content: str = Form("content", description="content", examples=["content"]),
):
    return {
        "title": f"response: {title}",
        "content": f"response: {content}",
    }


@router.post("/complex_case_post")
async def complex_case(
    item_id: int = Query(None, description="item_id", examples=["item_id"]),
    title: str = Body("title", description="title", examples=["title"], embed=True),
    content: str = Body(
        "content", description="content", examples=["content"], embed=True
    ),
):
    return {
        "item_id": item_id,
        "title": f"response: {title}",
        "content": f"response: {content}",
    }


@router.post("/complex_case_form")
async def complex_case_form(
    item_id: int = Query(None, description="item_id", examples=["item_id"]),
    title: str = Form("title", description="title", examples=["title"]),
    content: str = Form("content", description="content", examples=["content"]),
):
    return {
        "item_id": item_id,
        "title": f"response: {title}",
        "content": f"response: {content}",
    }


@router.post("/complex_case_form_and_body")
async def complex_case_form_and_body(
    item_id: int = Query(None, description="item_id", examples=["item_id"]),
    title: str = Form("title", description="title", examples=["title"]),
    content: str = Form("content", description="content", examples=["content"]),
    body: str = Body("body", description="body", examples=["body"], embed=True),
):
    return {
        "item_id": item_id,
        "title": f"response: {title}",
        "content": f"response: {content}",
        "body": f"response: {body}",
    }


@router.get("/get_page_num_as_requested")
async def get_page_num_as_requested(
    offset: int = Query(0, description="offset", examples=[0]),
    limit: int = Query(20, description="limit", examples=[20]),
):
    return {"hello": "world"}


@router.post("/test_upload_file")
async def upload_file(
    file: UploadFile = File(None, description="file", examples=["file"]),
):
    return {"file_name": file.filename, "file_content": file.file.read()}
