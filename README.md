
# Task 1 - Network Port Scanning

## 🔍 Task: Scan Your Local Network for Open Ports

This repository contains the results and analysis of **Task 1**. The goal was to use **Nmap** to perform a TCP SYN scan on the local network and optionally analyze packets with **Wireshark**.

## ✨ Project Status

This task has been successfully completed and documented, providing insights into local network security.

## 🎯 Objective

Our primary objectives for this task were to:

* Perform a TCP SYN scan using Nmap.
* Identify open ports on various devices within the local network.
* Understand the exposure and security risks associated with running identified services.
* Capture and analyze network traffic using Wireshark to observe the scan's behavior.

## 🛠️ Tools Used

The following tools were essential for completing this task:

* Nmap: A powerful open-source utility for network discovery and security auditing.
* Wireshark: A widely used network protocol analyzer for detailed packet inspection.
* Kali Linux (inside VirtualBox): Our operating environment, providing a robust suite of penetration testing tools.

## 🧪 Steps Performed

Here's a breakdown of the steps taken to complete the network port scanning task:

1.  Identified Local IP Range:
    We first used the `ifconfig` command to determine the network interface and the local IP address range of our Kali Linux machine. This was crucial for accurately targeting the Nmap scan.

2.  Performed TCP SYN Scan using Nmap:
    A TCP SYN scan (-sS) was chosen for its efficiency and stealth. This "half-open" scan does not complete the full TCP handshake, making it less intrusive and often less detectable than a full connect scan. We targeted the entire local network range.

    ```bash
    nmap -sS 192.168.126.6
    # Example: nmap -sS 192.168.126.6/24
    ```

3.  Analyzed Nmap Output:
    The output from Nmap provided a comprehensive list of active hosts, their open ports, the services running on those ports, and often, the version of the service.

4. Packet Analysis with Wireshark:
    To gain a deeper understanding of how the SYN scan interacts with network protocols, Wireshark was used to capture and analyze packets during the Nmap scan. This allowed us to visually confirm the "half-open" nature of the SYN scan.

## 📈 Results

During the scan of the local network, only one open port were identified on various devices. While specific IP addresses and devices vary, here's an example of typical findings:

PORT   STATE SERVICE VERSION
53/tcp open  domain  dnsmasq 2.51

## 🧠 Analysis & Learnings

This task significantly enhanced our understanding of network security fundamentals:

* Understanding Exposure: Identifying open ports directly highlights potential entry points for attackers. This understanding is critical for assessing a network's attack surface.
* Service Identification: Nmap's ability to identify services running on open ports is invaluable for understanding what applications are accessible and their potential vulnerabilities.
* Security Risks: We learned that running unnecessary services or services with default/weak configurations poses significant security risks. Each open port represents a potential vector for exploitation if not properly secured.
* Nmap Proficiency: This hands-on exercise greatly improved practical skills in using Nmap for effective network reconnaissance and initial vulnerability assessment.
* Wireshark Insight: By observing the packets in Wireshark, we get to know that how observe network and how Nmap's various scan types interact with target systems.


## 🎯 Conclusion

This task successfully demonstrated the effectiveness of Nmap as a vital tool for network port scanning and provided a foundational understanding of network exposure and its security implications. It reinforced the importance of regular network auditing to identify and mitigate potential vulnerabilities.

