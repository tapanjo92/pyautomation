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

if __name__ == '__main__':
    cli()
