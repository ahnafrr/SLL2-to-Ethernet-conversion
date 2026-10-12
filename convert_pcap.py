"""
How to use:
python convert_pcap.py <input_sll2.pcap> <output_ethernet.pcap>
"""
import struct
import sys
import dpkt
 
 
SLL2_LINKTYPE = 276 # If file encapsulation is Linux cooked-mode capture v2, use this (276). But if file encapsulation is Linux cooked-mode capture v1, use 113.
SLL2_HEADER_LEN = 20 # If file encapsulation is Linux cooked-mode capture v2, use this (20). But if file encapsulation is Linux cooked-mode capture v1, use 16.
FAKE_MAC = b"\x00\x00\x00\x00\x00\x00"

def main(src, dst):
    converted = skipped = 0
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        reader = dpkt.pcap.Reader(fin)
        if reader.datalink() != SLL2_LINKTYPE:
            sys.exit(f"Input not SLL2 (linktype {reader.datalink()}), need to convert.")
        writer = dpkt.pcap.Writer(fout, linktype=dpkt.pcap.DLT_EN10MB)
        for ts, buf in reader:
            if len(buf) < SLL2_HEADER_LEN:
                skipped += 1
                continue
            # First 2 bytes of SLL2 header = protocol type (EtherType, big-endian)
            ethertype = struct.unpack("!H", buf[0:2])[0]
            payload = buf[SLL2_HEADER_LEN:]
            # Wrap again: destination MAC + source MAC (dummy) + EtherType + payload
            frame = FAKE_MAC + FAKE_MAC + struct.pack("!H", ethertype) + payload
            writer.writepkt(frame, ts)
            converted += 1
    print(f"OK: {converted} packets converted, {skipped} packets skipped (too short)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_pcap.py <input_sll2.pcap> <output_ethernet.pcap>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])