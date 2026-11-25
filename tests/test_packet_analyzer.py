from src.packet_analyzer import PacketAnalyzer
from scapy.all import IP, IPv6, ARP

def test_analyze_capture():
    analyzer = PacketAnalyzer("captures/sample.pcap")

    analyzer.load_capture()
    analyzer.analyze_capture()
    
    print("\n=== First Five Analyzed Packets ===")

    for packet in analyzer.packet_records[:5]:
        print(packet)


if __name__ == "__main__":
    test_analyze_capture()