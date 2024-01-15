from marshmallow import (
    Schema,
    fields,
    validate,
    EXCLUDE,
)


class GetKitchenScheduleParameters(Schema):
    class Meta:
        unknown = EXCLUDE
    progress = fields.Boolean()
    limit = fields.Integer()
    since = fields.DateTime()


class OrderItemSchema(Schema):
    class Meta:
        unknown = EXCLUDE  # We use the Meta class to ban unknown properties.

    product = fields.String(required=True)
    size = fields.String(
        required=True, validate=validate.OneOf(['small', 'medium', 'big'])
    )
    quantity = fields.Integer(
        validate=validate.Range(1, min_inclusive=True), required=True
    )


class ScheduleOrderSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    order = fields.List(fields.Nested(OrderItemSchema), required=True)


class GetScheduledOrderSchema(ScheduleOrderSchema):
    id = fields.UUID(required=True)
    scheduled = fields.DateTime(required=True)
    status = fields.String(required=True,
                           validate=validate.OneOf(
                               ["pending", "progress", "cancelled", "finished"]
                           ),
                           )


class GetScheduledOrdersSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    schedules = fields.List(fields.Nested(GetScheduledOrderSchema), required=True)


class ScheduleStatusSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    status = fields.String(
        required=True,
        validate=validate.OneOf(
            ["pending", "progress", "cancelled", "finished"]
        ),
    )
