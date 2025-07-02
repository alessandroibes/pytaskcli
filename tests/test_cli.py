import pytest

from pytaskcli.cli import get_parser, dispatch_command


@pytest.fixture
def dummy_db():
    return {}


def test_add_command_parsing():
    parser = get_parser()
    args = parser.parse_args(["add", "Do homework"])
    assert args.command == "add"
    assert args.description == "Do homework"


def test_update_command_parsing():
    parser = get_parser()
    args = parser.parse_args(["update", "1", "New task"])
    assert args.command == "update"
    assert args.id == "1"
    assert args.description == "New task"


def test_dispatch_add(monkeypatch, dummy_db):
    called = {}

    def mock_add(db, description):
        called["description"] = description
        return {"1": {"description": description}}


def test_dispatch_add(monkeypatch, dummy_db):
    called = {}

    def mock_add(db, description):
        called["description"] = description
        return {"1": {"description": description}}

    monkeypatch.setattr("pytaskcli.cli.core.add_task", mock_add)
    parser = get_parser()
    args = parser.parse_args(["add", "Read a book"])
    result = dispatch_command(args, dummy_db)
    assert called["description"] == "Read a book"
    assert result["1"]["description"] == "Read a book"
