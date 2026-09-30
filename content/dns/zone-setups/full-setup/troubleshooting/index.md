<p>If you see unexpected results when <a href="/dns/zone-setups/full-setup/setup/">changing your nameservers</a>, review the following troubleshooting questions.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7940.md")
</aside>
<h2 id="is-a-ds-record-present-at-your-registrar">Is a DS record present at your registrar?</h2>
<p>You need to remove any pre-Cloudflare <strong>DS</strong> records at your registrar to update your authoritative nameservers. This will disable DNSSEC and allow Cloudflare to resolve your domain name.</p>
<p>You can then <a href="/dns/zone-setups/full-setup/setup/#4-re-enable-dnssec">re-enable DNSSEC</a> in Cloudflare and at your registrar after you have changed your nameservers.</p>
<h2 id="do-the-nameservers-at-your-registrar-exactly-match-the-values-provided-by-cloudflare">Do the nameservers at your registrar exactly match the values provided by Cloudflare?</h2>
<p>If the nameservers in your registrar do not exactly match those provided by Cloudflare, your domain will not resolve correctly.</p>
<h2 id="are-additional-nameservers-listed-at-your-registrar">Are additional nameservers listed at your registrar?</h2>
<p>If so, you should remove these nameservers.</p>
<p>You should have only Cloudflare nameservers listed at your registrar.</p>
<h2 id="have-you-waited-longer-than-24-hours">Have you waited longer than 24 hours?</h2>
<p>For some registrars, you will need to wait up to 24 hours for updates to your nameservers.</p>
