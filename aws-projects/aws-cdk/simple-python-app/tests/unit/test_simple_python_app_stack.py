import aws_cdk as core
import aws_cdk.assertions as assertions

from simple_python_app.simple_python_app_stack import SimplePythonAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in simple_python_app/simple_python_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SimplePythonAppStack(app, "simple-python-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
