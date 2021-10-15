# r-lstm-qqpdataset
This is an implementation of *Neural Paraphrase Generation with Stacked Residual LSTM Networks* in [Quora dataset](https://data.quora.com/First-Quora-Dataset-ReleaseQuestion-Pairs). We divided different training and test sets and evaluated the model with Metrics (BLEU and METERO) in them. And we compare this model in Quora with our designed model. 

## Baseline Model
we train 3 different  models in Quora.<br />
R-LSTM-138: The Stacked Residual LSTM Networks trained in 138K shuffling data in Quora.<br />
R-LSTM-143: The Stacked Residual LSTM Networks trained in 143K shuffling data in Quora.<br />
T5-138: Our model trained in 138K shuffling data in Quora.

## Metrics Evaluation Comparison

### Result in 5K testing data
| Model | BLEU | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4| METERO|
|-------|------|--------|--------|--------|-------|-------|
|R-LSTM-138 | 20.65 | 52.50 | 26.30 | 15.10 | 8.70 | 0.28 |
|R-LSTM-143 | 29.95 | 60.80 | 35.70 | 23.90 | 16.50 | 0.31 |
|T5-138(our model) | 26.15 | 61.20| 34.00 | 20.70 | 12.50 | 0.31 |
 
 ### Result in 12K testing data
| Model | BLEU | BLEU-1 | BLEU-2 | BLEU-3 | BLEU-4| METERO|
|-------|------|--------|--------|--------|-------|-------|
|R-LSTM-138 | 35.40 | 67.20 | 43.40 | 31.20 | 23.10 | 0.33 |
|R-LSTM-143 | 36.26 | 68.30 | 44.60 | 32.70 | 24.70 | 0.31 |
|T5-138(our model) | 34.66 | 71.10 | 45.70 | 32.00 | 23.00 | 0.34 |

## Generated Sentences Comparison

| Source | asd asd asd as |
|--------|----------------|
|R-LSTM-138| asd asd asd |
|R-LSTM-143| asd asd asd |
|T5-138(our model)| asd asd asd |
|Target| asd asd asd |
