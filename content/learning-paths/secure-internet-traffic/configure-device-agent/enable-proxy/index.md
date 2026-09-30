<p>With Cloudflare Gateway, you can log and filter DNS, network, and HTTP traffic from devices running the Cloudflare One Client. This includes traffic to the public Internet and traffic directed to your private network. DNS filtering is enabled by default since the Cloudflare One Client sends DNS queries to Cloudflare's public DNS resolver, <a href="/1.1.1.1/">1.1.1.1</a>. To enable network and HTTP filtering, you will need to allow Cloudflare Gateway to proxy that traffic.</p>
<h2 id="enable-the-proxy">Enable the proxy</h2>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>Enable <strong>Allow Secure Web Gateway to proxy traffic</strong> for TCP.</li>
<li>(Recommended) To proxy all port <code>443</code> traffic, including internal DNS queries, select <strong>UDP</strong>.</li>
<li>(Optional) To scan file uploads and downloads for malware, <a href="/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/">enable anti-virus scanning</a>.</li>
</ol>
<p>Cloudflare will now proxy traffic from enrolled devices, except for the traffic excluded in your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/#3-route-private-network-ips-through-the-cloudflare-one-client">split tunnel settings</a>. For more information on how Gateway forwards traffic, refer to <a href="/cloudflare-one/traffic-policies/proxy/">Gateway proxy</a>.</p>
