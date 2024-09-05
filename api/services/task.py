from api.models.task import TaskDB, Task
from database.db import db
from api.utils.serializer import Serializer

class TaskDBException(Exception):
    pass

class TaskService():
    def createTask(self, task:Task):
        try:
            taskDB = TaskDB(name=task.name, description=task.description, done=task.done)
            db.session.add(taskDB)
            db.session.commit()

            return taskDB.id
        except TaskDBException as e:
            raise TaskDBException(str(e))
        
    def updateTask(self, taskId, updatedData):
        try:
            taskDB = TaskDB.query.get(taskId)
        
            if(taskDB is None):
                return None
            
            taskDB.name = updatedData.get("name", taskDB.name)
            taskDB.description = updatedData.get("description", taskDB.description)
            taskDB.done = updatedData.get("done", taskDB.done)

            db.session.commit()
            
            return True
        except TaskDBException as e:
            raise TaskDBException(str(e))
       
    def deleteTask(self, taskId):
        try:
            taskDB = TaskDB.query.get(taskId)

            if(taskDB is None):
                return None
            
            db.session.delete(taskDB)
            db.session.commit()
            
            return True
        except TaskDBException as e:
            raise TaskDBException(str(e))
        
    def getAllTasks(self):
        try:
            return Serializer.serialize_list(TaskDB.query.all()) 
        except TaskDBException as e:
            raise TaskDBException(str(e))
    
    def getTask(self, taskId):
        try:
            taskDB = TaskDB.query.get(taskId)

            if(taskDB is None):
                return None

            return taskDB.serialize()
        except TaskDBException as e:
            raise TaskDBException(str(e))