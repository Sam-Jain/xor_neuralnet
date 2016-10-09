import neuralpy

layers = [2, 10, 8, 1]
net = neuralpy.Network(layers)

#neuralpy will automatically generate random incoming weights and biases for each processing layer.


datum_1 = ([1, 1], [0])
datum_2 = ([1, 0], [1])
datum_3 = ([0, 1], [1])
datum_4 = ([0, 0], [0])

training_data = [datum_1, datum_2, datum_3, datum_4]
epochs = 300
learning_rate = 3
#monitor_cost tracks the cost of every epoch
net.train(training_data, epochs, learning_rate)

print net.forward([1,0])
print net.forward([0,0])
print net.forward([0,1])
print net.forward([1,1])