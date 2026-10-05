// app.test.js — Node CDK fixture assertions.
//
// Responsibilities
// - Exercise CDK imports and deterministic offline template output.
//
// Maintainer Notes
// - Keep canonical sources shared by locked and unlocked fixture jobs.
const { test } = require('node:test');
const { Template } = require('aws-cdk-lib/assertions');
const { stack } = require('./app');
test('synthesizes the expected output without AWS credentials', () => {
  Template.fromStack(stack).resourceCountIs('AWS::SQS::Queue', 1);
  Template.fromStack(stack).hasOutput('Message', { Value: 'fixture' });
});
