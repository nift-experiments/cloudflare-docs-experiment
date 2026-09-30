<p>Certificate Transparency (CT) Monitoring is an <a href="#opt-in-and-out">opt-in</a> feature that lets you double-check any SSL/TLS certificates issued for your domain.</p>
<p>CT Monitoring alerts are triggered whenever a certificate that covers your monitored domain is issued by a <a href="/ssl/reference/certificate-authorities/">Certificate Authority (CA)</a> and added to a public CT log. Alerts for certificates Cloudflare issues on your behalf, including backup certificates, are automatically filtered out. For more information, refer to <a href="https://blog.cloudflare.com/certificate-transparency-monitoring-ga">Certificate Transparency Monitoring filtering behavior</a>, or to the <a href="https://blog.cloudflare.com/introducing-certificate-transparency-monitoring/">introductory blog post</a> to learn more about how CT Monitoring works.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="aspects-to-consider">Aspects to consider</h3>
@markup("md", "content/.markup/bodies/14144.md")
</aside>
<hr />
<h2 id="opt-in-and-out">Opt in and out</h2>
<p>Alerts are turned off by default. If you want to receive alerts, go to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates#ct-alerting-card"><strong>Edge Certificates</strong></a> page and turn on <strong>Certificate Transparency Monitoring</strong>, then select <strong>Add Email</strong>.</p>
<p>To stop receiving alerts, turn off <strong>Certificate Transparency Monitoring</strong> or remove your email from the feature card.</p>
<hr />
<h2 id="emails-to-be-concerned-about">Emails to be concerned about</h2>
<p>Cloudflare filters out the certificates it issues for you, so every alert you get is worth a quick look.</p>
<p>Most alerts are routine. Open the email and check three things:</p>
<ol>
<li><strong>Your domain.</strong> Does it match what you own?</li>
<li><strong>The issuer.</strong> Did you or your organization request this certificate, or was it requested by a service you use? The issuer is listed as the <a href="/ssl/reference/certificate-authorities/">Certificate Authority</a> in the email.</li>
<li><strong>The DNS names and validity dates.</strong> Do they look reasonable?</li>
</ol>
<p>If you can confirm that your organization or a service you use requested the certificate, no action is required. Otherwise, investigate the issuance with your security team or certificate provider. You can review certificates configured on Cloudflare from the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates">Edge Certificates page</a> in the dashboard. For external certificates, review the CT log entry or use <a href="https://crt.sh/">Certificate Search</a>.</p>
<p>Take action if:</p>
<ul>
<li>You do not recognize the issuer or did not request the certificate.</li>
<li>You do not recognize the DNS names.</li>
<li>Your website has been acting strangely.</li>
</ul>
<hr />
<h2 id="how-to-take-action">How to take action</h2>
<h3 id="option-1-contact-certificate-authorities">Option 1: Contact certificate authorities</h3>
<p>Only Certificate Authorities can revoke malicious certificates. If you believe an illegitimate certificate was issued for your domain, contact the Certificate Authority listed as the <strong>Issuer</strong> in the email.</p>
<ul>
<li>
<p><a href="https://support.globalsign.com/">GlobalSign support</a></p>
</li>
<li>
<p><a href="https://www.godaddy.com/contact-us?sp_hp=B">GoDaddy support</a></p>
</li>
<li>
<p><a href="https://pki.goog/faq/">Google Trust Services support</a></p>
</li>
<li>
<p><a href="https://www.identrust.com/support/support-team">IdenTrust support</a></p>
</li>
<li>
<p><a href="https://letsencrypt.org/contact/">Let's Encrypt support</a></p>
</li>
<li>
<p><a href="https://sectigo.com/support">Sectigo support</a></p>
</li>
<li>
<p><a href="https://www.ssl.com/submit-a-ticket/">SSL.com support</a></p>
</li>
</ul>
<h3 id="option-2-contact-domain-registrars">Option 2: Contact domain registrars</h3>
<p>Domain registrars may be able to <strong>suspend</strong> potentially malicious domains. If, for example, you notice that a malicious domain was registered through GoDaddy, contact GoDaddy’s support team to see if they can help you. Do the same for other registrars.</p>
<h3 id="option-3-improvise">Option 3: Improvise</h3>
<p>There are other ways to combat malicious certificates. You can warn your visitors with an on-site notification or ask browser makers (Google for Chrome, etc.) to block these domains.</p>
<p>If someone is attempting to impersonate you online, you should absolutely take action. This is usually difficult to recognize, so exercise caution. <strong>Remember: the vast majority of certificates are not malicious. Only take action if you believe something is wrong.</strong></p>
<hr />
<h2 id="http-public-key-pinning">HTTP Public Key Pinning</h2>
<p>Certificate Transparency Monitoring addresses the same problems as HTTP Public Key Pinning (HPKP), but with <a href="https://scotthelme.co.uk/im-giving-up-on-hpkp/">fewer technical issues</a>.</p>
<p>Cloudflare does not offer or support HPKP and advises against using it with Universal SSL.</p>
