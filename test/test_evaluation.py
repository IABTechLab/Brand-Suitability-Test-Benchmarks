import pandas as pd
import evaluation
import pytest


def test_labels():
    labels = pd.DataFrame.from_dict({'Label': ['HIGH', 'MEDIUM', 'LOW'], 'URL': ['a', 'b', 'c']})
    predictions = pd.DataFrame.from_dict({'Prediction': ['HIGH', 'LOW', 'LOW'], 'URL': ['a', 'b', 'c']})
    result = evaluation.calc_error_metrics(labels, predictions)
    assert 2/3 == pytest.approx(result[1])


def test_convert_label():
    labels = pd.DataFrame.from_dict({'Label': ['HIGH', 'LOW', 'LOW'], 'URL': ['a', 'b', 'c']})
    expected = labels.copy(deep=True)
    expected['is_high'] = [True, False, False]
    result = evaluation.convert_labels_to_booleans(labels, 'HIGH')
    assert expected.equals(result)


def test_float():
    labels = pd.DataFrame.from_dict({'Label': ['HIGH', 'MEDIUM', 'MEDIUM'], 'URL': ['a', 'b', 'c']})
    predictions = pd.DataFrame.from_dict({'Prediction': [0.8, 0.7, 0.2], 'URL': ['a', 'b', 'c']})
    result = evaluation.calc_error_metrics(labels, predictions, 'HIGH')
    assert result[1] == 1
