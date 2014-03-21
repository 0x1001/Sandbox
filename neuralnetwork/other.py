from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import TanhLayer
from pybrain.structure import SoftmaxLayer

net = buildNetwork(3, 200, 3)

ds = SupervisedDataSet(3, 3)
for i in range(5):
    ds.addSample((1, 2, 3), (1, 1, 1))
    ds.addSample((4, 3, 4), (7, 5, 6))
    ds.addSample((5, 5, 5), (7, 8, 1))
    ds.addSample((2, 7, 6), (3, 1, 1))
    ds.addSample((3, 3, 1), (1, 200, 1))

print "Training starts"
trainer = BackpropTrainer(net, ds)
trainer.trainUntilConvergence()
print "Training stops"

print net.activate([1, 2, 3])
print net.activate([4, 3, 4])
print net.activate([5, 5, 5])
print net.activate([2, 7, 6])
print net.activate([3, 3, 1])