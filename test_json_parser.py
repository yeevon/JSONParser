import os
import pytest
from json_parser import hard_parse_json

def get_test_files(folder_path):
    return [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, file))
    ]

def test_step1():
    file_names = get_test_files('test_data/step1/')

    for name in file_names:
        expected_exit_code = 1 if 'inval' in name.lower() else 0

        with pytest.raises(SystemExit) as exec_info:
            hard_parse_json(name)
        assert exec_info.value.code == expected_exit_code


def test_step2():
    file_names = get_test_files('test_data/step2/')

    for name in file_names:
        expected_exit_code = 1 if 'inval' in name.lower() else 0

        with pytest.raises(SystemExit) as exec_info:
            print(name)
            hard_parse_json(name)
        assert exec_info.value.code == expected_exit_code

def test_step3():
    file_names = get_test_files('test_data/step3/')

    for name in file_names:
        expected_exit_code = 1 if 'inval' in name.lower() else 0

        with pytest.raises(SystemExit) as exec_info:
            print(name)
            hard_parse_json(name)
        assert exec_info.value.code == expected_exit_code

def test_step4():
    file_names = get_test_files('test_data/step4/')

    for name in file_names:
        expected_exit_code = 1 if 'inval' in name.lower() else 0

        with pytest.raises(SystemExit) as exec_info:
            print(name)
            hard_parse_json(name)
        assert exec_info.value.code == expected_exit_code

def test_step5():
    file_names = get_test_files('test/')

    for name in file_names:
        expected_exit_code = 1 if 'fail' in name.lower() else 0

        with pytest.raises(SystemExit) as exec_info:
            print(name)
            hard_parse_json(name)
        assert exec_info.value.code == expected_exit_code