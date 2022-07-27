import socket 
import select


def main(request_type, ip_address, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    DT_request = create_packet(request_type)
    try:
        ip_address = socket.gethostbyname(ip_address)
    except:
        print("IP address unrecongised")
    try:
        client_socket.sendto(DT_request, (ip_address, port))
        print("Request sent to {}:{}".format(ip_address, port))
    except:
        print("Error sending request to {}:{}".format(ip_address, port))
    #recieve
    client_socket.setblocking(0)
    ready = select.select([client_socket], [], [], 1)    
    try:
        if ready[0]:       
            data, server_address = client_socket.recvfrom(1024)
        print("Response recieved from {}:{}".format(server_address[0], 
                                                    server_address[1]))
    except:
        print("Error recieving response from: {}:{}".format(ip_address, 
                                                            port))
        return 0
        
    if check_data(data) == 1:
        full_print(data)
    else:
        print("error code: {}".format(check_data(data)))
    client_socket.close()

    
def create_packet(request_type):
    """Forms a DT_request packet for sending"""
    DT_req = bytearray(6)
    b'0x497E,0x0001'
    DT_req[0] = 0x49
    DT_req[1] = 0x7E
    DT_req[2] = 0x00
    DT_req[3] = 0x01
    DT_req[4] = 0x00
    if request_type == "date":
        DT_req[5] = 0x01
    elif request_type == "time":
        DT_req[5] = 0x02
    else:
        print("error: Request Type not recognised")
        return -1
    return DT_req
    
    
def check_data(data):
    """checks a DT_response packet type for errors, returns 1 if there are none"""
    if len(data) <= 13:
        print("error: data length too small")
        return -1
    if join2b(data[0], data[1]) != 0x497E:
        print("error: magic number incorrect")
        return -2
    if join2b(data[2], data[3]) != 0x0002:
        print("error: packet type not recognised")
        return -3
    lan_num = join2b(data[4], data[5])
    if lan_num != 1 and lan_num != 2 and lan_num != 3:
        print("error: language type not recognised")
        return -4 
    if join2b(data[6], data[7]) >= 2100:
        print("error: year is too high")
        return -5
    if data[8] < 0:
        print("error: month can't be negative")
        return -6
    if data[9] < 1 or data[9] > 31:
        print("error: invalid day")
        return -7
    if data[10] < 0 or data[10] > 23:
        print("error: invalid hour")
        return -8
    if data[11] < 0 or data[11] > 59:
        print("error: invalid minute")
        return -9
    if len(data) != 13 + data[12]:
        print("error: unexpected data length")
        return -10
    else:
        return 1
    
        
def join2b(a, b):
    """Combines 2 bytes"""
    x = a << 8 | b
    return x
    
    
def to_text(pos, data):
    """converts a portion of a bytearray to a utf-8 string"""
    text = data[pos:].decode('utf-8')
    return text

    
def full_print(data):
    """prints out every feild in a DT_response packet"""
    print("Magic Number: {}".format(join2b(data[0], data[1])))
    print("Packet Type: {}".format(join2b(data[2], data[3])))
    print("Language Number: {}".format(join2b(data[4], data[5])))
    print("Year: {}".format(join2b(data[6], data[7])))
    print("Month: {}".format(data[8]))
    print("Day: {}".format(data[9]))
    print("Hour: {}".format(data[10]))
    print("Minute: {}".format(data[11]))
    print("Length: {}".format(data[12]))
    text = to_text(13, data)
    print(text)    

main("date", "192.168.1.75", 5005)