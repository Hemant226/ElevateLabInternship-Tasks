# Task 8: Working and Understanding of VPN 

This repository documents a hands-on task to understand the functionality, benefits, and limitations of a Virtual Private Network (VPN). The project involved setting up a VPN, testing its impact on IP address and network speed, and summarizing the security features.

---

## 📝 Project Overview

The primary objective was to gain practical experience with VPNs to understand their role in protecting online privacy and ensuring secure communication. This was achieved by using a free, reputable VPN service to perform a series of tests and document the outcomes.

---

## 🛠️ Tools Used

* **VPN Service:** ProtonVPN (Free Tier) 
* **IP Verification:** `whatismyipaddress.com` 
* **Speed Testing:** `speedtest.net`

---

## ⚙️ Methodology

The following steps were performed to complete the analysis:

1.  A free account was created with ProtonVPN, and its client was downloaded and installed. 
2.  The original IP address and network speed were recorded to establish a baseline. 
3.  A connection was established to a free VPN server located in Japan. 
4.  The new IP address was verified to confirm that the VPN was successfully masking the original IP. 
5.  Websites were browsed to test the encrypted connection and check for any performance changes. 
6.  A comparative speed test was conducted with the VPN active. 
7.  The security protocols and encryption standards of ProtonVPN were researched. 
8.  All observations were compiled into a summary report. 

---

## 📊 Key Findings & Observations

### 1. IP Address Masking

The VPN successfully masked the original IP address, replacing it with one from the VPN server's location.

| Status | IP Address | Location |
| :--- | :--- | :--- |
| **Before VPN** | `152.xx.xx.xxx` | India  |
| **After VPN** | `212.xx.xx.xxx` | Japan  |

*This was verified using `whatismyipaddress.com` and the ProtonVPN client itself.*

### 2. Network Speed Comparison

A noticeable decrease in network speed was observed while connected to the VPN. This is an expected trade-off for the encryption and rerouting of traffic.

| Status | Download Speed | Upload Speed |
| :--- | :--- | :--- |
| **Without VPN** | 162.11 Mbps | 1.21 Mbps |
| **With VPN** | 10.20 Mbps | 0.91 Mbps |

**Observation:** Web pages took approximately 1-2 seconds longer to load with the VPN active, but the connection remained stable and usable for general Browse.

### 3. Security & Encryption

* **Encryption:** The report confirms that ProtonVPN uses **AES-256-bit encryption**, which is recognized as a military-grade security standard. 
* **Protocol:** The connection primarily utilized the **OpenVPN** protocol, known for its reliability and strong security. 

### 4. Observed Benefits

* **Anonymity:** The VPN effectively hid my real IP address, preventing websites and services from tracking my physical location. 
* **Traffic Encryption:** All internet data was encrypted, securing it from potential eavesdropping by ISPs or attackers on the network. 
* **Geo-Unlocking:** It was possible to access content specific to other geographic regions. 
* **Public Wi-Fi Security:** The added layer of encryption is particularly beneficial for protecting data on unsecured public Wi-Fi networks. 

### 5. Encountered Limitations

* **Reduced Speed:** The most significant drawback was the decrease in internet speed, especially when connected to distant servers. 
* **Limited Servers (Free Tier):** The free version of ProtonVPN offered a limited selection of server locations. 
* **Provider Trust:** It was noted that the security of a VPN is dependent on the provider's policies. It is crucial to use a VPN with a verified **no-logs policy**, as some less reputable services may log user activity. 

---

## ✅ Conclusion

This task demonstrated that a VPN is a powerful and essential tool for enhancing online privacy and security. While it introduces a trade-off in terms of internet speed, the benefits of IP masking, strong encryption, and bypassing geo-restrictions are significant. The choice of a trustworthy provider with a strict no-logs policy is paramount for ensuring true privacy.

