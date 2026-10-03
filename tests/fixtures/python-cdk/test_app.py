"""Exercise Python CDK imports and deterministic offline template generation."""

from aws_cdk.assertions import Template

from app import create_stack


def test_queue_template():
    template = Template.from_stack(create_stack())
    template.resource_count_is("AWS::SQS::Queue", 1)
    template.has_resource_properties("AWS::SQS::Queue", {"SqsManagedSseEnabled": True})
