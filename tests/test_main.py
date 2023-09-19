from unittest.mock import patch, call, mock_open
from src.main import extract_temperature_from_line, process_dat_file, write_to_csv

def test_extract_temperature_from_line():
    assert extract_temperature_from_line("TEMP 25") == "25"
    assert extract_temperature_from_line("TEMP") == None
    assert extract_temperature_from_line("OTHER 30") == None

@patch('builtins.open', mock_open(read_data="TEMP 25\nOTHER 20"))
def test_process_dat_file(mocker):
    mocker.patch('builtins.open', mock_open(read_data="TEMP 25\nOTHER 20"))
    assert process_dat_file('sample.dat') == ('sample.dat', '25')

@patch('csv.writer')
def test_write_to_csv(mock_csv_writer):
    write_to_csv([("file1.dat", "25"), ("file2.dat", "30")])
    
    # Debugging print
    print(mock_csv_writer().writerow.mock_calls)
    
    calls = [
        call(['Filename', 'Temperature']),
        call(('file1.dat', '25')),
        call(('file2.dat', '30'))
    ]
    
    mock_csv_writer().writerow.assert_has_calls(calls)
