import boto3
import click

s3 = boto3.resource('s3')

@click.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

if __name__ == '__main__':
    list_buckets()
