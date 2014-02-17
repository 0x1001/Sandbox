import string
import random
import time
import uuid

base1k = "".join([random.choice(string.ascii_letters) for i in range(1024)])
base1m = "".join([base1k for i in range(1024)])

size_in_MB = 200
data = "".join([base1m for i in range(size_in_MB)])

session_id = uuid.uuid4().get_hex()

################################################################################

# Frame
#
# idx session_id control payload
# 10  32         8       8192-10-32-8
#
payload_size = 8192 - 10 - 32 - 8

partitioned_data = []

start_time = time.time()
# - 1
for idx in range(len(data)/payload_size + 1):
    partitioned_data.append("".join([str(idx).zfill(10),session_id,"AAAAAAAA",data[payload_size*idx:payload_size*(idx+1)]]))

# - 2
#[data[payload_size*idx:payload_size*(idx+1)] for idx in range(len(data)/payload_size + 1)]

# - 3
#partitioned_data = map(lambda idx: data[payload_size*idx:payload_size*(idx+1)],range(len(data)/payload_size + 1))

stop_time = time.time()

print "Duration: " + str(stop_time - start_time)

print len(partitioned_data)
print len(partitioned_data[0])

print "Overhead: " + str((((len(partitioned_data) - 1.0)*8192.0 + len(partitioned_data[-1]))/len(data))*100.0 - 100.0)

start_time = time.time()
data_received = "".join([data_portion[50:] for data_portion in partitioned_data])
stop_time = time.time()
print "Duration: " + str(stop_time - start_time)

print len(data_received)
print len(data)