// app.js — Node CDK runtime fixture.
//
// Responsibilities: Build an environment-agnostic template without AWS
// lookups.
//
// Maintainer Notes: Export the stack for assertions; never deploy this
// fixture.
const cdk = require('aws-cdk-lib');
const app = new cdk.App();
const stack = new cdk.Stack(app, 'Fixture');
new cdk.CfnResource(stack, 'Queue', { type: 'AWS::SQS::Queue' });
new cdk.CfnOutput(stack, 'Message', { value: 'fixture' });
module.exports = { app, stack };
