
# Taks 4: Firewall Configuration Practice (UFW on Linux)

## Project Overview

This project walks through the setup, configuration, and testing of UFW (Uncomplicated Firewall) on a Kali Linux system. The primary goal was to understand how to manage inbound network traffic by enabling the firewall, setting up rules to allow or block specific ports, verifying these rules, and then cleaning up test configurations.

This exercise was undertaken as part of a cybersecurity internship task, focusing on developing practical firewall management skills.

## What I Did: Setting Up UFW

Here’s a detailed account of the actions I performed in the terminal:

1.  **Opened Terminal & Initial UFW Status Check**:
    * I started by launching the terminal in my Kali Linux environment.
    * Command: `sudo ufw status verbose`
    * **Observation**: The output `Status: inactive` indicated that UFW was installed but not currently active.

2.  **Enabling UFW**:
    * Command: `sudo ufw enable`
    * **Observation**: UFW responded with `Firewall is active and enabled on system startup`. This activated the firewall.

3.  **Verifying Active Status & Default Policies**:
    * Command: `sudo ufw status verbose`
    * **Observation**: The status was now `active`. The default policies were shown as: `deny (incoming), allow (outgoing), disabled (routed)`.

4.  **Adding a Rule to Block Inbound Telnet (Port 23)**:
    * To test blocking capabilities, I added a rule to deny inbound TCP traffic on port 23 (Telnet).
    * Command: `sudo ufw deny 23/tcp`
    * **Observation**: The system confirmed `Rule added` (and `Rule added (v6)`).

5.  **Confirming the New Block Rule**:
    * Command: `sudo ufw status verbose`
    * **Observation**: The rule list now included `23/tcp DENY IN Anywhere`.

6.  **Testing the Block Rule via Telnet**:
    * I attempted a Telnet connection to my machine's IP (`192.168.159.6`) on port 23.
    * Command: `telnet 192.168.159.6 23`
    * **Observation**: The connection attempt resulted in `telnet: Unable to connect to remote host: Connection refused`, confirming the firewall rule was effectively blocking the connection.

7.  **Adding a Rule to Allow Inbound SSH (Port 22)**:
    * Ensuring essential remote access, I added a rule to allow inbound TCP traffic on port 22 (SSH).
    * Command: `sudo ufw allow 22/tcp`
    * **Observation**: The system confirmed `Rule added` (and `Rule added (v6)`).

8.  **Verifying Both Block and Allow Rules**:
    * Command: `sudo ufw status verbose`
    * **Observation**: The output now listed both the `DENY IN` rule for port 23 and the `ALLOW IN` rule for port 22.

9.  **Listing Rules Numerically**:
    * To facilitate rule deletion by number, I listed the current rules with numerical prefixes.
    * Command: `sudo ufw status numbered`
    * **Observation**: Rules were displayed with numbers, e.g., `[ 1] 23/tcp DENY IN Anywhere`.

10. **Removing the Test Block Rule (Telnet)**:
    * I removed the previously added deny rule for port 23/tcp.
    * Command: `sudo ufw delete deny 23/tcp`
    * **Observation**: The system confirmed `Rule deleted` (and `Rule deleted (v6)`).

11. **Verifying Final Firewall Configuration**:
    * Command: `sudo ufw status verbose`
    * **Observation**: The final rule list showed that the deny rule for port 23 was removed, while the allow rule for port 22 remained active.

## Deliverable Evidence

The series of screenshots taken throughout this process document the application and verification of firewall rules. Key screenshots include:
* Shows both the Telnet (port 23) deny rule and the SSH (port 22) allow rule active, along with the successful test of the Telnet block.
* Shows the final state after the Telnet block rule was removed.

## Key Learnings & Outcomes

Through this task, I gained hands-on experience with:
* Verifying the status of UFW and enabling it.
* Adding rules to `allow` and `deny` traffic based on port and protocol.
* The significance of default firewall policies (deny incoming, allow outgoing).
* Testing firewall rules to confirm their correct operation.
* Managing rules by listing them numerically and deleting specific rules.
* The importance of ensuring critical services (like SSH) are explicitly allowed when configuring a firewall.

This exercise was a practical demonstration of fundamental network security principles using UFW on Linux.
