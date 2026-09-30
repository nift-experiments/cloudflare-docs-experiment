<p class="article-summary">Understand bounce handling and reputation management for optimal email delivery.</p>
<p>When you send an email, there is no guarantee it reaches the recipient's inbox. Inbox providers like Gmail, Yahoo, Outlook, and iCloud invest heavily in filtering out unwanted email. If you send poorly targeted emails, have high bounce rates, or trigger spam complaints, these providers may flag your domain as untrustworthy. Once that happens, even your legitimate emails can end up in spam or be blocked outright.</p>
<p>This concept is referred to as email deliverability: maintaining a healthy sending reputation so that inbox providers trust your emails. Cloudflare Email Service helps with this by automatically handling bounces, managing suppression lists, and authenticating your emails through SPF, DKIM, and DMARC.</p>
<h2 id="bounces">Bounces</h2>
<p>Bounces occur when emails cannot be delivered to recipients. There are two types of bounces: <strong>hard bounces</strong> and <strong>soft bounces</strong>.</p>
<h3 id="hard-bounces">Hard bounces</h3>
<p>Hard bounces are permanent delivery failures that occur when:</p>
<ul>
<li>The recipient address does not exist.</li>
<li>The recipient domain does not exist.</li>
<li>The receiving server permanently rejects the recipient.</li>
</ul>
<p><strong>Hard bounces are never retried</strong> because the failure is permanent. Emails that hard bounce will generate a bounce notification to the sender address and can be monitored through <a href="/email-service/observability/metrics-analytics/">analytics</a>.</p>
<p>Email Service adds eligible recipient-side hard bounces to your <a href="/email-service/concepts/suppressions/">suppression list</a>. Suppressions have no expiration when the mailbox or domain does not exist.</p>
<p>They also have no expiration when the recipient remains unavailable across repeated delivery attempts. Other eligible hard-bounce suppressions last seven days.</p>
<h3 id="soft-bounces">Soft bounces</h3>
<p>Soft bounces are temporary failures that may succeed if retried:</p>
<ul>
<li>Recipient mailbox is full</li>
<li>Email server temporarily down</li>
<li>Rate limiting or greylisting</li>
</ul>
<p>Cloudflare automatically retries soft bounces with exponential backoff. Eligible recipient-side failures create a 24-hour suppression.</p>
<h2 id="reputation-management">Reputation management</h2>
<p>Cloudflare automatically manages:</p>
<ul>
<li><strong>IP reputation</strong>: Managed sending infrastructure optimized for deliverability</li>
<li><strong>Domain authentication</strong>: DKIM signing, SPF alignment, DMARC compliance</li>
<li><strong>Feedback processing</strong>: ISP complaint handling and suppression list management</li>
</ul>
<h3 id="best-practices">Best practices</h3>
<h4 id="content-and-list-hygiene">Content and list hygiene</h4>
<p>Avoid content that can trigger spam-detection or can be perceived as unwanted content:</p>
<ul>
<li>Avoid spam trigger words (FREE, URGENT, GUARANTEED)</li>
<li>Include both HTML and plain text versions</li>
<li>Use legitimate URLs and clear sender identification</li>
</ul>
<p>Ensure that your email lists are clean and contain intended recipients:</p>
<ul>
<li>Validate emails before sending</li>
<li>Implement double opt-in for subscriptions</li>
<li>Remove hard bounced addresses immediately</li>
</ul>
<p>Ensure that your deliverability stays above key metrics to avoid affecting your email sending reputation:</p>
<ul>
<li>Delivery rate &gt;95%</li>
<li>Hard bounce rate &lt; 2%</li>
<li>Complaint rate &lt; 0.1%</li>
</ul>
<h4 id="use-separate-domains-for-separate-purposes">Use separate domains for separate purposes</h4>
<p>Each domain builds its own deliverability reputation with inbox providers. Use separate domains or subdomains for different types of email so that one category does not affect the reputation of another. For example:</p>
<ul>
<li><code>notifications.yourdomain.com</code> for transactional emails (order confirmations, password resets)</li>
<li><code>marketing.yourdomain.com</code> for marketing and promotional emails</li>
<li><code>yourdomain.com</code> for important account-related communications</li>
</ul>
<p>This way, if marketing emails generate higher complaint rates, your transactional email deliverability is not impacted. Each domain can be onboarded separately through <a href="/email-service/configuration/domains/">domain configuration</a>.</p>
