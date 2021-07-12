import numpy as np


class NeuralNetwork():
    def __init__(self, layer_sizes):
        n_x = layer_sizes[0]
        n_h1 = layer_sizes[1]
        n_y = layer_sizes[2]
        # TODO
        # layer_sizes example: [4, 10, 2]
        pass
        self.W1 = np.random.randn(n_h1, n_x)
        self.b1 = np.zeros((n_h1, 1))
        self.W2 = np.random.randn(n_y, n_h1)
        self.b2 = np.zeros((n_y, 1))

    # sigmoid function
    def activation(self, x):
        return 1 / (1 + np.exp(-x))

    # # this function calculate next A with A_prev, W and b
    # def linear_activation_forward(self, A_prev, W, b, activationType):
    #     if activationType == "sigmoid":
    #         Z = (W @ A_prev) + b
    #         A = activation(Z)

    def forward(self, x):
        # TODO
        # x example: np.array([[0.1], [0.2], [0.3]])
        self.A0 = x
        Z1 = (self.W1 @ self.A0) + self.b1
        A1 = self.activation(Z1)
        Z2 = (self.W2 @ A1) + self.b2
        A2 = self.activation(Z2)
