import io
from googleapiclient.http import MediaIoBaseDownload
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import os
import logging
from .log import info
obj = lambda: None

SCOPES = 'https://www.googleapis.com/auth/drive.readonly'


@info
def get_gdrive_service():
    """

    :return:
    """
    obj = lambda: None
    lmao = {"auth_host_name": 'localhost', 'noauth_local_webserver': 'store_true', 'auth_host_port': [8080, 8090],
            'logging_level': 'ERROR'}
    for k, v in lmao.items():
        setattr(obj, k, v)

    store = file.Storage('token.json')
    creds = store.get()
    # The following will give you a link if token.json does not exist, the link allows the user to give this app permission
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store, obj)
    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))
    return DRIVE


@info
def search(service, query):
    """

    :param service:
    :param query:
    :return:
    """
    # search for the file
    result = []
    page_token = None
    while True:
        response = service.files().list(q=query,
                                        spaces="drive",
                                        fields="nextPageToken, files(id, name, mimeType)",
                                        pageToken=page_token).execute()
        # iterate over filtered files
        for file in response.get("files", []):
            print(f"Found file: {file['name']} with the id {file['id']} and type {file['mimeType']}")
            result.append((file["id"], file["name"], file["mimeType"]))
        page_token = response.get('nextPageToken', None)
        if not page_token:
            # no more files
            break
    return result


@info
def download_file_from_google_drive(DRIVE, file_id, file_name):
    """

    :param DRIVE:
    :param file_id:
    :param file_name:
    :return:
    """

    request = DRIVE.files().get_media(fileId=file_id)
    fh = io.FileIO(file_name, mode='w')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print('status, done', status, done)
        print("Download %d%%." % int(status.progress() * 100))
        logging.info('Download %d%%.'% int(status.progress()*100))


@info
def download(filename):
    """

    :param filename:
    :return:
    """
    try:

        service = get_gdrive_service()
        # search for the file by name
        search_result = search(service, query=f"name='{filename}'")
        logging.info('Search result: {}'.format(search_result))
        if search_result:
            # get the GDrive ID of the file
            file_id = search_result[0][0]
            print('file_id', file_id)
            logging.info('file id: {}'.format(file_id))
            download_file_from_google_drive(service, file_id, filename)
        else:
            print('Please enter valid file Name')
            logging.info('Please enter valid file Name')
    except Exception as e:
        logging.error('Error occurred while downloading file from Gdrive: {}'.format(e))

# Testing purpose
# if __name__ == '__main__':
    # filename = "********"
    # download(filename)