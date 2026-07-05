import torch
y = torch.tensor([0,1,2])
y_hat = torch.tensor([[0.1, 0.3, 0.6], [0.3, 0.2, 0.5],[0.4, 0.2, 0.5]])
X = torch.tensor([[1.0, 2.0, 3.0],
                  [1.0, 2.0, -1.0]])
print(X.numel())