#!/usr/bin/env python3
from scapy.all import *
from datetime import datetime

def show_packet(packet):
    """Display basic packet information in a simple format"""
    if IP in packet:
        # Get basic packet info
        time = datetime.now().strftime('%H:%M:%S')
        src = packet[IP].src
        dst = packet[IP].dst
        size = len(packet)
        
        # Determine protocol
        if TCP in packet:
            proto = "TCP"
            extra = f"port {packet[TCP].sport} → {packet[TCP].dport}"
        elif UDP in packet:
            proto = "UDP" 
            extra = f"port {packet[UDP].sport} → {packet[UDP].dport}"
        elif ICMP in packet:
            proto = "ICMP"
            extra = "ping"
        else:
            proto = "Other"
            extra = ""
        
        # Print the packet info
        print(f"\n[{time}] {src} → {dst}")
        print(f"  {proto} {extra} | {size} bytes")
        
        # Show a bit of payload if available
        if Raw in packet:
            payload = packet[Raw].load[:20]
            print(f"  Data: {payload}")

def start_sniffing():
    """Start the packet capture"""
    print("Simple Packet Sniffer")
    print("Capturing IP traffic... (Press Ctrl+C to stop)\n")
    
    try:
        sniff(filter="ip", prn=show_packet, store=False)
    except KeyboardInterrupt:
        print("\nCapture stopped")

if __name__ == "__main__":
    start_sniffing()
