import socket
import select
import datetime


IP = "192.168.1.65"
English = ["x", "January", "Febuary", "March", "April","May", "June", 
           "July", "August", "October", "November", "December"]

Maori = ["x", "Kohitatea", "Hui-tanguru", "Poutu-te-rangi", "Paenga-whawha",
         "Haratua", "Pipiri", "Hongongoi", "Here-turi-koka", "Mahuru", 
         "Whiringa-a-nuku", "Whiringa-a-rangi", "Hakihea"]

German = ["x", "Januar", "Februar", "Marzm", "April", "Mai", "Juni", "Juli",
          "August", "September", "Oktober", "November", "Dezember"]

Lists = [English, Maori, German]

Language_Strings = ["English", "Maori", "German"]


def main(portE, portM, portG):
    try:
        english_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        english_socket.bind((IP, portE))
        maori_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        maori_socket.bind((IP, portM))
        german_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        german_socket.bind((IP, portG))
        sockets = [english_socket, maori_socket, german_socket]
    except:
        print("Failed to set up socket connection")
        return 0

    while True:
        requests, _, _ = select.select(sockets, [], [])
        count = 0
        for request in requests:
            try:
                data, client_address = request.recvfrom(1024)
                print("Request revieved from {}:{}".format(client_address[0], 
                                                           client_address[1]))
                lan_str = Language_Strings[sockets.index(request)]                            
            except:
                print("Error accepting request")
                return 0
            
        if check_data(data) == 1:
            date = datetime.datetime.now()
            request_type = join2b(data[4], data[5])
            text, lan_num = make_txt(request_type, date, lan_str)
            DT_res = dt_response(request_type, lan_num, date, text)
            try:
                sockets[lan_num-1].sendto(DT_res, client_address)
                print("Response sent to {}:{}".format(client_address[0], 
                                                      client_address[1]))
            except:
                print("Error sending response to {}:{}".format(client_address[0],
                                                               client_address[1]))
    se.close()
    sm.close()
    sg.close()


def check_data(data):
    """Checks a DT_request packet for errors, returns 1 if there arn't any"""
    if len(data) != 6:
        print('error: Message Length Incorrect')
        return -1
    
    magic_no = join2b(data[0], data[1])
    if magic_no != 0x497E:
        print('error: Magic Number Incorrect')
        return -2
    
    packet_type = join2b(data[2], data[3])
    if packet_type != 0x0001:
        print('error: Packet Type not recognised')
        return -3
    
    request_type = join2b(data[4], data[5])
    if  (request_type != 0x0001) and (request_type != 0x0002):
        print('error: Request Type not recognised')
        return -4
    
    else:
        return 1
    
    
    
def join2b(a, b):
    """Combines 2 bytes"""
    x = a << 8 | b
    return x


def make_txt(request_type, date, lan_str):
    """Returns a string containing the date or time in the requested language"""
    if request_type == 1:
        if lan_str == 'English':
            text = "Todays date is {:0>2} {:0>2}, {:0>4}".format(Lists[0][date.month], 
                                                                 date.day, date.year)
            lan_num = 0x01
        elif lan_str == 'Maori':
            text = "Ko te ra o tenei ra ko {:0>2} {:0>2}, {:0>4}".format(Lists[1][date.month], 
                                                                         date.day, date.year)
            lan_num = 0x02
        else:
            text = "Heute ist der {:0>2}. {:0>2} {:0>4}".format(date.day, Lists[2][date.month],
                                                                date.year)
            lan_num = 0x03
            
    else: #request_type == 2
        if lan_str == 'English':
            text = "The current time is {:0>2}:{:0>2}".format(date.hour, date.minute)
            lan_num = 0x01
        elif lan_str == 'Maori':
            text = "Ko te wa o tenei wa {:0>2}:{:0>2}".format(date.hour, date.minute)
            lan_num = 0x02
        else:
            text = "Die Uhrzeit ist {:0>2}:{:0>2}".format(date.hour, date.minute)
            lan_num = 0x03
            
    return text, lan_num
    
    
def dt_response(r_type, lan_num, date, text):
    """composes dt_response packet"""
    x = text.encode('utf-8')
    res = bytearray(13 + len(x)) 
    res[0] = 0x49 
    res[1] = 0x7E
    res[2] = 0x00
    res[3] = 0x02
    res[4] = 0x00
    res[5] = lan_num
    year = date.year.to_bytes(2, 'big')
    res[6] = year[0]
    res[7] = year[1]
    res[8] = date.month
    res[9] = date.day
    res[10] = date.hour
    res[11] = date.minute
    res[12] = len(x)
    count = 13
    for byte in x:
        res[count] = byte
        count += 1
    return res

main(5001,5002,5003)