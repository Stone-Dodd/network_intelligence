class PacketInfo:
    def __init__(self, src_ip, dst_ip, protocol,
        src_port=None, dst_port=None, packet_size=0):
            self.src_ip = src_ip
            self.dst_ip = dst_ip
            self.protocol = protocol
            self.src_port = src_port
            self.dst_port = dst_port
            self.packet_size = packet_size
    def __str__(self):
        if self.src_port is not None and self.dst_port is not None:
            return(f"Source IP: {self.src_ip} | Destination IP: {self.dst_ip} | Protocol: {self.protocol}\n"
                f"Source Port: {self.src_port} | Destination Port: {self.dst_port} | Packet Size: {self.packet_size}"
            )
        else:
            return(f"Source IP: {self.src_ip} | Destintation IP: {self.dst_ip}\n"
                    f"Protocol: {self.protocol} | Packet Size: {self.packet_size}")