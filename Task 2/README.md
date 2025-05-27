# Task 2 - Analysis of a Phishing Email Sample

 Analyze a Phishing Email Sample" for the Cyber Security Internship. My goal was to take a suspicious email and pick it apart to find any phishing red flags.

## The Task Overview

* **Objective:** Identify phishing characteristics in a suspicious email sample.
* **Tools:** Email client or saved email file (text), free online header analyzer.
* **Deliverables:** A report listing phishing indicators found (so, this document!).

## My Tools & Approach

To tackle this, I used the following:

1.  **Sample Phishing Email:** The task was done using a sample from what looks like an online training platform (`cybermillion.immersivelabs.online/...` from the browser tab. The specific email is the "HR Culture Survey 2019" from "Survey Hound."
2.  **Viewing Email Headers:** If this were a real email in my inbox (like Gmail), I'd use the "Show original" feature to get the full headers.
3.  **Online Header Analyzer:** For checking those headers, I'd use a free online tool like MXToolbox. 

My general approach followed the "Hints/Mini Guide" provided with the task:

1.  Get the sample email.
2.  Look closely at the sender's address.
3.  Check the email headers.
4.  Spot any suspicious links or attachments.
5.  Check for urgent or threatening language.
6.  Make sure displayed links match the actual URLs.
7.  Look for spelling/grammar mistakes and weird formatting.
8.  List out all the phishing signs found.

---

## Step-by-Step Breakdown: Analyzing the "HR Culture Survey 2019" Email

Here's how I applied those steps to the "Survey Hound" email:

**Our Sample Email:**
* **Platform:** Immersive Phishing Emails
* **From:** Survey Hound `<surveys@surveyhound.uk>`
* **To:** Iml ✔️
* **Visible Subject Area:** HR Culture Survey 2019
* **Body Snippet 1:** "Iml, you have been sent a survey from Bella Steele."
* **Body Snippet 2:** "Hey there! HR is taking an employee culture survey, and would like your input! Please fill this survey out as soon as you can. It should only take you 5 minutes or so."
* **Link:** A button "Start survey" pointing to `https://surveyhound.uk/hr/19`

---

### 1. Obtain a Sample Phishing Email

Done! We're using the "Survey Hound" email from the training platform.

### 2. Examine Sender's Email Address for Spoofing

* **Sender:** `Survey Hound <surveys@surveyhound.uk>`
* **What I looked for:**
    * **Domain (`surveyhound.uk`):** Is this a known, trusted company? Or does it just sound plausible? Phishers often register domains that are slightly off from real ones (e.g., `paypa1.com` instead of `paypal.com`) or use generic names. `surveyhound.uk` itself doesn't have obvious misspellings or weird repeated characters (`goooogle.com`), but its legitimacy is key. The `.uk` TLD means it's UK-based; is that expected?
    * **Display Name vs. Email:** Here, "Survey Hound" matches the `surveyhound.uk` domain, which is good. But I'd always check if the display name (e.g., "Microsoft Support") actually matched a very different, unofficial email address (e.g., `user123@randomail.com`).

### 3. Check Email Headers for Discrepancies

* **For the "Survey Hound" email:** I don't have its actual headers from the screenshots.
* **If I did have them:**
    1.  I'd first grab the full header text. In Gmail, for example, I'd click the three dots and "Show original" which shows headers a different email
       
    2.  Then, I'd copy all that header text and paste it into an online analyzer like MXToolbox show MXToolbox analyzing those headers.
    4.  **What I'd look for in the "Survey Hound" headers:**
        * **SPF, DKIM, DMARC results:** Do these `PASS` or `FAIL`? A `FAIL` would strongly suggest spoofing. (If the example shows all `PASS`, means which is good for *that* email).
        * **Return-Path:** Does it match the `From` address, or does it go somewhere else?
        * **Received Path:** Does the email come from servers/locations that make sense for "Survey Hound"? Or is it a weird, convoluted path?

### 4. Identify Suspicious Links or Attachments

* **Link:** The "Start survey" button links to `https://surveyhound.uk/hr/19`.
* **Attachments:** None visible in this sample.
* **What I looked for:**
    * **Hovering (Crucial!):** If this were a live email, I'd hover over the "Start survey" button. The *actual* URL it links to would pop up (usually bottom-left of the window). I'd check if this matches `https://surveyhound.uk/hr/19`. Sometimes the text looks fine, but the hidden link is totally different and malicious.
    * **URL Itself (`https://surveyhound.uk/hr/19`):**
        * It uses `https` (good, but not a guarantee of safety).
        * The domain `surveyhound.uk` again needs to be assessed for legitimacy.
        * No obvious tricks here like `surveyhound.uk.malicious.com` or `surveyh0und.uk` or weird repeated characters in the URL.
    * **Attachments (if there were any):** I'd be super wary of unexpected attachments, especially `.exe`, `.zip` (containing executables), or Office docs asking to "Enable Macros." File names like "UrgentInvoice.exe" or "Payment_Details.docm" are big red flags.

### 5. Look for Urgent or Threatening Language in the Email Body

* **Text:** "Please fill this survey out *as soon as you can*. It should only take you 5 minutes or so."
* **My take:** This is pretty mild. Phishers often use much stronger stuff like "Your account will be closed in 24 hours!" or "Suspicious activity detected - verify NOW!" to create panic. The "as soon as you can" and "only 5 minutes" here is more about gentle nudging.

### 6. Note Any Mismatched URLs

As mentioned in step 4, this is about the hover check. Since I'm looking at static images, I can't do this for the "Survey Hound" email. But it's a critical step – always verify that the link goes where it says it's going!

### 7. Verify Presence of Spelling, Grammar Errors, and Other Stylistic Anomalies

* **Recipient:** The email is addressed to user@immersive.local. The message body, however, begins with "Iml, you have been sent a survey from Bella Steele."

* **Mismatch in Recipient Name:** This is a red flag. The email was sent to a specific address (user@immersive.local), but the salutation refers to “Iml” — which is likely a placeholder or formatting error. This mismatch suggests bulk or automated mailing, where variables weren't replaced properly, a common trait in phishing emails.
* **Greeting:** "Hey there!" – This is pretty informal for an HR-related survey from an external company in most professional settings. Could be a stylistic choice, but combined with other flags, it adds to suspicion.
  
* **From "Bella Steele":** Who is Bella Steele? Is she from my HR? From Survey Hound? The email doesn't clarify.
* **Other things I'd look for:**
    * Obvious typos (e.g., "acount" instead of "account").
    * Bad grammar.
    * Weird formatting (mixed fonts, odd spacing).
    * Excessive ALL CAPS or exclamation marks!!! (e.g., "YOU HAVE WONNNN!!!"). This sample doesn't have those.

### 8. Summarize Phishing Traits Found in the "Survey Hound" Email

* **Major Red Flag: Failed Personalization:** The email was sent to user@immersive.local, but the message body refers to the recipient as "Iml" — likely a placeholder or template variable that was not properly replaced. This indicates a mail merge error, which is common in automated phishing campaigns. It shows a lack of personalization and care, which is suspicious and unprofessional, especially for a message claiming to be from a legitimate HR-related service.
* **Questionable Sender Legitimacy:** The domain `surveyhound.uk` and sender "Survey Hound" would need to be verified as a legitimate service used by my organization's HR. If it's unexpected, it's a flag.
* **Informal Tone:** "Hey there!" might be too casual, depending on company culture and if the sender is truly external.
* **Unclear Authority/Source:** The mention of "Bella Steele" without context adds a bit of confusion.
* **Generic Nature:** While it mentions "HR Culture Survey," the approach feels a bit generic, especially with the "Iml" issue.

(If I had its headers and they showed SPF/DKIM fails, that would be another huge red flag!)

---

## What I Learned About Header Analysis (From the Screenshots 10-12 Example)

Looking at the email headers in the screenshots was useful to see what a *good* analysis looks like:

* **SPF (Sender Policy Framework):** The screenshot shows `PASS` for `gmail.com`. This means Google's servers confirmed the email came from a server authorized to send emails for `gmail.com`. If it said `FAIL`, it would mean it likely wasn't authorized (spoofed).
* **DKIM (DomainKeys Identified Mail):** Also `PASS` for `gmail.com`. This means the email had a digital signature that matched the `gmail.com` domain, proving it wasn't tampered with in transit and originated from where it claims. A `FAIL` would be suspicious.
* **DMARC (Domain-based Message Authentication, Reporting & Conformance):** `PASS`. This builds on SPF and DKIM. A `PASS` means the email aligned with the domain owner's policies based on SPF and DKIM passing. A `FAIL` would mean it didn't meet the criteria and might be rejected or quarantined by my mail server.

So, if the "Survey Hound" email had `FAIL` on these, I'd be almost certain it was a phish.

## Key Takeaways / Phishing Concepts I Focused On

From the task sheet, these were the key concepts, and I definitely saw them in action:

* **Phishing:** This whole exercise was about spotting it!
* **Email Spoofing:** Checking the sender address and (hypothetically) the headers is all about detecting this.
* **Header Analysis:** Realized how important SPF, DKIM, and DMARC are.
* **Social Engineering:** The "Iml" error, the informal tone, the (mild) urgency – these are all little psychological nudges.
* **Threat Detection:** This whole process is a form of threat detection.
## Conclusion
The email is a phishing attempt, evident from the failed personalization ("Iml"), unclear sender identity, suspicious domain, and informal tone. These signs point to an automated, deceptive campaign designed to trick users.
