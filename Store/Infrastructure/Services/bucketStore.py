from Infrastructure.Config.ConfigBucketStore import client
import mimetypes


def send_file(file_name, bucket_name, store_uuid, object_name=None):
    if object_name is None:
        object_name = file_name

    content_type, _ = mimetypes.guess_type(file_name)
    if content_type is None:
        content_type = 'application/octet-stream'
    try:
        response = client.upload_file(
            file_name, bucket_name, object_name, ExtraArgs={'ACL': 'public-read', 'Metadata': {'uuid': str(store_uuid)},  'ContentType': content_type})
    except Exception as e:
        print(e)
        return False
