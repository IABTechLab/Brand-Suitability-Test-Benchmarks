from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import average_precision_score
import pandas as pd
import argparse
from typing import Optional, Set, Tuple


def convert_labels_to_booleans(df: pd.DataFrame, higher_level: Optional[str] = None) -> pd.DataFrame:
    high_labels: Set[str] = set()
    if higher_level == 'floor':
        high_labels = {'floor'}
    elif higher_level == 'high':
        high_labels = {'floor', 'high'}
    elif higher_level == 'medium':
        high_labels = {'floor', 'high', 'medium'}
    df['is_high'] = df.label.isin(high_labels)
    return df


def calc_error_metrics(
        labels: pd.DataFrame,
        predictions: pd.DataFrame,
        higher_level: Optional[str] = None
) -> Tuple[str, float]:
    joined = labels.merge(predictions, on='url', how='inner')
    if labels.shape[0] != predictions.shape[0] != joined.shape[0]:
        raise ValueError(f'Shape of label ({labels.shape[0]}, predictions ({predictions.shape[0]}),'
                         f'and joined ({joined.shape[0]}) are not the same.')
    if joined.dtypes['prediction'] == 'float':
        joined = convert_labels_to_booleans(joined, higher_level)
        ap = average_precision_score(y_true=joined.is_high, y_score=joined.prediction)
        return 'Average Precision', ap
    else:
        ba = balanced_accuracy_score(y_true=joined.label, y_pred=joined.prediction)
        return 'Balanced Accuracy', ba


def main() -> None:
    help_msg = '''
        Command line tool to evaluate brand suitability predictions.  The predictions may be either labels with the
        words "low", "medium", "high", or "floor" or floating point numbers between 0 and 1.  If the predictions
        are numeric then an additional argument called level must be supplied to indicate which two levels
        are being differentiated against.
    '''
    parser = argparse.ArgumentParser(description=help_msg)
    parser.add_argument(
        '-l',
        '--labels',
        default='video/youtube.csv',
        required=True,
        type=argparse.FileType('r', encoding='UTF-8'),
        help='CSV file containing ground truth. Should have at least two columns, label and URL.'
    )
    parser.add_argument(
        '-p',
        '--predictions',
        required=True,
        type=argparse.FileType('r', encoding='UTF-8'),
        help='CSV file containing predictions.  Should have at least two columns, prediction and url.  Predictions may '
             'either be a string with one of "low", "medium", "high", "floor" or a float between 0 and 1.'
    )
    parser.add_argument(
        '--level',
        help='One of "medium", "high", or "floor".  This argument is used when the predictions are numeric to '
             'state which two levels the score is differentiating between.  This argument is the higher level.',
        default='high',
        choices=['floor', 'high', 'medium']
    )
    args = parser.parse_args()
    labels = pd.read_csv(args.labels)
    predictions = pd.read_csv(args.predictions)
    metrics = calc_error_metrics(labels, predictions)
    print(f'{metrics[0]}: {metrics[1]}')


if __name__ == "__main__":
    main()
