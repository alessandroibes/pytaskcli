from unittest.mock import patch, MagicMock
from pytaskcli import main


def test_main_add_command(capsys):
    # Mock the parser to simulate `add "Test task"`
    mock_args = MagicMock()
    mock_args.command = "add"
    mock_args.description = "Test task"

    with patch("pytaskcli.main.get_parser") as mock_parser, \
         patch("pytaskcli.main.load_database", return_value={}), \
         patch("pytaskcli.main.save_database") as mock_save, \
         patch("pytaskcli.main.dispatch_command", return_value={"1": {
             "description": "Test task", "status": "todo", "created-at": "2024-01-01T10:00:00", "updated-at": "2024-01-01T10:00:00"
         }}):
        
        mock_parser.return_value.parse_args.return_value = mock_args
        main.main()

        out = capsys.readouterr().out
        assert "Test task" in out
        mock_save.assert_called_once()


def test_main_list_empty(capsys):
    mock_args = MagicMock()
    mock_args.command = "list"
    mock_args.status = "all"

    with patch("pytaskcli.main.get_parser") as mock_parser, \
         patch("pytaskcli.main.load_database", return_value={}), \
         patch("pytaskcli.main.save_database"), \
         patch("pytaskcli.main.dispatch_command", return_value=[]):

        mock_parser.return_value.parse_args.return_value = mock_args
        main.main()

        out = capsys.readouterr().out
        assert "Nothing to display" in out
