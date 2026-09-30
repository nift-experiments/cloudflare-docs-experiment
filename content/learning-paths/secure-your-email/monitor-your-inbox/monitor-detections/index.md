<p>Spam and Malicious emails are blocked outright by Email security, but Suspicious and Spoof dispositions should be monitored. Suspicious messages should be investigated by a security analyst to determine the legitimacy of the message.</p>
<p><a href="/cloudflare-one/email-security/phishguard/">PhishGuard</a> (Cloudflare's managed email security service) can review these messages for you and move them from the end user inbox if they are deemed malicious.</p>
<p>Messages that receive a Spoof disposition should be investigated because it signals that the traffic is either non-compliant with your email authentication process <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/">SPF</a>, <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/">DKIM</a>, <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/">DMARC</a>, or has a mismatching Envelope From and Header From value.</p>
<p>In most cases, a Spoof disposition is triggered by a legitimate third-party mail service. If you determine that the Spoofed email is a legitimate business use case, you can either:</p>
<ul>
<li>Update your email authentication records.</li>
<li>Add an acceptable sender <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">allow policy</a> to exempt messages from the Spam, Spoof, or Bulk disposition, but not Malicious or Suspicious, so the content of the message can still be monitored.</li>
</ul>
<h2 id="search-email-messages">Search email messages</h2>
<p>Email security offers a variety of ways for you to better examine and understand your message traffic:</p>
<p>You can search for emails that have been processed by Email security, whether they are marked with a <a href="/email-security/reference/dispositions-and-attributes/">detection disposition</a> or not.</p>
<p>There are three ways for searching emails:</p>
<ul>
<li>Popular screen: A popular screen allows you to view messages based on common pre-defined criteria.</li>
<li>Regular screen: A regular screen allows you to investigate your inbox by inserting a term to screen across all criteria.</li>
<li>Advanced screen: The advanced screen criteria gives you the option to narrow message results based on specific criteria. The advanced screen has several options (such as keywords, subject keywords, sender domain, and more) to scan your inbox.</li>
</ul>
<p>Additional information on search can be found on the <a href="/cloudflare-one/email-security/investigation/search-email/#screen-criteria">Screen criteria</a> documentation.</p>
<h3 id="export-messages">Export messages</h3>
<p>With Email security, you can export messages to a CSV file. Via the dashboard, you can export up to 1,000 rows. If you want to export all messages, you can use the <a href="https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/methods/get/">API</a>.</p>
