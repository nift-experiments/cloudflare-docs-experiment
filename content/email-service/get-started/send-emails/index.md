<p class="article-summary">Send your first email using the Workers binding, the REST API, or SMTP.
</p>
<p>Send emails from your applications using Cloudflare Email Service. You can use the <strong>Workers binding</strong> for applications built on Cloudflare Workers, the <strong>REST API</strong> from any platform, or <strong>SMTP</strong> from any SMTP-capable application or mail client.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8598.md")
</aside>
<h2 id="set-up-your-domain">Set up your domain</h2>
<p>Before using Email Sending, configure your domain.</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Compute</strong> &gt; <strong>Email Service</strong> &gt; <strong>Email Sending</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Onboard Domain</strong>.</p>
</li>
<li>
<p>Choose a domain from your Cloudflare account. Optionally review the DNS records that Cloudflare will add to the <code>cf-bounce</code> subdomain of your domain:</p>
<ul>
<li>MX records to route bounce emails to Cloudflare.</li>
<li>TXT record for SPF to authorize sending emails.</li>
<li>TXT record for DKIM to provide authentication for emails sent from your domain.</li>
<li>TXT record for DMARC on <code>_dmarc.yourdomain.com</code>.</li>
</ul>
</li>
<li>
<p>Select <strong>Done</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8597.md")
</aside>
<p>Once your domain is onboarded, you can start sending emails.</p>
<h2 id="send-your-first-email">Send your first email</h2>
<p>You can send your first email using the Workers binding, the REST API, or SMTP.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8603.md")
</div></div>
<h2 id="next-steps">Next steps</h2>
<p>Now that you can send emails, explore advanced features:</p>
<ul>
<li><strong><a href="/email-service/get-started/route-emails/">Route incoming emails</a></strong> - Process emails sent to your domain</li>
<li><strong><a href="/email-service/api/send-emails/">API reference</a></strong> - Complete API documentation</li>
<li><strong><a href="/email-service/examples/">Examples</a></strong> - Real-world implementation patterns</li>
</ul>
