import pytest
from unittest.mock import patch
from src.algorithms import divide

@patch("src.algorithms.logging.error")
def test_logging(mock_log):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
    mock_log.assert_called_with("Division by zero error")
