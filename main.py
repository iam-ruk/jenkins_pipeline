from langchain.utilities import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
import os
import numpy as np
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI,Depends
from sqlmodel import Session, SQLModel, create_engine
from models.Chat_History import ChatHistory
from models.request_payload import RequestPayload
from typing import Annotated
import uuid
from fastapi.middleware.cors import CORSMiddleware
from constants.application_constants import PROMPT



#find .env files
dotenv_path = find_dotenv()
#load environment variables
load_dotenv(dotenv_path)

class SQLAgent:

    def __init__(self):
        #init env variables

        self.__db = SQLDatabase.from_uri(os.getenv("DB_URI"))
        self.__OPENAI_GPT_MODEL = os.getenv("OPENAI_GPT_MODEL")


        #instantiate model and sql agent
        
        self.__db.get_usable_table_names()

        self.__llm = ChatOpenAI(
            model = self.__OPENAI_GPT_MODEL,
            verbose = "True",
            max_tokens=None,
            openai_api_key = os.getenv("OPENAI_API_KEY")
        )

        self.__agent_executor = create_sql_agent(
            llm=self.__llm,
            toolkit=SQLDatabaseToolkit(db = self.__db, llm = self.__llm),
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        )

    def get_agent(self):
        return self.__agent_executor
    
    def get_model(self):
        return self.__llm
    



def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

sql_agent = SQLAgent()
model = sql_agent.get_model()
app = FastAPI()
agent = sql_agent.get_agent() 
sqlite_url = os.getenv("DB_URI")

engine = create_engine(sqlite_url)
SessionDep = Annotated[Session, Depends(get_session)]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    print("Server Init")
    create_db_and_tables()

@app.post("/")
async def handle_request(payload: RequestPayload):
   query = (PROMPT + " " +  payload.test_result + " query : " + payload.query + " answer the following query")
   chat = ChatHistory(id = uuid.uuid4(), user_id = payload.user_id, query = payload.query)
   with Session(engine) as session:
    session.add(chat)
    session.commit()
   return model.invoke(query).content;