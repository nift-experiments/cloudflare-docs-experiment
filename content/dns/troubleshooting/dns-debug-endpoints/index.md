<p>The following debug endpoints are available via <code>dig</code> or other DNS query tools.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7563.md")
</aside>
<h2 id="get-your-public-ip-address">Get your public IP address</h2>
<pre><code class="language-sh">dig @alex.ns.cloudflare.com chaos txt myip.cloudflare +short&#10;</code></pre>
<p>This command returns your public IP address, meaning the IP address that Cloudflare receives the DNS query from. This is useful for debugging when you need to know your own IP.</p>
<h2 id="find-your-connected-data-center">Find your connected data center</h2>
<pre><code class="language-sh">dig @alex.ns.cloudflare.com chaos txt id.server +short&#10;</code></pre>
<p>This command returns the Cloudflare data center you are connecting to, for DNS queries sent from where you execute this command.</p>
<h2 id="check-the-dns-software-version">Check the DNS software version</h2>
<pre><code class="language-sh">dig @alex.ns.cloudflare.com chaos txt version.bind +short&#10;</code></pre>
<p>This command returns the version of Cloudflare's authoritative DNS software that is running on the data center you are connected to. Usually, the same version is present on all Cloudflare data centers. However, since Cloudflare performs staged releases, different versions can exist on different data centers.</p>
<h2 id="get-your-ip-asn-and-country-code">Get your IP, ASN, and country code</h2>
<pre><code class="language-sh">dig @alex.ns.cloudflare.com txt whoami.cloudflare.net +short&#10;</code></pre>
<p>This command returns your public IP (same as the first command), your ASN, and the associated country code, all indicating where you are sending the query from.</p>
