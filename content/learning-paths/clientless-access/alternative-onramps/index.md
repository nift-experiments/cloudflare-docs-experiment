<p>As discussed in the previous modules, almost everything you do with the Cloudflare reverse proxy requires <a href="/learning-paths/clientless-access/initial-setup/add-site/">adding a site</a> to Cloudflare. That public DNS record (or its subdomains) becomes the domain on which your users access your private applications. This method is exceptionally secure and transparent; each domain and subdomain has access to the Cloudflare web security portfolio, are inherently DDoS protected, and receive an obfuscated origin IP. For these reasons, using a <a href="/learning-paths/clientless-access/connect-private-applications/">public hostname on Cloudflare</a> is the recommended method to onboard applications for clientless user access.  However, there may be times in which a public DNS record cannot be created, or other situations that prevent administrators from using this method.</p>
<h2 id="objectives">Objectives</h2>
<p>By the end of this module, you will be able to:</p>
<ul>
<li>Connect to private web applications using their private hostnames.</li>
</ul>
