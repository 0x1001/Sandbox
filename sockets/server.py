from comm import server_factory
from comm import CommServerException
import threading
import time

ip = "127.0.0.1"
port = 59899

def request_handler(request):
    """
        Handles clients requestes

        Input:
        request     - Client request

        Returns:
        Nothing
    """
    from comm import CommException

    try:
        recv_frame = request.receive()
    except CommException as error:
        print error
        request.close()
        return

    print "Received"

    try:
        request.send("a")
    except CommException as error:
        print error
    finally:
        request.close()



if __name__ == "__main__":
    comm_server = server_factory(ip,port,request_handler)

    comm_server_thread = threading.Thread(target=comm_server.serve_forever)
    comm_server_thread.daemon = True
    comm_server_thread.start()

    while True:
         time.sleep(1)