from scapy.all import rdpcap, IP, IPv6, TCP, UDP
from src.packet_info import PacketInfo


class PacketAnalyzer:
    def __init__(self, capture_file):
        self.capture_file = capture_file
        self.raw_packets = []
        self.packet_records = []

    def load_capture(self):
        self.raw_packets = rdpcap(self.capture_file)
        print(f"Total Packets: {len(self.raw_packets)}")

    def analyze_packet(self, packet):
        src_port = None
        dst_port = None

        if IP in packet:
            ip_layer = packet[IP]
        elif IPv6 in packet:
            ip_layer = packet[IPv6]
        else:
            return None
        
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        
        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        else:
            protocol = ip_layer.payload.name
            
        packet_size = len(packet)
        return PacketInfo(
            src_ip,
            dst_ip,
            protocol,
            src_port,
            dst_port,
            packet_size
        )
    def analyze_capture(self):
        for packet in self.raw_packets:
            result = self.analyze_packet(packet)
            if result is not None:
                self.packet_records.append(result)
        print(f"Successfully analyzed {len(self.packet_records)} IP packets.")