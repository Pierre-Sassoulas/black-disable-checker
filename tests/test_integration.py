from pathlib import Path
from unittest.mock import patch

import pytest

from black_disable_checker.__main__ import main

TEST_DIRECTORY = Path(__file__).parent


def test_integration_no_args() -> None:
    with patch("sys.argv", ["black-disable-checker"]):
        with pytest.raises(SystemExit) as e:
            main()
    assert e.value.code == 0


@pytest.mark.parametrize(
    "file_path,expected",
    [
        ["fmt_off", "Please do not use '# fmt: off'"],
        ["fmt_skip", "Please do not use '# fmt: skip'"],
        ["yapf_disable", "Please do not use '# yapf: disable'"],
        ["multiple", "Please do not use '# fmt: skip', or '# yapf: disable'"],
    ],
)
def test_integration(file_path: str, expected: str, capsys) -> None:
    with patch(
        "sys.argv",
        ["black-disable-checker", str(TEST_DIRECTORY / f"fixture_{file_path}.py")],
    ):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == -1
    out, err = capsys.readouterr()
    assert not out
    assert expected in err
