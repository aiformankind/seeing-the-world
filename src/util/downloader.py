import requests
import os
from src.util.common_lib import get_unique_time


class DownloadHelper(object):

    def __init__(self, url):
        self.url = url
        self.download_loc = os.path.abspath("{}/resources/download_images".format(os.getcwd()))

    def is_photographic(self, http_response):
        """
        Check the Contnet-Type from HTTP responses.

        :param http_response:
        :return: bool
        :raise: TypeError(): if not the right media and file format
        """
        content_type = http_response.headers.get('Content-Type').lower()
        if content_type in ["image/jpeg", "image/jpg"]:
            return True
        else:
            raise TypeError("Please choose jpeg or jpg file format and not `{}`".format(content_type))

    def is_right_file_size(self, http_response):
        """
        Check the Contnet-lenght from HTTP responses.

        :param http_response:
        :return: bool
        :raise TypeError() if the file size is over 3 Mb.
        """
        content_lenght = int(http_response.headers.get('content-length'))
        if content_lenght > 3000000:
            raise TypeError("The size of file `{}` is too big".format(content_lenght))
        else:
            return True

    def download_image(self):
        """
        Download file from Internet and gives a unique name to the new downloading file. The file
        will be stored in a default location.

        :return: str() The download path and file name
        """
        uniq_filename = "{}.jpg".format(get_unique_time())
        http_response = requests.get(self.url)
        dump = http_response.content
        file_path = os.path.join(self.download_loc, uniq_filename )
        if self.is_right_file_size(http_response) and self.is_photographic(http_response):
            open(file_path, 'wb').write(dump)

        return file_path
