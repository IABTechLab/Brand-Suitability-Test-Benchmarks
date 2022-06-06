import pandas as pd
import evaluation
import pytest


def test_labels() -> None:
    labels = pd.DataFrame.from_dict({'label': ['high', 'medium', 'low'], 'url': ['a', 'b', 'c']})
    predictions = pd.DataFrame.from_dict({'prediction': ['high', 'low', 'low'], 'url': ['a', 'b', 'c']})
    result = evaluation.calc_error_metrics(labels, predictions)
    assert 2/3 == pytest.approx(result[1])


def test_convert_label() -> None:
    labels = pd.DataFrame.from_dict({'label': ['high', 'low', 'low'], 'url': ['a', 'b', 'c']})
    expected = labels.copy(deep=True)
    expected['is_high'] = [True, False, False]
    result = evaluation.convert_labels_to_booleans(labels, 'high')
    assert expected.equals(result)


def test_float() -> None:
    labels = pd.DataFrame.from_dict({'label': ['high', 'medium', 'medium'], 'url': ['a', 'b', 'c']})
    predictions = pd.DataFrame.from_dict({'prediction': [0.8, 0.7, 0.2], 'url': ['a', 'b', 'c']})
    result = evaluation.calc_error_metrics(labels, predictions, 'high')
    assert result[1] == 1
