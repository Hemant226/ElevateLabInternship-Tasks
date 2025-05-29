# Task 3: Performing a Basic Vulnerability Scan

This repository is where I've documented my hands-on experience with a basic vulnerability scan, a core task from my Cyber Security Internship. The goal was pretty straightforward: use readily available free tools to pinpoint common security weaknesses on a personal computer and then present the findings in a clear report. It was a fascinating dive into understanding how systems can be exposed!

---

## Task Overview

This project was assigned as **Task 3: Perform a Basic Vulnerability Scan on Your PC** as part of my Cyber Security Internship.
The core **Objective** was to utilize free tools to identify common vulnerabilities present on a personal computer.
For this, I had the option to use either **OpenVAS Community Edition** or **Nessus Essentials**. I ultimately chose **Nessus Essentials** for my scans, which generated reports like "My Host Discovery Scan" and "My Basic Network Scan" on May 29, 2025.

The primary **Deliverable** for this task was a comprehensive vulnerability scan report detailing all identified issues. This involved reviewing the report, researching potential fixes, and documenting the most critical vulnerabilities, along with providing supporting screenshots.

---

## What I Set Out to Do

My main objective for this task was to perform a basic vulnerability scan on my PC. This involved using free tools to identify common security vulnerabilities present on the system. It was all about getting practical experience with vulnerability assessment.

## The Tools I Used

For this particular task, I opted for **Tenable Nessus Essentials**. It's a widely recognized and powerful vulnerability scanner, and the "Essentials" version is perfect for learning and small-scale assessments.

## What I Produced

The key deliverable from this exercise was a comprehensive vulnerability scan report, highlighting all the identified issues on my system.

---

## My Step-by-Step Process

Here's a detailed breakdown of how I approached and completed this task:

### 1. Getting Nessus Essentials Up and Running

My first step was to get the scanning tool in place. I chose to install Nessus Essentials within a Kali Linux virtual machine (VM) that I was running on Oracle VirtualBox. This approach is great for cybersecurity tasks as it keeps my scanning activities isolated from my main operating system. The installation itself was fairly straightforward, following the guided prompts after downloading the Nessus Essentials package.

### 2. Defining My Scan Target

The task specified scanning "my PC." For safety and practical purposes, I configured Nessus to scan the local machine itself, which in my Kali Linux VM setup, corresponded to the IP address `192.168.159.6`. This allowed me to assess the VM's vulnerabilities directly.

### 3. First Pass: Host Discovery Scan

Before diving into a full vulnerability assessment, I initiated a **Host Discovery Scan** in Nessus. This initial scan is like taking a quick inventory of active devices on the network segment I was targeting. It successfully identified `192.168.159.6` as a live host. The discovery scan was quick and provided 2 "Info" level findings, indicating that the host was active.

### 4. Deeper Dive: Basic Network Scan

Once I confirmed the target host was active, I moved on to the core of the task: a **Basic Network Scan**. This is where Nessus really shines, actively probing the target for a wide range of known vulnerabilities. I set up a new scan task, selected the "Basic Network Scan" policy, and pointed it at my `192.168.159.6` target. This scan takes significantly longer than the discovery scan as it performs a much more thorough analysis of services, configurations, and potential weaknesses.

### 5. Dissecting the Report

After the "Basic Network Scan" completed, I eagerly reviewed the generated report. The summary provided a clear overview of the vulnerabilities found on `192.168.159.6`:

* **Critical:** 1
* **High:** 4
* **Medium:** 2
* **Low:** 0
* **Info:** 67

In total, Nessus identified 74 vulnerabilities on the system.

### 6. Researching How to Fix Things

The most crucial part after identifying vulnerabilities is understanding how to fix them. I focused on the "Critical" and "High" severity findings.

