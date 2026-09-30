<p>When you set up a gateway with a DNSLink record, that gateway is restricted to a particular piece of content — either a specific Content Identifier (CID) or an Interplanetary Name Service (IPNS) hostname. This is called a restricted gateway.</p>
<p>A restricted gateway differs from a <a href="/web3/ipfs-gateway/concepts/universal-gateway/">universal gateway</a>, which allows users to access any content hosted on the IPFS network.</p>
<h2 id="what-is-dnslink">What is DNSLink?</h2>
<p>Every file on <a href="/web3/ipfs-gateway/concepts/ipfs/">IPFS</a> is identified by a <a href="https://docs.ipfs.io/concepts/glossary/#cid">CID</a> — a long string like <code>bafybeiaysi4s6lnjev27ln5icwm6tueaw2vdykrtjkwiphwekaywqhcjze</code>. These CIDs are not practical for end users to type or remember, the same way IP addresses (<code>192.0.2.1</code>) are not practical compared to domain names (<code>example.com</code>).</p>
<p>DNSLink solves this by mapping a human-readable domain name to an IPFS CID through a DNS TXT record. You put your website files into an IPFS directory and create a DNSLink record pointing your domain to that directory's CID. Users then access your site through a readable URL like <code>https://cf-ipfs.com/ipns/en.wikipedia-on-ipfs.org/</code>, and the gateway resolves it to the correct CID.</p>
<p>DNSLink also simplifies content updates. When you publish a new version of your site, update the DNSLink record to point to the new CID and the gateway serves the new version automatically — no need to share a new URL.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15802.md")
</aside>
<h2 id="how-is-it-used-with-cloudflare">How is it used with Cloudflare?</h2>
<p>You have the option to specify the DNSLink when you <a href="/web3/how-to/manage-gateways/#create-a-gateway">create an IPFS gateway</a>, which serves as a custom hostname that directs users to a website already hosted on IPFS.</p>
<p>By default, your DNSLink path is <code>/ipns/onboarding.ipfs.cloudflare.com</code>. If you choose to put your website in a different content folder hosted at your own IPFS node or with a pinning service, you will need to specify that value.</p>
<p>For example, the default DNSLink record for <code>www.example.com</code> would look like this:</p>
<table>
<thead>
<tr>
<th>Record type</th>
<th>Name</th>
<th>Content</th>
</tr>
</thead>
<tbody>
<tr>
<td>TXT</td>
<td><code>_dnslink.www.example.com</code></td>
<td><code>dnslink=/ipns/onboarding.ipfs.cloudflare.com</code></td>
</tr>
</tbody>
</table>
<p>For more details about the DNS records created by the IPFS gateway, refer to <a href="/web3/reference/gateway-dns-records/">Gateway DNS records</a>.</p>
