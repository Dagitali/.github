# tests/fixtures/python-cdk/app.py
# Dagitali shared automation library
#
# Responsibilities
# - Credential-free synthesis fixture, never deployed.
#
# Maintainer Notes
# - Keep fixture/test effects isolated; do not duplicate Popo policy logic.

"""Credential-free synthesis fixture, never deployed."""

from aws_cdk import App, RemovalPolicy, Stack
from aws_cdk.aws_sqs import Queue, QueueEncryption


def create_stack() -> Stack:
    """Return an environment-agnostic SQS stack for offline tests and synthesis; never deploy it."""
    app = App()
    stack = Stack(app, "PythonFixture")
    Queue(
        stack,
        "Queue",
        encryption=QueueEncryption.SQS_MANAGED,
        enforce_ssl=True,
        removal_policy=RemovalPolicy.DESTROY,
    )
    return stack


if __name__ == "__main__":
    create_stack().node.root.synth()
