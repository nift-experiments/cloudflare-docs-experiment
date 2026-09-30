<p>Hyperdrive uses the <a href="https://www.cloudflare.com/ips/">Cloudflare IP address ranges</a> to connect to your database. If you decide to restrict the IP addresses that can access your database with firewall rules, the IP address ranges listed in this reference need to be allow-listed in your database's firewall and networking configurations.</p>
<p>You can connect to your database from Hyperdrive using any of the 3 following networking configurations:</p>
<ol>
<li>Configure your database to allow inbound connectivity from the public Internet (all IP address ranges).</li>
<li>Configure your database to allow inbound connectivity from the public Internet, with only the IP address ranges used by Hyperdrive allow-listed in an IP access control list (ACL).</li>
<li>Configure your database to allow inbound connectivity from a private network, and run a Cloudflare Tunnel instance in your private network to enable Hyperdrive to connect from the Cloudflare network to your private network. Refer to <a href="/hyperdrive/configuration/connect-to-private-database/">documentation on connecting to a private database using Tunnel</a>.</li>
</ol>
