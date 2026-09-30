<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 13, 2026</time><h2 id="post-title">Origin CA certificate support for Workers VPC</h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p>Workers VPC now supports <a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA certificates</a> when connecting to your private services over HTTPS. Previously, Workers VPC only trusted certificates issued by publicly trusted certificate authorities (for example, Let's Encrypt, DigiCert).</p>
<p>With this change, you can use free Cloudflare Origin CA certificates on your origin servers within private networks and connect to them from Workers VPC using the <code>https</code> scheme. This is useful for encrypting traffic between the tunnel and your service without needing to provision certificates from a public CA.</p>
<p>For more information, refer to <a href="/workers-vpc/configuration/vpc-services/#supported-tls-certificates">Supported TLS certificates</a>.</p>
</div></article></div>
