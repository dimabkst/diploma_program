import json


def put_data_to_file(file_path: str, data: dict) -> None:
    """

    :param file_path: string with path to the file to put into
    :param data: data to put into the file
    :return: None
    """
    try:
        with open(file_path, "w") as write_file:
            json.dump(data, write_file)

    except Exception as e:
        raise e
