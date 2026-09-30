<h2 id="submit-reports">Submit reports</h2>
<p>Cloudflare provides security, performance, and reliability services to millions of websites. When you report abuse involving a website that uses Cloudflare, Cloudflare's ability to respond depends on the Cloudflare service involved. Many reports involve websites using Cloudflare's pass-through CDN and security services, while others involve domains registered through Cloudflare Registrar or content hosted on Cloudflare's developer platform.</p>
<p>If you find abusive content on a website that uses Cloudflare, you can submit a report in one of three ways:</p>
<ul>
<li><strong>Public form</strong>: Use <a href="https://abuse.cloudflare.com/">Submit an abuse report</a> to report abuse to Cloudflare. This form is available to anyone on the Internet.</li>
<li><strong>Cloudflare dashboard</strong>: Entitled Cloudflare customers can submit abuse reports from the <strong>Abuse reports</strong> page. You must have the <strong>Trust &amp; Safety</strong>, <strong>Admin</strong>, or <strong>Super Admin</strong> role.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li><strong>Cloudflare API</strong>: Entitled Cloudflare customers can submit abuse reports using the <a href="/api/resources/abuse_reports/">Abuse Reports API</a>. You must have the <strong>Trust &amp; Safety</strong>, <strong>Admin</strong>, or <strong>Super Admin</strong> role.</li>
</ul>
<h2 id="view-submitted-reports">View submitted reports</h2>
<p>Entitled Cloudflare customers with the <strong>Trust &amp; Safety</strong>, <strong>Admin</strong>, or <strong>Super Admin</strong> role can view abuse reports against content associated with their account.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Abuse reports</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Optionally, filter reports by date, report status, report type, or domain.</li>
</ol>
<p>If Cloudflare applied a mitigation to your website because of an abuse report, you may be able to request a review of that mitigation in the dashboard or using the <a href="/api/resources/abuse_reports/subresources/mitigations/">Abuse Report Mitigations API</a>. Cloudflare will review the request and may remove the mitigation.</p>
<h2 id="receive-notifications">Receive notifications</h2>
<p>You can enable abuse notifications for your account to configure email, webhook, or PagerDuty alerts about new abuse reports against your websites.</p>
<p>For help setting up alerts, refer to <a href="/notifications/get-started/">Configure Cloudflare notifications</a>.</p>
