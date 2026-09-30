<p>Though Cloudflare automatically hides your origin server IP address when you <a href="/learning-paths/prevent-ddos-attacks/baseline/proxy-dns-records/">proxy your DNS records</a>, there are other ways to discover an IP address.</p>
<p>To prevent attackers from discovering your origin's IP address, review the following suggestions.</p>
<h2 id="rotate-ip-addresses">Rotate IP addresses</h2>
<p>DNS records are in the public domain, meaning that - even though your IP addresses are hidden once you proxy your DNS records - someone could uncover historical records of your addresses.</p>
<p>For additional security, you could rotate the IP addresses of your origin server, which would also require <a href="/dns/manage-dns-records/how-to/create-dns-records/#edit-dns-records">updating your DNS records</a> within Cloudflare.</p>
<h2 id="review-unproxied-dns-records">Review unproxied DNS records</h2>
<p>Unproxied DNS records - also known as <strong>DNS-only</strong> records - can sometimes contain origin IP information, especially those used for FTP or SSH.</p>
<p>Review these records to make sure they do not contain origin IP information or use <a href="/spectrum/">Cloudflare Spectrum</a> to proxy these records.</p>
<h2 id="conceal-unproxied-dns-records">Conceal unproxied DNS records</h2>
<p>If you need to have <strong>DNS-only</strong> records that contain origin IP information, use non-standard names for these records. This action makes dictionary scans of your DNS less likely to expose your origin IP address.</p>
<p>For example, instead of <code>ftp.example.com</code>, you could use <code>827450184590183489.example.com</code> or <code>cloudflare-docs-are-great.example.com</code>.</p>
<h2 id="evaluate-mail-infrastructure">Evaluate mail infrastructure</h2>
<p>If possible, do not host a mail service on the same server as the web resource you want to protect, since emails sent to non-existent addresses get bounced back to the attacker and reveal the mail server IP address.</p>
<p>Cloudflare recommends using non-contiguous IPs from different IP ranges.</p>
