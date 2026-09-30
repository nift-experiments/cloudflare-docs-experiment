<p class="article-summary">Set up email routing to forward incoming emails to existing mailboxes or process them with Workers.
</p>
<p>Route incoming emails sent to your domain to existing mailboxes, Workers for processing, or other destinations.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8606.md")
</aside>
<h2 id="set-up-your-domain">Set up your domain</h2>
<p>Before using Email Routing, configure your domain.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Routing</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Onboard Domain</strong>.</p>
</li>
<li>
<p>Choose a domain from your Cloudflare account. Optionally review the DNS records that Cloudflare will add to your root domain:</p>
<ul>
<li>MX records to route incoming emails to Cloudflare.</li>
<li>TXT record for SPF to authorize email routing.</li>
<li>TXT record for DKIM to provide authentication for routed emails.</li>
</ul>
</li>
<li>
<p>Select <strong>Done</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8605.md")
</aside>
<p>Once your domain is onboarded, you can start routing emails.</p>
<h2 id="route-your-first-email">Route your first email</h2>
<p>You can route your first email by setting up routing rules in the dashboard, or by processing emails with Workers.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8610.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<p>Now that you can route emails, explore advanced features:</p>
<ul>
<li><strong><a href="/email-service/get-started/send-emails/">Send outbound emails</a></strong> - Send emails from your applications</li>
<li><strong><a href="/email-service/api/route-emails/">API reference</a></strong> - Complete routing API documentation</li>
<li><strong><a href="/email-service/examples/">Examples</a></strong> - Real-world routing patterns</li>
</ul>
