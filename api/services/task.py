from api.models.task import TaskDB, Task
from database.db import db
from api.utils.serializer import Serializer

class TaskDBException(Exception):
    pass

class TaskService():
    def createTask(self, task:Task):
        taskDB = TaskDB(name=task.name, description=task.description)
        db.session.add(taskDB)
        db.session.commit()

    def updateTask(self, taskId, updatedData):
        taskDB = TaskDB.query.get(taskId)
        
        if(taskDB is None):
            raise TaskDBException("Task not found")
        
        taskDB.name = updatedData.get("name", taskDB.name)
        taskDB.description = updatedData.get("description", taskDB.description)

        db.session.commit()
        
    def deleteTask(self, taskId):
        taskDB = TaskDB.query.get(taskId)

        if(taskDB is None):
            raise TaskDBException("Task not found")
        
        db.session.delete(taskDB)
        db.session.commit()
        
    def getAllTasks(self):
        try:
            return Serializer.serialize_list(TaskDB.query.all()) 
        except Exception as e:
            raise str(e)
    
    def getTask(self, taskId):
        try:
            taskDB = TaskDB.query.get(taskId)

            if(taskDB is None):
                raise TaskDBException("Task not found")

            return taskDB.serialize()
        except TaskDBException as e:
            raise TaskDBException(str(e))