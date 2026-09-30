<p>Brand Protection allows you to proactively identify and mitigate domain impersonation and phishing attacks. By monitoring newly registered domains and visual assets across the Internet, Cloudflare helps protect your brand's reputation and prevents your customers or employees from submitting sensitive information to fraudulent sites.</p>
<p>Common threats include:</p>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Typosquatting">Typosquatting</a>: For example, typing <code>cloudfalre.com</code> instead of <code>cloudflare.com</code>.</li>
<li>Concatenation of services (<code>cloudflare-service.com</code>) often registered by attackers to trick unsuspecting victims into submitting private information such as passwords.</li>
<li><a href="https://en.wikipedia.org/wiki/IDN_homograph_attack">Homoglyph attacks</a> that use lookalike characters to trick unsuspecting victims.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="user-permission">User permission</h3>
@markup("md", "content/.markup/bodies/378.md")
</aside>
<h2 id="types-of-queries">Types of queries</h2>
<p>Cloudflare Brand Protection offers two distinct methods for monitoring impersonation: domain search and logo search.</p>
<h3 id="domain-search">Domain search</h3>
<p>Search for domains based on text patterns, misspellings, or service combinations.</p>
<p>To start searching for new domains that might be trying to impersonate your brand:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Brand Protection</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>In <strong>String query</strong>, provide a name for your query. You can add multiple brand phrases on the same query, and the results will generate matches for all of those. Once you entered the string queries, select <strong>Search matches</strong>.</p>
</li>
<li>
<p>In the <strong>Character distance</strong>, select from <code>0-3</code>. This defines how many characters a result can differ from your string (for example, a distance of 1 would catch <code>clpudflare.com</code>). The number of characters the results can differ from your domain.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/377.md")
</aside>
<ol start="4">
<li>
<p>You can select <strong>Save query</strong> to monitor it in the future and perform other actions, such as delete, clone and set up alerts, according to your Paid plan limits.</p>
</li>
<li>
<p>To export all matches from a saved query, select your <strong>Query name</strong> &gt; select the three dots &gt; <strong>Export matches</strong>.</p>
</li>
</ol>
<p>In the section <strong>Monitor Strings</strong>, you can check all the string queries that you selected to monitor. You can delete, clone, or create notifications for a string query. Refer to <a href="#brand-protection-alerts">Brand Protection Alerts</a> to set up notifications. You can also dismiss any domain matched in the query if you have investigated and deemed it benign or a false positive. Users can still access their previously dismissed matches by turning on the  <strong>Show dismissed matches</strong> toggle in the Cloudflare dashboard.</p>
<h3 id="logo-search-ai-powered">Logo search (AI-powered)</h3>
<p>Logo search uses computer vision to detect domains using your visual assets, even if the domain name does not contain your brand string.</p>
<p>To set up a new logo query:</p>
<ol>
<li>Select <strong>Monitor Logos</strong> and select <strong>Add logo</strong>.</li>
<li>Add a name for your query and upload your logo. Only the <code>.png</code>, <code>.jpeg</code>, and <code>.jpg</code> file extensions are supported.</li>
<li>Set the threshold: Set a match threshold (the minimum is 75%). A higher score ensures high-precision matches, while a lower score catches remixed or slightly altered versions of your logo.</li>
<li>Select <strong>Save logo</strong>. The system will now scan newly detected infrastructure for visual matches.</li>
</ol>
<p>The browser will return to the <strong>Monitored Logos</strong> page, where you can access your query and configure notifications.</p>
<h2 id="investigate-a-query">Investigate a query</h2>
<p>In this section, the dashboard displays:</p>
<ul>
<li><strong>Domain overview</strong> where you can request to <a href="/security-center/investigate/change-categorization/">change categorization</a> and view the resolution history of your domain for up to seven days.</li>
<li><strong>WHOIS</strong> that provides details about the date the domain was created, registrant and nameservers.</li>
<li><strong>Domain history</strong> that provides information on the domain category and when it was last changed. Refer to <a href="/security-center/investigate/investigate-threats/">Investigate threats</a> for more details.</li>
<li><strong>URL Reports</strong> that provides information on any reported URL.</li>
</ul>
<p>To investigate a string query:</p>
<ol>
<li>Go to the <strong>Monitor Strings</strong> or <strong>Monitor Logos</strong> section to view all your queries.</li>
<li>Select a monitored query to inspect all the domains that matched your query.</li>
<li>Next to the domain, select <strong>Domain</strong> or <strong>URL</strong>. This will trigger a search on the <a href="/security-center/investigate/"><strong>Investigate</strong></a> section in a separate tab. URL scanner will also be triggered from <strong>Brand Protection</strong> through <strong>Security Center</strong> &gt; <strong>Investigate</strong>. You will also have access to a report which will be generated automatically. The report will display screenshots of the matched domain, and the registrar of your domain.</li>
</ol>
<h2 id="report-abuse">Report abuse</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="submit-abuse-report">Submit abuse report</h3>
@markup("md", "content/.markup/bodies/376.md")
</aside>
<p>To submit abuse reports directly from the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Brand Protection</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Monitor Strings</strong>, select the query you want to report.</li>
<li>Select <strong>Report to Cloudflare</strong>.</li>
<li>Fill in the details to submit an abuse report.</li>
<li>Select <strong>Submit</strong>.</li>
</ol>
<p>To view abuse reports, in the Cloudflare dashboard, go to the <strong>Abuse Reports</strong> page.</p>
<div class="nb-dash-button"></div>
<p>You can review abuse reports against your zones and any mitigations taken against reports in response.</p>
<p>You can also <strong>Request review</strong> of most mitigations.</p>
<h2 id="cease-and-desist-letters">Cease and Desist letters</h2>
<p>When you identify an infringing domain hosted outside of Cloudflare, you can generate a Cease and Desist (C&amp;D) letter directly from the dashboard. The system automatically pulls registrar data and WHOIS contact information (such as the registrant or registrar abuse email) and pre-fills your custom-branded templates.</p>
<p>When reviewing a matched domain, you have two paths to action depending on where the domain is hosted:</p>
<ul>
<li><strong>Report to Cloudflare</strong>: If the matched domain is using Cloudflare's network or registrar, trigger the integrated abuse reporting flow instantly.</li>
<li><strong>Generate a C&amp;D Letter</strong>: If the domain is hosted elsewhere, use one of the default templates or one you previously saved in the dashboard.</li>
</ul>
<h3 id="generate-a-c-d-letter">Generate a C&amp;D letter</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Brand Protection</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Monitor Strings</strong> and select a query to view its matched domains.</li>
<li>Next to the domain you want to take action on, click <strong>Generate C&amp;D Letter</strong>.</li>
<li>Choose a template. You can select from three default templates or from your own saved templates:
<ul>
<li><strong>Registrant - Exact Match</strong>: A cease and desist letter direct to a registrant of a domain that is an exact match to the protected trademark.</li>
<li><strong>Registrant - Similar Match</strong>: A cease and desist letter directed to a registrant of a domain that is confusingly similar to the protected trademark (1-character distance).</li>
<li><strong>Registrar - Trademark Infringement</strong>: A letter directed to a domain registrar regarding trademark infringement by their registrant.</li>
<li><strong>Registrar - Trademark Infringement &amp; Phishing</strong>: A letter directed to a domain registrar regarding trademark infringement and phishing by their registrant.</li>
</ul>
</li>
<li>Review and edit the pre-filled letter. The system auto-populates recipient data from WHOIS records.</li>
<li>Click <strong>Download</strong> to save the finalized PDF.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/375.md")
</aside>
<h2 id="brand-protection-api">Brand Protection API</h2>
<p>The <a href="/api/resources/brand_protection/">Brand Protection API</a> allows for programmatic management and integration with your <a href="https://www.cloudflare.com/en-gb/learning/security/glossary/what-is-a-security-operations-center-soc/">SOC</a> or <a href="https://www.cloudflare.com/en-gb/learning/security/what-is-siem/">SIEM</a>. Using the Brand Protection API, you can:</p>
<ul>
<li>Manage queries: Create, edit, or delete string and logo queries.</li>
<li>Data retrieval: Read and download matches for automated ingestion.</li>
<li>Query editing: Update existing query parameters without losing historical data.</li>
</ul>
<h2 id="notifications-and-alerts">Notifications and alerts</h2>
<p>Brand Protection integrates with Cloudflare's ANS (Alerts Notification Service) to provide configurable alerts when new domains are detected.</p>
<p>Any matches that are found during the new domain search are then inserted into an internal alerts table which triggers an alert for the user. This allows you to receive real-time notifications and take immediate action to investigate and potentially block any suspicious domains that may be attempting to impersonate your brand.</p>
<details><summary>Brand Protection Alerts</summary><strong>Who is it for?</strong><p>Customers who want a summary of activity related to <a href="/security-center/brand-protection/">Brand Protection</a>.</p>
<strong>Other options / filters</strong><p>You can set up Brand Protection Alerts on individual monitored queries. For more details, refer to <a href="/security-center/brand-protection/#brand-protection-alerts">Brand Protection Alerts</a>.</p>
<strong>Included with</strong><p>Professional plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Investigate and potentially block any suspicious domains that may be trying to impersonate your brand.</p>
</details><details><summary>Brand Protection Digest</summary><strong>Who is it for?</strong><p>Customers who want a summary of activity related to <a href="/security-center/brand-protection/">Brand Protection</a>.</p>
<strong>Other options / filters</strong><p>You can set up Brand Protection Digest on individual monitored queries. For more details, refer to <a href="/security-center/brand-protection/#brand-protection-alerts">Brand Protection Alerts</a>.</p>
<strong>Included with</strong><p>Professional plans or higher.</p>
<strong>What should you do if you receive one?</strong><p>Investigate and potentially block any suspicious domains that may be trying to impersonate your brand.</p>
</details><details><summary>Logo Match Alerts</summary><strong>Who is it for?</strong><p>Customers who want to receive a notification when the <a href="/security-center/brand-protection/">Brand Protection</a> system detects a new domain which is using the uploaded logo and might be infringing copyright.</p>
<strong>Other options / filters</strong><p>You can select the query that you want to be alerted on.</p>
<strong>Included with</strong><p>Enterprise plans.</p>
<strong>What should you do if you receive one?</strong><p>Review the domains and URLs that are potentially impersonating your brand.</p>
</details><details><summary>Security Insights</summary><strong>Who is it for?</strong><p>Customers who want to receive notifications based on security insights findings.</p>
<strong>Other options / filters</strong><p>You can select the insight(s) you want to be alerted on.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>Review the insight and decide whether you want to resolve it, archive it, or export it.</p>
</details><details><summary>Abuse report</summary><strong>Who is it for?</strong><p>Customers who want to be alerted in the event that an abuse report is filed against their website.</p>
<strong>Other options / filters</strong><p>You can filter the reports based on date, report status, report type, and domain.</p>
<strong>Included with</strong><p>All Cloudflare plans.</p>
<strong>What should you do if you receive one?</strong><p>View our guidance on <a href="/fundamentals/reference/report-abuse/abuse-report-obligations/">customer abuse report obligations</a> and more information on how to <a href="/fundamentals/reference/report-abuse/submit-report/">view and submit abuse reports</a>.</p>
</details>
<p>To set up a Brand Protection Alert:</p>
<ol>
<li>
<p>Go to <strong>Monitor Strings</strong> and locate the query for which you would like to create notifications.</p>
</li>
<li>
<p>Select <strong>alerts</strong>. This should redirect you to the <strong>Add Notification</strong> page, where you can configure what you want to be notified about, and how.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/374.md")
</aside>
<ol start="3">
<li>
<p>Create a notification name, add a description (optional), and select the monitored queries. You can also add a Webhook, and a notification email. You can add multiple email addresses.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>Manage your notifications in the <strong>All notifications</strong> tab. You can disable, edit, delete, or test them.</p>
<h2 id="subscriptions-and-limitations">Subscriptions and limitations</h2>
<ul>
<li>Self-serve users can subscribe directly to add monitoring capacity to their account.</li>
<li>You may only use the Brand Protection search tools to search for domains that may be attempting to impersonate your brand or a brand that has authorized you to conduct such search on its behalf.</li>
</ul>
