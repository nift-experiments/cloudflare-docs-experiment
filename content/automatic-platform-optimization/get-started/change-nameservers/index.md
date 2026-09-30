<p>After you <a href="/automatic-platform-optimization/get-started/confirm-dns-records/">confirm your DNS records</a>, change your nameservers.</p>
<p>Updating your domain to use Cloudflare's nameservers is a critical step to ensure Cloudflare can optimize and protect your site. Nameservers are your primary DNS controller and identify the location of your domain on the Internet.</p>
<p>Domain registrars can take up to 24 hours to process the nameserver updates. You will receive an email from Cloudflare once your site is activated.</p>
<h2 id="lookup-domain-name-registration">Lookup domain name registration</h2>
<ol>
<li>Visit <a href="https://lookup.icann.org/">WHOIS</a> to look up your domain name registration.</li>
<li>In the text field, enter your domain name without <code>https://www.</code> and select <strong>Lookup</strong>.</li>
<li>From <strong>Domain Information</strong>, make note of the nameserver information that displays. You will update those nameservers to point to Cloudflare.</li>
</ol>
<p>We recommend keeping this browser tab or window open and opening a new tab or window for the next section.</p>
<h2 id="update-your-nameserver-with-your-domain-registrar">Update your nameserver with your domain registrar</h2>
<ol>
<li>Log in to the administrator account for your domain registrar.</li>
<li>Navigate to DNS Management.</li>
<li>Locate your nameserver information. Your nameservers should match the information from Step 3 of Lookup domain name registration.</li>
<li>Replace the existing nameserver information with the Cloudflare nameservers from Step 4 of Create the custom nameserver with Cloudflare.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3344.md")
</aside>
