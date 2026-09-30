<p>Most Internet service providers and some hosting providers dynamically update their customer's IP addresses. If this situation applies to you, you need an automated solution to dynamically update your DNS records in Cloudflare.</p>
<h2 id="cloudflare-api">Cloudflare API</h2>
<p>Create a script to monitor IP address changes and then have that script push changes to the <a href="/api/resources/dns/subresources/records/methods/update/">Cloudflare API</a>.</p>
<h2 id="ddclient">ddclient</h2>
<p><a href="https://github.com/ddclient/ddclient">ddclient</a> is a third-party Perl client used to update dynamic DNS entries for accounts on various DNS providers.</p>
