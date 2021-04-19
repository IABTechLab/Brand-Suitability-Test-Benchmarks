import unittest
import evaluation
import pandas as pd


class TestEvaluation(unittest.TestCase):

    def test_labels(self):
        labels = pd.DataFrame.from_dict({'Label': ['HIGH', 'MEDIUM', 'LOW'], 'URL': ['a', 'b', 'c']})
        predictions = pd.DataFrame.from_dict({'Prediction': ['HIGH', 'LOW', 'LOW'], 'URL': ['a', 'b', 'c']})
        result = evaluation.calc_error_metrics(labels, predictions)
        self.assertAlmostEqual(result[1], 2/3)

    def test_convert_label(self):
        labels = pd.DataFrame.from_dict({'Label': ['HIGH', 'LOW', 'LOW'], 'URL': ['a', 'b', 'c']})
        expected = labels.copy(deep=True)
        expected['is_high'] = [True, False, False]
        result = evaluation.convert_labels_to_booleans(labels, 'HIGH')
        self.assertTrue(expected.equals(result))

    def test_float(self):
        labels = pd.DataFrame.from_dict({'Label': ['HIGH', 'MEDIUM', 'MEDIUM'], 'URL': ['a', 'b', 'c']})
        predictions = pd.DataFrame.from_dict({'Prediction': [0.8, 0.7, 0.2], 'URL': ['a', 'b', 'c']})
        result = evaluation.calc_error_metrics(labels, predictions, 'HIGH')
        self.assertEqual(result[1], 1)


if __name__ == '__main__':
    unittest.main()
