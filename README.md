# r-lstm-qqpdataset
This is an implementation of *Neural Paraphrase Generation with Stacked Residual LSTM Networks* in [Quora dataset](https://data.quora.com/First-Quora-Dataset-ReleaseQuestion-Pairs). We divided different training and test sets and evaluated the model with Metrics (BLEU and METERO) in them. And we compare this model in Quora with our designed model. 

## Baseline Model
we train 4 different Stacked Residual LSTM models in different training set.<br />
R-LSTM-138: The Stacked Residual LSTM Networks trained in 138K shuffling data in Quora.<br />
R-LSTM-143: The Stacked Residual LSTM Networks trained in 143K shuffling data in Quora.<br />
N-R-LSTM-138: The Stacked Residual LSTM Networks trained in 138K shuffling data(the same as R-LSTM-138 training data) in Quora, but with richer vocabulary(28K).<br />
N-R-LSTM-143: The Stacked Residual LSTM Networks trained in 143K shuffling data(the same as R-LSTM-143 training data) in Quora, but with richer vocabulary(28K).<br />
T5: Our model trained in 138K shuffling data in Quora.

## Metrics Evaluation Comparison
20.65 52.5/26.3/15.1/8.7
### Result in 5K testing data
| Model | BLEU | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4| METERO|
|-------|------|--------|--------|--------|-------|-------|
|R-LSTM-138 | 19.80 | 52.70| 25.90 | 14.40 | 7.90 | 0.27 |
|N-R-LSTM-138 | 20.65 | 52.50 | 26.30 | 15.10 | 8.70 | 0.28 |
|R-LSTM-143 | 23.54 | 57.10| 30.40 | 18.50 | 11.20 | 0.28 |
|N-R-LSTM-143 | 29.95 | 60.80 | 35.70 | 23.90 | 16.50 | 0.31 |
|T5(our model) | 26.15 | 61.20| 34.00 | 20.70 | 12.50 | 0.31 |
 
 ### Result in 12K testing data
| Model | BLEU | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4| METERO|
|-------|------|--------|--------|--------|--------|-------|-------|
|R-LSTM-138 | 25.03 | 58.70| 36.00 | 23.80 | 16.50 | 0.28 |
|N-R-LSTM-138 |  | |  |  |  |  |
|R-LSTM-143 | 29.45 | 65.00| 39.10 | 26.20 | 18.10 | 0.30 |
|N-R-LSTM-143 | 36.26 | 68.30| 44.60 | 32.70 | 24.70 | 0.31 |
|T5(our model) |  | |  |  |  |  |

