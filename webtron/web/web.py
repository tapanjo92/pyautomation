import boto3
import click

s3 = boto3.resource('s3')

@click.group()
def cli():
    "Web deploys websites to aws"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
def list_bucket_objects():
    "Get Objects in s3"
    for obj in s3.Bucket('automatingtj-boto3').objects.all():
        print(obj)


if __name__ == '__main__':
    cli()
