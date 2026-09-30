<p>Phase 3 is when you make the actual switch to Cloudflare.</p>
<h2 id="1-final-verification"><ol>
<li>Final verification</li>
</ol></h2>
<p>Complete one last check of all DNS records in your Cloudflare dashboard for accuracy and ensure your BIND servers are still operational as a fallback if needed.</p>
<h2 id="2-update-nameservers-at-your-registrar"><ol start="2">
<li>Update nameservers at your registrar</li>
</ol></h2>
<ol>
<li>Log in to your domain registrar's control panel for each domain.</li>
<li>Navigate to the section for managing nameservers.</li>
<li>Replace your current on-prem BIND nameserver entries with your Cloudflare nameservers.</li>
<li>Add the Cloudflare nameservers assigned to your domain (Cloudflare will provide at least two).</li>
<li>Save the changes.</li>
</ol>
<h2 id="3-monitor-propagation"><ol start="3">
<li>Monitor propagation</li>
</ol></h2>
<ul>
<li>
<p>DNS nameserver changes can take time to propagate globally, typically anywhere from a few minutes to 48 hours (though often much faster due to lowered TTLs).</p>
</li>
<li>
<p>Use the commands exemplified below, replacing <code>yourdomain.com</code> by your actual domain.</p>
<ul>
<li><code>dig yourdomain.com NS @8.8.8.8</code> (query Google's DNS)</li>
<li><code>dig yourdomain.com NS @1.1.1.1</code> (query Cloudflare's DNS)</li>
<li><code>whois yourdomain.com</code></li>
<li><code>dig yourdomain.com @tld.nameserver.com</code> (<code>tld.nameserver.com</code> is the nameserver of your domain's TLD. You can find this information by querying it as <code>dig com ns +short</code> where <code>.com</code> is the example.)</li>
</ul>
<p>You are looking for the Cloudflare nameservers to be reported consistently.</p>
</li>
</ul>
<h2 id="4-initial-testing"><ol start="4">
<li>Initial testing</li>
</ol></h2>
<p>Once propagation appears to be widespread, perform basic resolution tests for critical records (for example, your website's <code>A</code> record and any <code>MX</code> records, if you had them set up).</p>
<ul>
<li><code>dig yourdomain.com A +short</code></li>
<li><code>dig yourdomain.com MX +short</code></li>
</ul>
