import json


def retrieve_data_from_file(file_path: str) -> dict:
    """

    :param file_path: string with path to the file to read
    :return: dict with data from file
    """
    try:
        with open(file_path, "r") as read_file:
            data = json.load(read_file)

        return data
    except Exception as e:
        raise e
