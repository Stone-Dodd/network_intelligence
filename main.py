from scapy.all import rdpcap, IP, TCP, UDP


def packet_summary():
    packets = rdpcap("captures/sample.pcap")
    src_ip = "Unknown"
    dst_ip = "Unknown"
    source_ports = "None"
    destination_ports = "None"
    total_packets = len(packets)
    ipv4_count = 0
    tcp_count = 0
    udp_count =0
    other_ipv4_count = 0

    for i, packet in packets:
        if IP in packet:
            ipv4_count += 1
            #Source IP
            src_ip = packet[IP].src
            #Destination IP
            dst_ip = packet[IP].dst
            #Primary transport protocols
            transport_protocol = packet[IP].payload.name
            #Extracting the source and destination ports
            source_ports = ""
            destination_ports = ""
            #TCP is present
            if TCP in packet:
                tcp_count += 1
                source_ports = packet[TCP].sport
                destination_ports = packet[TCP].dport
            #UDP is present
            elif UDP in packet:
                udp_count += 1
                source_ports = packet[UDP].sport
                destination_ports = packet[UDP].dport
            #Other protocols
            else:
                other_ipv4_count += 1
                other_packets = transport_protocol

        print("\n=== Network Traffic Intelligence ===\n")
        print(f"{src_ip} --> {dst_ip}")
        print(f"Source port: {source_ports} | Desintation ports: {destination_ports} ")
        
        print("\n=== IPv4 Protocol Summary ===")
        print(f"Total packets: {total_packets}")
        print(f"IPv4 packets: {ipv4_count}")
        print(f"TCP packets: {tcp_count}")
        print(f"UDP packets: {udp_count}")
        print(f"Other protocols: {other_ipv4_count}")

packet_summary()