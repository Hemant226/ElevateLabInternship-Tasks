# Browser Extension Security Review 🛡️🔍

This repository documents a hands-on task I completed as part of a cybersecurity learning exercise: **Identifying and Remove Suspicious Browser Extensions**.

The main goal was to get familiar with how browser extensions work, what permissions they ask for, and how to spot potentially risky ones. It's all about boosting awareness of browser security.

## 🚀 The Task

The core task involved:
* Diving into the extension managers of different browsers.
* Carefully checking out each installed extension. 
* Paying close attention to the permissions each extension requests and why. 
* Deciding if an extension is truly needed and if its permissions make sense for what it does. 

For this particular review, the focus was on the investigation and learning process,and also there were no malicious extension, so no extensions were actually removed. I also spent some time researching the general ways malicious extensions can cause harm. 

## 🌐 Browsers Under the Microscope

I poked around in:
* Google Chrome 
* Mozilla Firefox

## 🛠️ Extensions Reviewed

Here's a quick look at what I found:

### Mozilla Firefox

* **FoxyProxy**
    * **What it does:** An advanced tool for managing proxy settings. I used it for Burp Suite.
    * **Permissions:** The necessary permissions for its core job (like controlling proxy settings and accessing browser tabs) were enabled. Good news: more sensitive optional permissions (like accessing data on all websites or clearing history) were found to be turned OFF. 
    * **Action:** Reviewed. Kept it as is. 

### Google Chrome

* **Google Docs Offline** 
    * **What it does:** The official Google extension that lets you work on Docs, Sheets, etc., even when you're not connected to the internet.
    * **Permissions:** Sensibly, it only asks for access to Google Docs and Drive websites. Totally lines up with what it's supposed to do.
    * **Action:** Reviewed. Kept it.

* **McAfee® WebAdvisor** 
    * **What it does:** A tool from McAfee to help protect you while you browse. It is an antivirus software's extension.
    * **Permissions:** This one needs broader access, like reading Browse history and accessing data on all websites, to do its job of keeping an eye out for dodgy sites and content. While "access all data on websites" sounds like a lot, it's pretty standard for comprehensive security tools from trusted names.
    * **Action:** Reviewed. Kept it. 

## 💡 What I Learned

This was a great exercise!
* Definitely more aware now of the kinds of risks browser extensions *can* pose if we're not careful. 
* Got some solid hands-on practice navigating the extension menus and figuring out what all those permission requests really mean. 

Thanks for checking out my project!
