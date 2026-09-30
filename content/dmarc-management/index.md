<div class="nb-description">
@markup("md", "content/.markup/bodies/1138.md")
</div>
<div class="nb-plan">
<p>Available on all plans</p>
</div>
<p>When someone receives an email that claims to be from your domain, email servers check whether that message is authentic. Three DNS-based mechanisms handle this verification:</p>
<ul>
<li><strong><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-spf-record/">SPF (Sender Policy Framework)</a></strong> confirms the email was sent from an IP address or domain your domain authorizes.</li>
<li><strong><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dkim-record/">DKIM (DomainKeys Identified Mail)</a></strong> authenticates the sender's domain and verifies the email content was not altered in transit, using a cryptographic signature.</li>
<li><strong><a href="https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/">DMARC (Domain-based Message Authentication Reporting and Conformance)</a></strong> ties SPF and DKIM together and tells receiving servers what to do when a check fails (for example, reject the email, quarantine it, or take no action).</li>
</ul>
<p>Cloudflare DMARC Management helps you track every source that is sending emails from your domain and review DMARC reports for each source. These reports show whether messages sent from your domain are passing SPF, DKIM, and DMARC checks — so you can identify unauthorized senders and protect your domain from being used in phishing or spoofing attacks.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1137.md")
</aside>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1139.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/1140.md")
</div>
