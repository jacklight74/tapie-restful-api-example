from pydantic import BaseModel, Field

class TodoCreate(BaseModel):
    title: str = Field(..., example="우유 사기", description="할 일의 제목 또는 내용입니다.")
    completed: bool = Field(default=False, example=False, description="완료 여부입니다. 기본값은 False입니다.")

class TodoUpdate(BaseModel):
    title: str | None = Field(None, example="책 읽기", description="새로운 제목입니다. 선택 사항입니다.")
    completed: bool | None = Field(None, example=True, description="새로운 완료 여부입니다. 선택 사항입니다.")

class Todo(TodoCreate):
    id: int = Field(..., example=1, description="할 일 항목의 고유 ID입니다.")