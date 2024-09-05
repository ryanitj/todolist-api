from flask import request
from flask_smorest import Blueprint
from api.http.controllers.taskController import TaskController 
from api.http.schemas.task import TaskSchema, TaskSchemaStore, TaskSchemaUpdate
from api.decorators.auth import auth_route

task_controller = TaskController()
task_blueprint = Blueprint("task", __name__, url_prefix="/api")

@task_blueprint.route("/tasks", methods=["GET"])
@task_blueprint.arguments(TaskSchema)
@auth_route
@task_blueprint.doc(
    summary="Get all tasks",
    description="Returns an array of all tasks.",
    tags=['task'],
    responses={
        200: {
            "description": "Tasks retrieved successfully",
        },
        500: {
            "description": "Internal server error"
        },
        401: {
            "description": "Not Authorized"
        },
    }
)
def getAllTasks(item_data):
    return task_controller.getAllTasks()

@task_blueprint.route("/tasks", methods=["POST"])
@task_blueprint.arguments(TaskSchemaStore)
@auth_route
@task_blueprint.doc(
    summary="Create a task",
    description="Create a new task with the provided details",
    tags=['task'],
    parameters=[
        {
            'in': 'body',
            'name': 'name',
            'description': 'Name of the task',
            'required': True,
            'type': "string"
        },
         {
            'in': 'body',
            'name': 'description',
            'description': 'Description of the task',
            'required': False,
            'type': "string"
        },
    ],
    responses={
        200: {
            "description": "Tasks created successfully",
        },
        400: {
            "description": "Bad request - Invalid input data"
        },
        500: {
            "description": "Internal server error"
        },
        401: {
            "description": "Not Authorized"
        },
    }
)
def createTask(task_data):
    data = task_data
    return task_controller.createTask(data)

@task_blueprint.route("/tasks/<int:id>", methods=["GET"])
@auth_route
@task_blueprint.doc(
    summary="Get a single task",
    description="Return a single task",
    tags=['task'],
    parameters=[
        {
            'in': 'query',
            'name': 'id',
            'description': 'Id of the task',
            'required': True,
            'schema': {
                'type': 'string',
            }
        }
    ],
    responses={
        200: {
            "description": "Task retrieved successfully",
            "content": {
                "application/json": {
                    "schema": TaskSchema
                }
            }
        },
        400: {
            "description": "Bad request - Invalid input data"
        },
        500: {
            "description": "Internal server error"
        },
        401: {
            "description": "Not Authorized"
        },
    }
)
def getTask(id):
    return task_controller.getTask(id)

@task_blueprint.route("/tasks/<int:id>", methods=["DELETE"])
@auth_route
@task_blueprint.doc(
    summary="Delete a task",
    description="Delete a single task",
    tags=['task'],
    parameters=[
        {
            'in': 'query',
            'name': 'id',
            'description': 'Id of the task',
            'required': True,
            'schema': {
                'type': 'string',
            }
        },
    ],
    responses={
        200: {
            "description": "Task deleted successfully",
        },
        400: {
            "description": "Bad request - Invalid input data"
        },
        500: {
            "description": "Internal server error"
        },
        401: {
            "description": "Not Authorized"
        },
    }
)
def deleteTask(id):
    return task_controller.deleteTask(id)

@task_blueprint.route("/tasks/<int:id>", methods=["PUT"])
@task_blueprint.arguments(TaskSchemaUpdate)
@auth_route
@task_blueprint.doc(
    summary="Updated a task",
    description="Updated a single task",
    tags=['task'],
    parameters=[
        {
            'in': 'query',
            'name': 'id',
            'description': 'Id of the task',
            'required': True,
            'schema': {
                'type': 'string',
            }
        },
        {
            'in': 'body',
            'name': 'name',
            'description': 'Name of the task',
            'required': False,
            'type': "string"
        },
         {
            'in': 'body',
            'name': 'description',
            'description': 'Description of the task',
            'required': False,
            'type': "string"
        },
        
    ],
    responses={
        200: {
            "description": "Task updated successfully",
        },
        400: {
            "description": "Bad request - Invalid input data"
        },
        500: {
            "description": "Internal server error"
        },
        401: {
            "description": "Not Authorized"
        },
    }
)
def updateTask(task_data, id):
    return task_controller.updateTask(id, task_data)