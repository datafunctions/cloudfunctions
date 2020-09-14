import os

project_id = os.environ.get('GCP_PROJECT')
print(project_id)


def main_function(event, context):
    print('hello from the directory github deployment')
    pass