<p>In this learning path, you will learn how to replace your existing VPN provider with Cloudflare's ZTNA solution. Your users will run the Cloudflare One Client on their devices, and you will run either Cloudflare Tunnel or Cloudflare Mesh in your network or on your application servers. After deploying Zero Trust, users will be able to connect to private resources (not exposed to the Internet) via TCP/UDP/ICMP, and administrators will be able to control access to these resources based on user identity, device posture, and other factors.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-10.svg" alt="How Cloudflare connects a user device to a private network application" /></p>
<p>This guide will highlight best practices to follow and other decisions to consider when planning your deployment. Additionally, each module will include links to the key resources and how-to pages needed to get your deployment up and running.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9885.md")
</aside>
<h2 id="objectives">Objectives</h2>
<p>By the end of this module, you will be able to:</p>
<ul>
<li>Understand the high-level architecture and requirements for a ZTNA deployment to replace a legacy VPN.</li>
</ul>
<ul>
<li>Set up a Cloudflare account.</li>
<li>Create a Zero Trust organization to manage your devices and policies.</li>
<li>Configure an identity provider (IdP) for user authentication.</li>
</ul>