One of the most prominent critical vulnerabilities identified was related to **Node.js**: "Node.js x < 20.19.2 / 22.x < 22.15.1 / 23.x < 23.11.1 / 24.x < 24.0.2 Multiple Vulnerabilities". The report specifically recommended upgrading Node.js to a patched version, listing the exact versions needed for different branches (e.g., 18.x to 18.19.1 or later, 20.x to 20.11.1 or later). The report also provided clear instructions on how to upgrade using various methods like Node Version Manager (nvm), package managers on Ubuntu/Debian (`sudo apt update && sudo apt upgrade nodejs`), Homebrew on macOS, or downloading the latest installer for Windows.

Another vulnerability identified was "Python Tornado Library 6.5.0 DoS", which pointed to a Denial of Service weakness. The recommendation was to upgrade to Tornado version 6.5.0 or later.

### 7. Documenting the Critical Findings

For the internship deliverable, it's important to document the most significant vulnerabilities. Here’s a summary of the critical ones I found and researched:

* **Vulnerability Name:** Node.js Multiple Vulnerabilities (affecting versions less than 20.19.2, 22.15.1, 23.11.1, or 24.0.2)
    * **Severity:** Critical
    * **Description:** These are multiple security flaws found in older versions of Node.js that could potentially be exploited, leading to various security risks within applications running on Node.js.
    * **Recommended Solution:** The primary fix involves upgrading the Node.js installation to a secure, patched version. Specific target versions are 20.19.2, 22.15.1, 23.11.1, or 24.0.2 or later, depending on the current branch of Node.js in use.
* **Vulnerability Name:** Python Tornado Library 6.5.0 DoS
    * **Severity:** (Not explicitly labeled as Critical in the remediation screenshot, but typically High/Medium for DoS vulnerabilities).
    * **Description:** This vulnerability points to a potential Denial of Service weakness in the Tornado web framework when using version 6.5.0. An attacker could potentially disrupt service availability.
    * **Recommended Solution:** Upgrade the Python Tornado Library to version 6.5.0 or later.

### 8. Visual Proof: Screenshots of My Work

I made sure to capture screenshots at key stages to illustrate my process and the results. These are included below:

* **Nessus Essentials: Initial Scan Setup Interface**
    * Here the "Welcome to Nessus Essentials" prompt, where I entered my target IP for the discovery scan.
* **Host Discovery Scan Results: Confirmed Host**
    * After the discovery scan, Nessus successfully identified `192.168.159.6` as a live host, ready for a more detailed scan.
    * A view of the vulnerabilities section for the host discovery scan, showing 2 'Info' level findings.
    * The hosts tab for the discovery scan, confirming `192.168.159.6` was found.
* **Basic Network Scan: Overview of Findings**
    * Here a summary of the vulnerabilities found by the Basic Network Scan, broken down by severity (Critical, High, Medium, Low, Info) for `192.168.159.6`.
* **Basic Network Scan: Remediations Tab**
    * This view from the Nessus report highlights the identified vulnerabilities and suggests remediation actions, such as the Node.js and Python Tornado updates.
* **Detailed Fixes for Node.js Vulnerability**
    * A helpful guide detailing the affected Node.js versions and recommended upgrade steps using various package managers.
---

## Conclusion

This hands-on experience with Nessus Essentials for vulnerability scanning has been incredibly insightful. It clearly demonstrated the power of automated tools in identifying security weaknesses in a systematic manner. Even a basic scan on a single host can reveal a significant number of vulnerabilities, ranging from critical software outdatedness to potential denial-of-service risks.
The process underscored the importance of not just identifying vulnerabilities but also thoroughly researching their implications and understanding the necessary remediation steps. It highlighted that vulnerability scanning is an essential first step in a robust security posture, acting as a continuous health check for systems. While tools automate the detection, the human element remains crucial for interpreting reports, prioritizing fixes based on risk, and validating results to differentiate true vulnerabilities from false positives. This task has significantly enhanced my understanding of proactive cyber defense strategies.
