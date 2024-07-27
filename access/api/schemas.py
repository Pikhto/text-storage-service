from marshmallow import EXCLUDE, Schema, fields, validate


class AccessGrantRequestSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    text_id = fields.String(required=True)
    user_id = fields.UUID(required=True)
    permission = fields.String(
        required=True, validate=validate.OneOf(["read", "write"])
    )


class AccessGrantResponseSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    access_granted = fields.Boolean()
