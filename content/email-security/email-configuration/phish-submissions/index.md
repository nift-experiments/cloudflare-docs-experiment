---
cp9:
  canonical: https://developers.cloudflare.com/email-security/email-configuration/phish-submissions/
  description: Submit missed phishing samples to Email security to improve detection models and threat coverage.
  full_title: Phish submissions · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Phish submissions · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Submit missed phishing samples to Email security to improve detection models and threat coverage."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/email-configuration/phish-submissions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/email-configuration/phish-submissions/index.md"><meta property="og:title" content="Phish submissions · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Submit missed phishing samples to Email security to improve detection models and threat coverage."><meta property="og:url" content="https://developers.cloudflare.com/email-security/email-configuration/phish-submissions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/email-configuration/phish-submissions/
  schema: 1
---
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="access-to-area-1">Access to Area 1</h3>
@markup("md", "content/.markup/bodies/8555.md")
</aside>
<p>As part of your continuous email security posture, administrators and security analysts need to submit missed <span class="nb-glossary-tooltip" title="phishing">phish</span> samples to <a href="https://horizon.area1security.com/support/service-addresses/">Email security (formerly Area 1) Service Addresses</a> so Cloudflare can process them and take necessary action.</p>
<p>Sometimes phish is missed as Email security uses several techniques to make a detection. These include preemptively crawling the web to identify campaigns, machine learning, custom signatures, among others. In order for Email security to identify why phish was missed, we need to run the original samples through our module and identify why some of our modules did not score the sample high enough to elevate it to malicious.</p>
<p>Submitting missed phish samples to Cloudflare is of paramount importance and necessary for continuous protection. Submitting missed phish samples helps Cloudflare improve our machine learning (ML) models, and alerts us of new attack vectors before they become prevalent.</p>
<h2 id="how-to-submit-phish">How to submit phish</h2>
<p>There are two different ways to submit a phish sample:</p>
<ul>
<li>
<p><strong>User submission</strong>: Submitted directly by the end users, and used with phish submission buttons. <br />
To learn more about user-submitted phish, refer to the following documentation: <ul class="directory-listing"><li><a href="/email-security/email-configuration/phish-submissions/knowbe4/">KnowBe4</a></li><li><a href="/email-security/email-configuration/phish-submissions/microsoft-report-message/">Microsoft Report Message (not compatible)</a></li><li><a href="/email-security/email-configuration/phish-submissions/phishnet-gworkspace/">PhishNet for Google Workspace</a></li><li><a href="/email-security/email-configuration/phish-submissions/phishnet-o365/">PhishNet for Office 365</a></li></ul></p>
</li>
<li>
<p><strong>Team submission</strong>: To be used when IT administrators or security teams submit to Email security. Submit original phish samples as an attachment in EML format to the appropriate <a href="https://horizon.area1security.com/support/service-addresses/">Team Submissions address</a>. For example, if you think an email should be marked as spoof, send it to the <code>SPOOF</code> address listed in Team Submissions. <br />
Phish samples submitted to this address will be considered as submissions from the customer's email security team. This increases the chances of similar samples being detected as malicious in the future.</p>
</li>
</ul>
<p>After submitting a phish sample to the team address, you will receive an update from <code>status@submission.area1reports.com</code> regarding the investigation and the verdict. The feedback is directly provided to customers by our threat research team, bypassing the support channel, to expedite the process.</p>
<h2 id="what-happens-after-a-phish-submission">What happens after a phish submission</h2>
<p>After you or your users submit a phish sample, Email security adds that sample directly into our machine learning (ML) queue for learning. Some samples will be directly converted to <code>MALICIOUS</code> upon going through machine learning and the rest will be further processed by our ML module.</p>
<h3 id="phish-submission-feedback">Phish submission feedback</h3>
<p>Use the following keywords to search for submitted phish samples on the Email security dashboard:</p>
<ul>
<li><code>phish_submission</code></li>
<li><code>user_malicious_submission</code></li>
<li><code>team_malicious_submission</code></li>
</ul>
<p>On the <strong>Reasons</strong> column you will see the feedback regarding the messages found. If the ML module learns and detects it as phish, the <strong>Reasons</strong> column shows the details regarding it. If not, the information on this column shows up as <code>phish submission</code>.</p>
<p>If there is a phishing email that is repeatedly sent to users despite being submitted to Email security for processing, <a href="/support/contacting-cloudflare-support/">contact support</a> with the details of the problematic phish submission sample (alert ID or message ID of the sample).</p>
<h3 id="phish-submission-response-beta">Phish Submission Response (beta)</h3>
<p>Phish Submission Response (PSR) is an additional layer of protection. When you enable PSR, Email security will automatically retract messages reported by users which are also deemed malicious by Email security after analysis. This feature uses machine learning margin scores by adding the user as an additional neuron into Email security's neural network.</p>
<p>To enable PSR:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Go to <strong>Settings</strong> (the gear icon).</li>
<li>In <strong>Email Configuration</strong>, go to <strong>Retract Settings</strong> &gt; <strong>Auto-Retract</strong>.</li>
<li>Enable <strong>Phish Submission Response (Beta)</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8554.md")
</aside>
<h2 id="false-positives">False positives</h2>
<p>If you find emails in your Email security account that are actually false positives, you can report them from the Email security dashboard:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Select the <strong>Search</strong> bar.</li>
<li>Search for one or more messages that you want to report as a false positive, and select <strong>Report as false positive</strong>.</li>
<li>In the next screen, choose a disposition from the list to clarify the nature of the false positive. The options are <em>Bulk</em>, <em>Malicious</em>, <em>None</em>, <em>Spam</em>, <em>Spoof</em> and <em>Suspicious</em>.</li>
<li>Select <strong>Report False Positive</strong>.</li>
</ol>
<h2 id="false-negatives">False negatives</h2>
<p><a href="/email-security/account-setup/permissions/">Email security administrators</a> can also submit false negatives directly from the dashboard:</p>
<ol>
<li>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</li>
<li>Select the <strong>Search</strong> bar.</li>
<li>Search for one or more messages that you want to report as a false negative, and select <strong>Report as False Negative</strong>.
<img src="/assets/upstream/images/email-security/phish-submissions/false-negative.png" alt="The link to submit false negatives, in the search results" /></li>
<li>In the next screen, choose a disposition from the list to clarify the nature of the false negative. The options are <em>Bulk</em>, <em>Malicious</em>, <em>Spam</em>, <em>Suspicious</em> and <em>Spoof</em>.</li>
<li>Select <strong>Report False Negative</strong>.</li>
</ol>
