# tests/fixtures/python-cdk/test_app.py
# Dagitali shared automation library
#
# Responsibilities: Exercise Python CDK imports and deterministic offline
# template generation.
#
# Maintainer Notes: Keep fixture/test effects isolated; do not duplicate Popo
# policy logic.

"""Exercise Python CDK imports and deterministic offline template generation."""

from app import create_stack
from aws_cdk.assertions import Template


def test_queue_template() -> None:
    """Assert the offline template contains one encrypted SQS queue."""
    template = Template.from_stack(create_stack())
    template.resource_count_is("AWS::SQS::Queue", 1)
    template.has_resource_properties("AWS::SQS::Queue", {"SqsManagedSseEnabled": True})
