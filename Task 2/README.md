# Taks 2 - Guide to Analyzing a Phishing Email Sample

This guide provides a step-by-step walkthrough on how to analyze a phishing email sample, based on the "Task 2: Analyze a Phishing Email Sample" from a Cyber Security Internship. We will use the provided screenshots as examples to illustrate the process.

## Task Overview (from an Internship Program)

**Task 2: Analyze a Phishing Email Sample**

* **Objective:** Identify phishing characteristics in a suspicious email sample.
* **Tools:** Email client or saved email file (text), free online header analyzer.
* **Deliverables:** A report listing phishing indicators found.

## Hints/Mini Guide (The 8 Steps to Analysis)

We will follow this mini-guide to analyze our sample email:

1.  Obtain a sample phishing email.
2.  Examine sender's email address for spoofing.
3.  Check email headers for discrepancies (using online header analyzer).
4.  Identify suspicious links or attachments.
5.  Look for urgent or threatening language in the email body.
6.  Note any mismatched URLs (hover to see real link).
7.  Verify presence of spelling or grammar errors.
8.  Summarize phishing traits found in the email.

---

## Step-by-Step Analysis of a Sample Email

Let's use the "HR Culture Survey 2019" email from "Survey Hound" (visible in `Screenshot (7).jpg` and `Screenshot (9).jpg`) as our primary example for analysis.

### 1. Obtain a Sample Phishing Email

For this exercise, our sample is the "HR Culture Survey 2019" email provided in an immersive learning environment.

* **Sender:** Survey Hound `<surveys@surveyhound.uk>`
* **Recipient:** Iml (with a checkmark)
* **Subject (Implied):** HR Culture Survey 2019
* **Body Text:** "Iml, you have been sent a survey from Bella Steele." "Hey there! HR is taking an employee culture survey, and would like your input! Please fill this survey out as soon as you can. It should only take you 5 minutes or so."
* **Link:** `https://surveyhound.uk/hr/19` (associated with a "Start survey" button).

![Sample Phishing Email Screenshot 1](Screenshot%20(7).jpg)
![Sample Phishing Email Screenshot 2](Screenshot%20(9).jpg)

### 2. Examine Sender's Email Address for Spoofing

* **Sender's Display Name:** "Survey Hound"
* **Sender's Email Address:** `surveys@surveyhound.uk`

**Analysis:**
* **Domain:** `surveyhound.uk`. We need to consider if this is a legitimate domain for HR surveys within an organization or a third-party service. If it's unsolicited or unexpected, its legitimacy is questionable. Phishers can register domains that sound plausible.
* **Generic Email Prefix:** `surveys@` is common, but also easy for attackers to set up.
* **".uk" TLD:** This is a country-code top-level domain for the United Kingdom. If you are not expecting emails from UK-based entities, this could be a flag, though many businesses operate internationally.

**Potential Red Flags (depending on context not visible in screenshot):**
* Is "Survey Hound" a known and trusted entity?
* Would your HR department use an external `.uk` domain for internal surveys?
* Does the company "Survey Hound" actually exist and offer such services? (In a real scenario, you might research this).

### 3. Check Email Headers for Discrepancies

We don't have the full email headers for the "Survey Hound" email itself. However, `Screenshot (10).png` shows an example of how to view an "Original Message" (headers) in Gmail, and `Screenshot (11).png` and `Screenshot (12).png` show these headers analyzed by MXToolbox.

**If we had the headers for the "Survey Hound" email, we would:**
1.  Copy the full header text.
2.  Paste it into an online header analyzer (like MXToolbox, Google Admin Toolbox Messageheader).
3.  Look for:
    * **`Return-Path` or `Reply-To` mismatches:** Does the reply address differ suspiciously from the `From` address?
    * **`Received` path:** Does the email originate from unexpected servers or geographical locations? Are there many convoluted hops?
    * **SPF (Sender Policy Framework) status:** A `fail` or `softfail` indicates the sending server might not be authorized to send emails for `surveyhound.uk`.
    * **DKIM (DomainKeys Identified Mail) status:** A `fail` would mean the email's signature doesn't validate, suggesting potential tampering or spoofing.
    * **DMARC (Domain-based Message Authentication, Reporting & Conformance) status:** A `fail` here often means either SPF or DKIM (or both) failed and the domain owner's policy indicates the email should be treated with suspicion (e.g., quarantined or rejected).

**Example of a Legitimate Header Analysis (from Screenshots 10, 11, 12 for a *different* email):**
The provided screenshots (`Screenshot (10).png`, `Screenshot (11).png`, `Screenshot (12).png`) show an analysis for an email from `Hemant Singh <dabbu2804@gmail.com>`.

![Gmail Original Message Headers](Screenshot%20(10).png)

This email shows:
* SPF: `PASS` with domain `gmail.com`
* DKIM: `PASS` with domain `gmail.com`
* DMARC: `PASS`

The MXToolbox analysis (`Screenshot (11).png`, `Screenshot (12).png`) confirms this:
* DMARC Compliant
* SPF Alignment & Authenticated
* DKIM Alignment & Authenticated
* Relay information shows legitimate Google mail servers.

![MXToolbox Header Analysis 1](Screenshot%20(11).png)
![MXToolbox Header Analysis 2](Screenshot%20(12).png)

