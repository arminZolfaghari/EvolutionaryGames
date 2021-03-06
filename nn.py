import numpy as np
from config import CONFIG


# input layer isn't normal, have to normalize
def normalize_input_layer(input_layer):
    pass
    max_width = CONFIG['WIDTH']
    max_height = CONFIG['HEIGHT']
    input_layer[0][0], input_layer[1][0] = input_layer[0][0] / max_width, input_layer[1][0]/ max_height
    input_layer[2][0], input_layer[3][0] = input_layer[2][0] / max_width, input_layer[3][0]/ max_height
    input_layer[4][0] = input_layer[4][0] / 1469
    input_layer[5][0] = input_layer[5][0] / 10
    #
    # input_layer[5], input_layer[6] = input_layer[5] / max_width, input_layer[6] / max_height


class NeuralNetwork():
    def __init__(self, layer_sizes, mode):
        n_x = layer_sizes[0]
        n_h1 = layer_sizes[1]
        n_y = layer_sizes[2]
        self.mode = mode
        # TODO
        # layer_sizes example: [4, 10, 2]

        # print("n_x, n_h1, n_y ", n_x, n_h1, n_y)
        # self.W1 = np.random.randn(n_h1, n_x)

        self.W1 = np.random.normal(size=(n_h1, n_x))
        self.W2 = np.random.normal(size=(n_y, n_h1))
         # self.W2 = np.random.randn(n_y, n_h1)
        self.b1 = np.random.normal(size=(n_h1, 1))
        self.b2 = np.random.normal(size=(n_y, 1))

        # elif self.mode == "gravity":
        #     self.b1 = np.zeros((n_h1, 1))
        #     self.b2 = np.zeros((n_y, 1))
        #     self.W1 = np.random.normal(0, 1, (n_h1, n_x))
        #     self.W2 = np.random.normal(0, 1, (n_y, n_h1))

        # self.W1 = np.random.uniform(-0.5, 0.5, (n_h1, n_x))
        # self.W2 = np.random.uniform(-0.5, 0.5, (n_y, n_h1))
        # self.W1 = np.random.normal(0, 1, (n_h1, n_x))
        # self.W2 = np.random.normal(0, 1, (n_y, n_h1))
        # print(self.W1)
        # print(self.W2)
        # print(self.b1)
        # print(self.b2)

    # sigmoid function
    def activation(self, x):
        return 1 / (1 + np.exp(-x))

    # # this function calculate next A with A_prev, W and b
    # def linear_activation_forward(self, A_prev, W, b, activationType):
    #     if activationType == "sigmoid":
    #         Z = (W @ A_prev) + b
    #         A = activation(Z)

    def forward(self, input_layer):
        # print(input_layer)
        normalize_input_layer(input_layer)
        # print(input_layer)
        # TODO
        # x example: np.array([[0.1], [0.2], [0.3]])
        self.A0 = input_layer
        Z1 = (self.W1 @ self.A0) + self.b1
        A1 = self.activation(Z1)
        Z2 = (self.W2 @ A1) + self.b2
        A2 = self.activation(Z2)
        return A2
