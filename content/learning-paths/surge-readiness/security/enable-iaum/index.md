<h2 id="enable-i-m-under-attack-mode-iaum">Enable &quot;I'm Under Attack&quot; mode (IAUM)</h2>
<p>If you are under attack and have this feature enabled during the attack, visitors will receive an interstitial page for about five seconds while the traffic is analyzed to make sure it is a legitimate human visitor. The vast majority of Layer 7 attack scripts are defeated by IUAM and can be honed via Page Rules.</p>
<p>Refer to <a href="https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/">I'm Under Attack Mode</a> for more information.</p>
<h2 id="change-access-control-list-acl">Change Access Control List (ACL)</h2>
<p>An ACL refers to rules that are applied to port numbers or IP addresses that are available on a host permitting use of the service. When you only allow Cloudflare IPs, you eliminate threats attempting to attack your origin IP range.</p>
<p>Refer to <a href="https://www.cloudflare.com/ips">Cloudflare IP Ranges</a> for more information.</p>
<h2 id="change-origin-ips-and-update-cloudflare-dns-records">Change Origin IPs and update Cloudflare DNS records</h2>
<p>If your origin is still being attacked, consider moving your Origin IPs and updating your Cloudflare DNS records.</p>
<p>Refer to <a href="/learning-paths/prevent-ddos-attacks/concepts/">Prevent DDoS attacks</a> for detailed guidance.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10274.md")
</aside>