**For the "Survey Hound" email, if these checks failed (e.g., SPF fail, DKIM fail), it would be a strong indicator of phishing.**

### 4. Identify Suspicious Links or Attachments

* **Link:** The email body contains a button "Start survey" which links to `https://surveyhound.uk/hr/19`.
* **Attachments:** No attachments are visible in this sample.

**Analysis of the Link:**
* **URL Structure:** `https://surveyhound.uk/hr/19`.
    * It uses `https`, which is good, but not a guarantee of safety. Phishers can also obtain SSL/TLS certificates.
    * The domain `surveyhound.uk` matches the sender's email domain. This *could* be legitimate. However, in a targeted phishing campaign, attackers might use a domain they control that mimics a real one or sounds plausible.
* **Context:** The link is for an "HR Culture Survey".
* **Action:** It prompts the user to "Start survey".

**Potential Red Flags:**
* If `surveyhound.uk` is not a domain your company uses or has approved for such surveys.
* If hovering over the link (Step 6) revealed a different underlying URL.

### 5. Look for Urgent or Threatening Language

The email says:
* "Please fill this survey out *as soon as you can*."
* "It should only take you 5 minutes or so."

**Analysis:**
* The urgency is relatively mild ("as soon as you can"). Phishing emails often use stronger language like "immediate action required," "account suspension imminent," or "within 24 hours."
* However, even mild pressure combined with other factors can be a social engineering tactic.
* The "only 5 minutes" tries to lower the perceived effort, making it more likely someone will click.

### 6. Note Any Mismatched URLs (Hover to See Real Link)

In this static image analysis, we see the displayed URL `https://surveyhound.uk/hr/19`. In a live email client:
* You would **hover your mouse cursor over the "Start survey" button or any hyperlinked text.**
* The actual destination URL would typically appear in the bottom status bar of the email client or browser.
* **Compare this actual URL with the displayed text/expected URL.** If they differ significantly (e.g., text says `surveyhound.uk` but link goes to `totally-different-evil-site.com`), it's a major red flag.

For our sample, we assume the displayed link is the actual link for now, as we cannot hover.

### 7. Verify Presence of Spelling or Grammar Errors

Let's examine the text:
* "**Iml**, you have been sent a survey from Bella Steele."
    * The name "Iml" followed by a checkmark (visible in the "To" field) is highly unusual. It looks like a placeholder (e.g., for `[Name]`) that wasn't correctly populated. This is a common sign of automated, bulk phishing emails.
* "**Hey there!** HR is taking an employee culture survey, and would like your input!"
    * "Hey there!" is quite informal for an official HR communication in many organizations. The appropriateness depends on company culture, but it can be a flag.
* The rest of the text appears grammatically acceptable, though the overall tone is informal.

**Potential Red Flags:**
* The placeholder "Iml" is the most significant issue here.
* Informal greeting.

### 8. Summarize Phishing Traits Found in the "Survey Hound" Email

Based on the analysis of the visible information:

1.  **Suspicious Sender Details (Potentially):**
    * The domain `surveyhound.uk` might be unknown or unexpected for an internal HR survey.
    * The sender name "Survey Hound" also needs verification if it's not a known service provider.
2.  **Generic/Impersonal Salutation & Recipient Handling:**
    * The recipient is listed as "Iml ✔️", and the salutation is "Iml," suggesting a failed mail merge or placeholder. This is a strong indicator of a non-targeted or carelessly crafted campaign.
3.  **Informal Tone:**
    * "Hey there!" might be too informal for an official communication, depending on the organizational context.
4.  **Call to Action with Mild Urgency:**
    * "Please fill this survey out as soon as you can." This encourages immediate action without being overly aggressive.
5.  **Nature of the Request (Context Dependent):**
    * An unsolicited request for survey participation from an external-sounding domain (`surveyhound.uk`) for an "HR" survey could be suspicious if not previously communicated through official internal channels.
6.  **Link to External Domain:**
    * The link `https://surveyhound.uk/hr/19` directs the user to an external site. While some companies use third-party survey tools, employees should be wary if this is not a standard or pre-notified practice.

**(If headers were available and showed SPF/DKIM/DMARC failures, those would be critical additions to this list.)**

---

## Deliverable: Report Listing Phishing Indicators

This README itself serves as an example of how you might structure a report. The summary above (Section 8) specifically lists the indicators found for the "Survey Hound" email. For your internship task, you would formalize this into a report.

## Key Concepts

The analysis above touches on several key cybersecurity concepts:

* **Phishing:** Attempting to acquire sensitive information (like usernames, passwords, credit card details) or install malware by masquerading as a trustworthy entity in an electronic communication.
* **Email Spoofing:** Creating email messages with a forged sender address. Header analysis (SPF, DKIM, DMARC) helps detect this.
* **Header Analysis:** Examining the metadata of an email to trace its origin and verify its authenticity.
* **Social Engineering:** Manipulating people into performing actions or divulging confidential information. Using urgency, informal language, or plausible scenarios are social engineering tactics.
* **Threat Detection:** The process of identifying potential cyber threats, including phishing attempts.

---

This detailed guide should help you approach your task of analyzing phishing emails effectively. Remember to always be cautious and scrutinize emails before clicking links or providing information.
