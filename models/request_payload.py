from pydantic import BaseModel, Field

class RequestPayload(BaseModel):
   query :str = Field(None, title="user query", max_length=100)
   test_result :str = Field(None, title="user test result", max_length=500)
   user_id :str = Field(None, title="user id", max_length=64)