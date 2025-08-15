# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List
# # get, post, put, delete
#
# app = FastAPI()
#
# @app.get('/')   # ('/') is called path
# def read():
#     return {"message": "Welcome to tea house"}
#
# class Tea(BaseModel):
#     id: int
#     name: str
#     origin: str
#
# teas:List[Tea] = []
#
# @app.get('/teas')
# def get_teas():
#     return teas
#
# @app.post('/teas')
# def add_teas(tea: Tea):
#     teas.append(tea)
#     print("Tea added")
#     return tea
#
# @app.put('/teas/tea_id')
# def update_tea(tea_id: int, updated_tea: Tea):
#     for index, tea in enumerate(teas):
#         if tea.id == tea_id:
#             teas[index] = updated_tea
#             return updated_tea
#     return {"error": "Tea not found"}
#
# @app.delete('teas/teas_id')
# def delete_tea(tea_id: int):
#     for index, tea in enumerate(teas):
#         if tea.id == tea_id:
#             delete = teas.pop(index)
#             return delete
#     return {"error": "Tea not found"}