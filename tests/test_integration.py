from pathlib import Path
from unittest.mock import patch

import pytest
from black_disable_checker.__main__ import main

def test_integration():
    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == 0
    with patch('sys.argv', ['black-disable-checker', str(Path(__file__).parent / 'fixture.py')]):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == -1