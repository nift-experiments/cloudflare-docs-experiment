<p>To download an ad-hoc DDoS report, generate a PDF report file by selecting <strong>Print report</strong> in your <a href="/ddos-protection/reference/analytics/">analytics dashboard</a>.</p>
<p>WAF/CDN customers can download a monthly report in Account Home &gt; <strong>Security Center</strong>, by selecting <a href="/analytics/account-and-zone-analytics/app-security-reports/">Security Reports</a> and downloading the desired monthly report.</p>
<p>Additionally, if you are a Magic Transit or Spectrum BYOIP customer, you will receive weekly DDoS reports by email with a snapshot of the DDoS attacks that Cloudflare detected and mitigated in the previous week.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/7454.md")
</aside>
<h2 id="weekly-ddos-reports">Weekly DDoS reports</h2>
<p>Cloudflare sends DDoS reports via email from <code>no-reply@notify.cloudflare.com</code> to users with the Super Administrator role on accounts with prefixes advertised by Cloudflare.</p>
<p>Reports contain the following information:</p>
<ul>
<li>Total number of DDoS attacks</li>
<li>Largest DDoS attack in packets per second (pps) and bits per second (bps)</li>
<li>Changes in DDoS attacks compared to the previous report</li>
<li>Top attack protocols</li>
<li>Top targeted IP addresses</li>
<li>Top targeted destination ports</li>
<li>Total potential downtime prevented (a sum of the duration of all attacks in that week)</li>
<li>Total bytes mitigated (a sum of all the mitigated attack traffic)</li>
</ul>
<p>Cloudflare issues DDoS reports via email each Tuesday. Reports summarize the attacks that occurred from Monday of the previous week to Sunday of the current week. For example, a report issued on 2020-11-10 (Tuesday) summarizes activity from 2020-11-02 (Monday) to 2020-11-08 (Sunday).</p>
<p>To receive real-time attack alerts, configure <a href="/ddos-protection/reference/alerts/">DDoS alerts</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/7453.md")
</aside>
<h3 id="example-report">Example report</h3>
<p>The following image shows an example DDoS report:</p>
<p><img src="/assets/upstream/images/ddos-protection/ddos-report-email.png" alt="Example email sent with a weekly DDoS report" /></p>
<p>When Cloudflare does not detect any L3/4 DDoS attacks in the prior week, Cloudflare sends a confirmation report:</p>
<p><img src="/assets/upstream/images/ddos-protection/ddos-report-no-attacks.png" alt="Example report email sent when Cloudflare does not detect any DDoS attack in the previous week" /></p>
<h3 id="manage-reporting-subscriptions">Manage reporting subscriptions</h3>
<p>Magic Transit and Spectrum BYOIP customers will receive the weekly DDoS report automatically.</p>
<p>To stop receiving DDoS reports, select the unsubscribe link at the bottom of the report email. To resubscribe after opting out, contact Cloudflare support.</p>
