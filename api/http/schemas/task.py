from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    done = fields.Bool(required=True)
    description = fields.Str()
    
class TaskSchemaUpdate(Schema):
    name = fields.Str()
    description = fields.Str()
    done = fields.Bool(required=True)

class TaskSchemaStore(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    done = fields.Bool(required=True)
    description = fields.Str()