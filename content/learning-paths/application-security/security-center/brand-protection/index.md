<p>Brand Protection allows you to proactively identify and mitigate domain impersonation and phishing attacks. By monitoring newly registered domains and visual assets across the Internet, Cloudflare helps protect your brand's reputation and prevents your customers or employees from submitting sensitive information to fraudulent sites.</p>
<p>Common threats include:</p>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Typosquatting">Typosquatting</a>: For example, typing <code>cloudfalre.com</code> instead of <code>cloudflare.com</code>.</li>
<li>Concatenation of services (<code>cloudflare-service.com</code>) often registered by attackers to trick unsuspecting victims into submitting private information such as passwords.</li>
<li><a href="https://en.wikipedia.org/wiki/IDN_homograph_attack">Homoglyph attacks</a> that use lookalike characters to trick unsuspecting victims.</li>
</ul>
<h2 id="types-of-queries">Types of queries</h2>
<ol>
<li>
<p><a href="/security-center/brand-protection/#domain-search">Domain search</a>: allows you to search for domains that might be trying to impersonate your brand.</p>
</li>
<li>
<p><a href="/security-center/brand-protection/#logo-queries">Logo search</a>: allows you to search for logos that might look and feel like your brand's logo.</p>
</li>
</ol>
<h2 id="alerts">Alerts</h2>
<p>Brand Protection integrates with Cloudflare's ANS (Alerts Notification Service) to provide configurable alerts when new domains are detected.</p>
<p>Any matches that are found during the new domain search are then inserted into an internal alerts table which triggers an alert for the user. This allows you to receive real-time notifications and take immediate action to investigate and potentially block any suspicious domains that may be attempting to impersonate your brand.</p>
