# SLL2-to-Ethernet Conversion

A tool for converting packet capture (PCAP) files from **Linux cooked-mode capture v1 (SLL) and v2 (SLL2) to Ethernet encapsulation**.

## Overview

PCAP files store captured network packets along with metadata describing how the packets are represented at the link layer. Depending on the capture interface and environment, packets may use Linux cooked-mode capture instead of Ethernet encapsulation.

This project aims to convert PCAP files using Linux cooked-mode capture v1 or v2 into the Ethernet format. This can help improve compatibility with tools and workflows that expect Ethernet-encapsulated packets.

## Supported Formats

| Format | Description |
|---|---|
| Linux cooked-mode capture v1 (SLL) | Original Linux cooked capture format |
| Linux cooked-mode capture v2 (SLL2) | Updated Linux cooked capture format |
| Ethernet | Target encapsulation format |

## Purpose

The main objectives of this project are to:

- Convert SLL v1 encapsulation to Ethernet.
- Convert SLL2 encapsulation to Ethernet.
- Make PCAP files easier to use with Ethernet-oriented packet analysis tools and workflows.
- Support network traffic analysis, packet inspection, and research involving captured network traffic.

## How It Works

At a high level, the conversion process involves:

1. Reading the input PCAP file and identifying its link-layer encapsulation.
2. Processing packets stored using Linux cooked-mode capture v1 or v2.
3. Converting the packet representation to Ethernet encapsulation.
4. Saving the converted packets into an output PCAP file.

**Note:** The exact conversion process depends on the implementation. SLL and SLL2 headers differ from Ethernet headers, so conversion may require reconstructing Ethernet headers using available packet information. The availability of source and destination MAC addresses can affect whether a valid Ethernet frame can be reconstructed.

## Use Cases

This project may be useful for:

- Preparing PCAP files for network traffic analysis.
- Improving compatibility between packet capture formats and analysis tools.
- Processing captured traffic in network security research.
- Working with PCAP datasets that use SLL or SLL2 encapsulation.

## Limitations

- Conversion results depend on the information available in the original packets.
- Ethernet header fields may need to be reconstructed when they are not directly available in the source capture.
- Converting the encapsulation format does not necessarily change the network-layer or transport-layer contents of a packet.
- The converted PCAP should be validated to ensure that the resulting link-layer format and packet contents are correct.
