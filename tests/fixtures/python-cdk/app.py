"""Credential-free synthesis fixture, never deployed."""

from aws_cdk import App, RemovalPolicy, Stack
from aws_cdk.aws_sqs import Queue, QueueEncryption


def create_stack() -> Stack:
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
