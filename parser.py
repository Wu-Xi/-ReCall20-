import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dataset', type=str, default='music-ori-KG3,music-ori-KG8',
                        help='which dataset to train(dataset: book, movie1m, music, restaurant, movie20m)')
    parser.add_argument('-b', '--batch_size', type=int, default=32, help='set the batch size of training')
    parser.add_argument('-t', '--tune', type=int, default=0, help='tune the parameters.')
    parser.add_argument('-m', '--model', type=str, default='fmgcn1',help='which module to choice(module: gcn, hgcn...)')
    parser.add_argument('-D', '--dim', type=int, default=4, help='embedding dimension')
    parser.add_argument('-h1', '--hidden1', type=int, default=64, help='the hidden_1 is u_hidden_size')
    parser.add_argument('-h2', '--hidden2', type=int, default=32, help='the hidden_2 is i_hidden_size')
    parser.add_argument('-H', '--heads', type=int, default=2, help="the number of GAT'heads")
    parser.add_argument('-C', '--cat', type=int, default=1, help="Is Inner product(0) or Concatenation(1)？")
    parser.add_argument('-L', '--loss', type=str, default='BPR', help="Loss to choose: BCE or BPR")
    parser.add_argument('-Depth', '--num_layers', type=int, default=1, help="number of layers of hetergcn")

    parser.add_argument('-ci', '--c_in', type=float, default=1., help='the curvature in for hnn(c) and hgcn')
    parser.add_argument('-co', '--c_out', type=float, default=1.0, help='the curvature out for hgcn')
    parser.add_argument('-do', '--dropout', type=float, default=0., help='the dropout for hyperbolic param')
    parser.add_argument('-E', '--epochs', type=int, default=300, help='the epochs of the training')
    parser.add_argument('-l', '--lr', type=float, default=1e-4, help='learning rate') # 1e-4
    parser.add_argument('-w', '--l2_weight_decay', type=float, default=1e-4, help='l2_weight_decay')
    parser.add_argument('-e', '--early_stop_patience', type=int, default=20, help='the parameter for stopping early')
    parser.add_argument('-ctr', '--show_ctr', type=int, default=1, help="1:show ctr;0:don't show ctr")
    parser.add_argument('-topk', '--show_topk', type=int, default=0, help="1:show topk;0:don't show topk")
    parser.add_argument('-time', '--show_time', type=int, default=1, help="1:show time;0:don't show time")
    parser.add_argument('-M', '--mode', type=str, default='train', help="train model;load model")
    parser.add_argument('--fermi', type=int, default=0, help='1:use fermiDiracDecoder;0: linear')
    parser.add_argument('--param_c', type=int, default=0, help='1:training c_in,c_out;0: fixed')
    parser.add_argument('--clamp', type=int, default=0, help='1:using clamp;0: softplus')
    parser.add_argument('--coldstartexp', type=bool, default=False, help='True:cold start experiment;False:normal experiment')
    parser.add_argument('--cl_weight', type = float, default = 0.0, help='Contrastive loss weight')
    parser.add_argument('--edge_retain', type = float, default = 0.8, help = "Edge retrain percentage for contrastive learning")
    parser.add_argument('--gpu', type = int, default = 0, help = "which gpu to use, -1 indicates uses cpu")
    parser.add_argument('--temperature', type = float, default = 0.5, help = "temperature for contrastive learning")
    parser.add_argument('--use_graphsaint', type=bool, default=False, help='True:use graph saint;False:do not use graphsaint')

    return parser.parse_args()
