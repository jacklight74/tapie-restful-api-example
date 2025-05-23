from fastapi import FastAPI, HTTPException
from schemas import Todo, TodoCreate, TodoUpdate
import data
import uvicorn

app = FastAPI(
    title="할 일 목록 API",
    description="FastAPI로 구현된 간단한 할 일 관리 API입니다.",
    version="1.0.0",
    contact={
        "name": "API 지원",
        "email": "support@example.com",
    },
    docs_url="/api-docs",
    redoc_url="/api-redoc",
)

@app.get("/todos", response_model=list[Todo], summary="모든 할 일 가져오기", tags=["할 일 관리"])
def read_todos():
    """전체 할 일 목록을 반환합니다."""
    return data.get_all_todos()

@app.get("/todos/{todo_id}", response_model=Todo, summary="특정 할 일 가져오기", tags=["할 일 관리"])
def read_todo(todo_id: int):
    """
    특정 할 일 항목을 ID로 조회합니다.

    - **todo_id**: 조회할 할 일 항목의 ID
    """
    todo = data.get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="할 일을 찾을 수 없습니다.")
    return todo

@app.post("/todos", response_model=Todo, status_code=201, summary="새 할 일 추가하기", tags=["할 일 관리"])
def create_todo(todo: TodoCreate):
    """
    새로운 할 일 항목을 추가합니다.

    - **title**: 할 일 내용
    - **completed**: 완료 여부 (기본값: False)
    """
    return data.create_todo(todo.dict())

@app.put("/todos/{todo_id}", response_model=Todo, summary="할 일 수정하기", tags=["할 일 관리"])
def update_todo(todo_id: int, todo: TodoUpdate):
    """
    기존 할 일 항목을 수정합니다.

    - **title**: 수정할 제목 (선택)
    - **completed**: 수정할 완료 여부 (선택)
    """
    updated = data.update_todo(todo_id, todo.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="할 일을 찾을 수 없습니다.")
    return updated

@app.delete("/todos/{todo_id}", status_code=204, summary="할 일 삭제하기", tags=["할 일 관리"])
def delete_todo(todo_id: int):
    """할 일 항목을 삭제합니다."""
    if not data.get_todo(todo_id):
        raise HTTPException(status_code=404, detail="할 일을 찾을 수 없습니다.")
    data.delete_todo(todo_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)