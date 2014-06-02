def getData():
    import xlrd

    excel_file = xlrd.open_workbook("PLKGHM000017.xls")
    first_sheet = excel_file.sheets()[0]

    data = []
    for cell in first_sheet.col(9):
        try:
            data_float = float(cell.value)/100.0
        except ValueError:
            pass
        else:
            data.append(data_float)

    return data

def train(data):
    from pybrain.tools.shortcuts import buildNetwork
    from pybrain.supervised.trainers import BackpropTrainer
    from pybrain.datasets import SupervisedDataSet

    INPUT = 10
    HIDDEN = 40
    OUTPUT = 1

    data_set = SupervisedDataSet(INPUT,OUTPUT)
    for idx,element in enumerate(data):
        input_data = (data[idx],
                      data[idx + 1],
                      data[idx + 2],
                      data[idx + 3],
                      data[idx + 4],
                      data[idx + 5],
                      data[idx + 6],
                      data[idx + 7],
                      data[idx + 8],
                      data[idx + 9],
                     )

        try:
            output_data = (data[idx + 10])
        except IndexError:
            break

        data_set.addSample(input_data,output_data)

    print "Training Data set length: " + str(len(data_set))

    net = buildNetwork(INPUT,HIDDEN,OUTPUT)
    trainer = BackpropTrainer(net,data_set)
    trainer.trainUntilConvergence()

    return net

if __name__ == "__main__":
    import pickle
    import datetime

    start_time = datetime.datetime.now()
    print start_time
    data = getData()
    net = train(data)
    end_time = datetime.datetime.now()
    print end_time

    print "Last 10 days data:   " + " ".join([str(num) for num in data[-10:]])
    print "Next day prediction: " + str(net.activate(data[-10:])[0])

    print "Calculation took:    " + str((end_time - start_time).total_seconds()/60) + " Min"
    with open("net.pck","wb") as fp:
        net_str = pickle.dump(net,fp)

