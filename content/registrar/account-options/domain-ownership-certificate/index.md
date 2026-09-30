<p>A domain ownership certificate is a PDF letter that certifies Cloudflare is the registrar of record for your domain and lists the domain's current registration data. You can use it as proof of ownership when a third party (such as a bank, marketplace, or legal entity) requires written confirmation that you control the domain.</p>
<p>The certificate is generated on demand and is automatically populated with your domain's current WHOIS information and the date it was generated. It includes:</p>
<ul>
<li>A certification statement confirming that Cloudflare, an ICANN-accredited registrar, is the registrar for the domain.</li>
<li><strong>Exhibit A</strong>, containing the domain's registration data:
<ul>
<li>Creation date and registry expiry date.</li>
<li>Registrant, administrative, technical, and billing contacts.</li>
<li>Name servers.</li>
</ul>
</li>
</ul>
<p>The contact details shown on the certificate reflect the authoritative contact information Cloudflare has on file, not the redacted values published in public WHOIS. To review or update this information, refer to <a href="/registrar/account-options/domain-contact-updates/">Registrant contact updates</a>.</p>
<h2 id="generate-a-certificate">Generate a certificate</h2>
<p>To download a domain ownership certificate:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12763.md")
</div>
<p>Your browser downloads a PDF named <code>&lt;domain&gt;_ownership_letter.pdf</code>.</p>
<h2 id="prerequisites-and-restrictions">Prerequisites and restrictions</h2>
<p>You can only generate a certificate when:</p>
<ul>
<li>The domain is registered with (sponsored by) Cloudflare Registrar.</li>
<li>You have permission to view the domain's contact information.</li>
<li>The domain has registrant contact information on file.</li>
</ul>
<p>If any of these conditions are not met, the certificate cannot be generated.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12762.md")
</aside>
