from api.models.task import Task
from flask import jsonify, make_response
from pydantic import ValidationError
from api.utils.response import response
from api.services.task import TaskService

task_service = TaskService()

class TaskController():
    def createTask(self, data):
        try:
            task = Task(name=data["name"], description=data["description"], done=data["done"])
            
            task_service.createTask(task)
            
            return response(
                success=True,
                data=[],
                message="Task created successfully.",
                statusCode=201
            )
        except ValidationError as e:
            return response(
                success=False,
                data=[],
                message=str(e),
                statusCode=400
            )

        
    def updateTask(self, id, data):
        try:
            result = task_service.updateTask(taskId=id, updatedData=data)
            
            if(result is None):
                return response(
                    success=True,
                    data=[],
                    message="Task not found.",
                    statusCode=204
                )
            
            return response(
                success=True,
                data=[],
                message="Task updated successfully.",
                statusCode=200
            )
        except ValidationError as e:
              return response(
                success=False,
                data=[],
                message=str(e),
                statusCode=400
            )
        except Exception as e:
            return response(
                success=False,
                data=[],
                message=str(e),
                statusCode=400
            )
                      
    def deleteTask(self, id):
        try:
            result = task_service.deleteTask(taskId=id)
            
            if(result is None):
                return response(
                    success=True,
                    data=[],
                    message="Task not found.",
                    statusCode=204
                )
            
            return response(
                success=True,
                data=[],
                message="Task deleted successfully.",
                statusCode=200
            )
        except ValidationError as e:
              return response(
                success=False,
                data=[],
                message=str(e),
                statusCode=400
            )
        except Exception as e:
            return response(
                success=False,
                data=[],
                message=str(e),
                statusCode=400
            )
        
    def getAllTasks(self):
        try:
            tasks = task_service.getAllTasks()
           
            return response(
                success=True,
                data=tasks,
                message="Tasks retrieved successfully.",
                statusCode=200
            )
        except ValidationError as e:
              return response(
                success=False,
                data=[],
                message=str(e),
                statusCode=400
            )
    
    def getTask(self, id):
        try:
            task = task_service.getTask(taskId=id)
            
            if(task is None):
                return response(
                    success=True,
                    data=[],
                    message="Tasks not found.",
                    statusCode=204
                )
            
            return response(
                success=True,
                data=task,
                message="Tasks retrieved successfully.",
                statusCode=200
            )
        except ValidationError as e:
            return response(
                success=False,
                data=[],
                message=str(e),
                statusCode=400
            )
        except Exception as e:
            return response(
                success=False,
                data=[],
                message=str(e),
                statusCode=400
            )