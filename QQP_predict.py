import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import logging
import tensorflow as tf
from seq2seq import Seq2seq
from data_handler import Data
from IPython import embed

FLAGS = tf.app.flags.FLAGS

# Model related
tf.flags.DEFINE_integer('num_units'         , 256           , 'Number of units in a LSTM cell')
tf.flags.DEFINE_integer('embed_dim'         , 256           , 'Size of the embedding vector')

# Training related
tf.flags.DEFINE_float('learning_rate'       , 0.001         , 'learning rate for the optimizer')
tf.flags.DEFINE_string('optimizer'          , 'Adam'        , 'Name of the train source file')
tf.flags.DEFINE_integer('batch_size'        , 32            , 'random seed for training sampling')
tf.flags.DEFINE_integer('print_every'       , 100           , 'print records every n iteration')
tf.flags.DEFINE_integer('iterations'        , 12000         , 'number of iterations to train')
tf.flags.DEFINE_string('model_dir', 'QQPcheckpoints', 'Directory where to save the model')

tf.flags.DEFINE_integer('input_max_length'  , 30            , 'Max length of input sequence to use')
tf.flags.DEFINE_integer('output_max_length' , 30            , 'Max length of output sequence to use')

tf.flags.DEFINE_bool('use_residual_lstm'    , True          , 'To use the residual connection with the residual LSTM')

# Data related
tf.flags.DEFINE_string('input_filename', 'data/QQPPos/train/src.txt', 'Name of the train source file')
tf.flags.DEFINE_string('output_filename', 'data/QQPPos/train/tgt.txt', 'Name of the train target file')
tf.flags.DEFINE_string('vocab_filename', 'data/QQPPos/QQP_vocab.txt', 'Name of the vocab file')

class Predict:
    def __init__(self):
        self.data  = Data(FLAGS)
        model = Seq2seq(self.data.vocab_size, FLAGS)
        estimator = tf.estimator.Estimator(model_fn=model.make_graph, model_dir=FLAGS.model_dir)
        def input_fn():
            inp = tf.placeholder(tf.int64, shape=[None, None], name='input')
            output = tf.placeholder(tf.int64, shape=[None, None], name='output')
            tf.identity(inp[0], 'source')
            tf.identity(output[0], 'target')
            dict =  { 'input': inp, 'output': output}
            return tf.estimator.export.ServingInputReceiver(dict, dict)

        self.predictor = tf.contrib.predictor.from_estimator(estimator, input_fn)

    def infer(self, sentence):
        input = self.data.prepare(sentence)
        # output = self.data.prepare(sentence2)
        predictor_prediction = self.predictor({"input": input, "output":input})
        words = [self.data.rev_vocab.get(i, '<UNK>') for i in predictor_prediction['output'][0] if i > 2]
        return ' '.join(words)

def main(args):
    P = Predict()
    # print(P.infer('why do some people like cats more than dogs ?'))
    # print(P.infer('why the bat and ball games like cricket are not included in the olympic games ?'))
    # print(P.infer('what are some safe and legal ways to view a private facebook profile ?'))
    # print(P.infer('what helps you pass a meth test ?'))
    generate_list = []
    with open('data/QQPPos/test/src_test_12000.txt', 'r',encoding='UTF-8') as f:
        f_lines = f.readlines()
        for line in f_lines:
            # print(P.infer(line))
            generate_list.append(P.infer(line))

    with open('data/QQPPos/test/N138-ckpt-28036_R-LSTM_T12000.txt', 'w') as f:
        for gen in generate_list:
            f.write(gen+'\n')



if __name__ == "__main__":
    tf.app.run()
