<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 12, 2025</time><h2 id="post-title">New BOLA Vulnerability Detection for API Shield</h2>
<div class="changelog-badges"><span>api-shield</span></div><div class="changelog-body"><p>Now, API Shield automatically searches for and highlights <strong>Broken Object Level Authorization (BOLA) attacks</strong> on managed API endpoints. API Shield will highlight both BOLA enumeration attacks and BOLA pollution attacks, telling you what was attacked, by who, and for how long.</p>
<p>You can find these attacks three different ways: Security Overview, Endpoint details, or Security Analytics. If these attacks are not found on your managed API endpoints, there will not be an overview card or security analytics suspicious activity card.</p>
<p>On the Security Overview card, select the suggestion &gt; <strong>View details</strong> to review the top attacked API endpoints, endpoint details, and the attack summary:
<img src="/assets/upstream/images/changelog/api-shield/bola-overview-card.png" alt="BOLA attack Overview card" />
<img src="/assets/upstream/images/changelog/api-shield/bola-overview-drawer.png" alt="BOLA attack Overview drawer" /></p>
<p>From the endpoint details, you can select <strong>View attack</strong> to find details about the BOLA attacker’s sessions.</p>
<p><img src="/assets/upstream/images/changelog/api-shield/bola-endpoint-attack.png" alt="BOLA attack endpoint details" /></p>
<p>From here, select <strong>View in Analytics</strong> to observe attacker traffic over time for the last seven days.</p>
<p><img src="/assets/upstream/images/changelog/api-shield/bola-analytics-drawer.png" alt="BOLA attack analytics drawer" /></p>
<p>Your search will filter to traffic on that endpoint in the last seven days, along with the malicious session IDs found in the attack. Session IDs are hashed for privacy and will not be found in your origin logs. Refer to IP and JA4 fingerprint to cross-reference behavior at the origin.</p>
<p>At any time, you can also start your investigation into attack traffic from Security Analytics by selecting the suspicious activity card.</p>
<p><img src="/assets/upstream/images/changelog/api-shield/bola-suspicious-card.png" alt="Suspicious Activity card" /></p>
<p>We urge you to take all of this client information to your developer team to research the attacker behavior and ensure any broken authorization policies in your API are fixed at the source in your application, preventing further abuse.</p>
<p>In addition, this release marks the end of the beta period for these scans. All Enterprise customers with API Shield subscriptions will see these new attacks if found on their zone.</p>
</div></article></div>
