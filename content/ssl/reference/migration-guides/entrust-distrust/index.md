<p>Google Chrome and Mozilla have announced they will no longer trust certificates issued from Entrust's root CAs.</p>
<p>Since Entrust is not within the <a href="/ssl/reference/certificate-authorities/">certificate authorities</a> used by Cloudflare, this change may only affect customers who upload <a href="/ssl/edge-certificates/custom-certificates/">custom certificates</a> issued by Entrust.</p>
<h2 id="the-decision">The decision</h2>
<p>New Entrust certificates issued on <strong>November 12, 2024 or after</strong> will not be trusted on Chrome by default. And new Entrust certificates issued on <strong>December 1, 2024 or after</strong> will not be trusted on Mozilla by default.</p>
<p>Refer to the announcements (<a href="https://security.googleblog.com/2024/06/sustaining-digital-certificate-security.html">Chrome</a>, <a href="https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/jCvkhBjg9Yw?pli=1">Mozilla</a>) for a full list of roots that will be distrusted.</p>
<h2 id="entrust-s-response">Entrust's response</h2>
<p>To prevent their customers from facing issues, Entrust has partnered with SSL.com, a different certificate authority, trusted by both Chrome and Mozilla.</p>
<p>This means that Entrust certificates will be issued using SSL.com roots.</p>
<h2 id="cloudflare-managed-certificates">Cloudflare-managed certificates</h2>
<p>Since Cloudflare also <a href="/ssl/reference/certificate-authorities/">partners with SSL.com</a>, you can switch from uploading custom certificates to using Cloudflare-managed certificates. This change brings the following advantages:</p>
<ul>
<li>Use <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced certificates</a> to have more control and flexibility while also benefitting from automatic renewals.</li>
<li>Enable <a href="/ssl/edge-certificates/additional-options/total-tls/">Total TLS</a> to automatically issue certificates for your <a href="/dns/proxy-status/">proxied hostnames</a>.</li>
<li>Use <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">Delegated DCV</a> to reduce manual intervention when renewing certificates for <a href="/dns/zone-setups/partial-setup/">partial (CNAME) setup</a> zones.</li>
<li>If you are a SaaS provider, extend the benefits of automatic renewals to your customers by specifying SSL.com as the certificate authority when <a href="/api/resources/custom_hostnames/methods/create/">creating</a> or <a href="/api/resources/custom_hostnames/methods/edit/">editing</a> your custom hostnames (API only).</li>
</ul>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/ssl/reference/certificate-authorities/">Use Cloudflare with SSL.com certificates</a></li>
<li><a href="https://security.googleblog.com/2024/06/sustaining-digital-certificate-security.html">Google Security Blog</a></li>
<li><a href="https://www.entrust.com/tls-certificate-information-center">Entrust TLS Certificate Information Center</a></li>
</ul>
