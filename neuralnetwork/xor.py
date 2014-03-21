from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import TanhLayer
from pybrain.structure import SoftmaxLayer

net = buildNetwork(2, 30, 1, bias=True,hiddenclass=TanhLayer)

ds = SupervisedDataSet(2, 1)
ds.addSample((0, 0), (0,))
ds.addSample((0, 0), (0,))
ds.addSample((0, 0), (0,))
ds.addSample((0, 0), (0,))
ds.addSample((0, 0), (0,))

ds.addSample((0, 1), (1,))
ds.addSample((0, 1), (1,))
ds.addSample((0, 1), (1,))
ds.addSample((0, 1), (1,))
ds.addSample((0, 1), (1,))
ds.addSample((0, 1), (1,))

ds.addSample((1, 0), (1,))
ds.addSample((1, 0), (1,))
ds.addSample((1, 0), (1,))
ds.addSample((1, 0), (1,))
ds.addSample((1, 0), (1,))

ds.addSample((1, 1), (0,))
ds.addSample((1, 1), (0,))
ds.addSample((1, 1), (0,))
ds.addSample((1, 1), (0,))
ds.addSample((1, 1), (0,))
ds.addSample((1, 1), (0,))

print "Training starts"
trainer = BackpropTrainer(net, ds)
trainer.trainUntilConvergence()
print "Training stops"

print net.activate([0, 0])
print net.activate([0, 1])
print net.activate([1, 0])
print net.activate([1, 1])