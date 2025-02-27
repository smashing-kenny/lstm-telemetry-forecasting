from sys import argv

if(len(argv) != 5):
    print("unit epoch batch")
    exit(1)

_, rnn, unit, epoch, batch = argv

rnn = rnn.upper()

if(rnn not in ['RNN', 'LSTM', 'GRU']):
	print('unknown learning algorithm',rnn)
	exit(1)

print(
	'rnn:', rnn,
	'unit:', unit,
	'epoch:', epoch,
	'batch:', batch)

