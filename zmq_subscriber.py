import zmq
import messages
import sys


def main():
    context = zmq.Context()
    socket = context.socket(zmq.SUB);
    print("Collecting updates form weather server:")
    socket.connect("tcp://localhost:5556")

    # Subscribe to zipcode, default is 10001 (NYC)
    zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"
    socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)

    # Process 100 updates
    total_temp = 0
    for update_number in range(100):
        update = socket.recv_string()
        (zipcode, temperature, humidity) = update.split();
        total_temp += float(temperature)
        print("Got an update for", zipcode, ": The temperature is", temperature, "with", humidity, "percent humidity.")
    print("The average temperature for zip", zip_filter, "was", total_temp/update_number)

    socket.close()
    context.destroy()

if __name__ == "__main__":
    main()