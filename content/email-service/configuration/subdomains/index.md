<p>Email Routing is a zone-level feature that applies to the apex domain (for example, <code>example.com</code>) by default. Email Sending treats each domain separately and is onboarded per domain. You can extend either service to subdomains of the same zone, such as <code>mail.example.com</code> or <code>corp.example.com</code>, but the onboarding flow differs between the two.</p>
<p>A zone can have up to 30 domains configured for Email Routing or Email Sending combined, including the apex domain. Refer to <a href="/email-service/platform/limits/">Limits</a> for the full list of platform limits.</p>
<h2 id="add-a-subdomain-to-email-routing">Add a subdomain to Email Routing</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Select the apex domain, then open <strong>Settings</strong>.</li>
<li>Under <strong>Subdomains</strong>, enter the subdomain you want to enable in the inline form and submit it.</li>
</ol>
<p>Cloudflare adds the required DNS records to the subdomain. Once the records propagate, you can create <a href="/email-service/configuration/email-routing-addresses/">routing rules</a> on the subdomain in the same way as on the apex domain.</p>
<h2 id="add-a-subdomain-to-email-sending">Add a subdomain to Email Sending</h2>
<p>Email Sending treats a subdomain as a separate sending domain. Onboard the subdomain through the standard onboarding flow:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Sending</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Select <strong>Onboard Domain</strong> and choose the subdomain you want to send from. The onboarding flow adds the <code>cf-bounce</code> MX, SPF, DKIM, and DMARC records to the subdomain.</li>
<li>Select <strong>Done</strong>.</li>
</ol>
<p>Once verified, you can send emails from addresses on the subdomain (for example, <code>notifications@mail.example.com</code>) using either the <a href="/email-service/api/send-emails/rest-api/">REST API</a> or the <a href="/email-service/api/send-emails/workers-api/">Workers binding</a>.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/email-service/configuration/domains/">Domain configuration</a> — manage DNS records for sending and routing.</li>
<li><a href="/email-service/configuration/email-routing-addresses/">Routing rules and addresses</a> — create routing rules on subdomains.</li>
<li><a href="/email-service/concepts/deliverability/">Deliverability</a> — separate subdomains for different email types.</li>
</ul>
