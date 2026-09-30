<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 10, 2026</time><h2 id="post-title">Automated Cease and Desist templates for Brand Protection</h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p><strong>TL;DR:</strong> Brand Protection now features an <strong>Automated Cease &amp; Desist (C&amp;D)</strong> workflow. When you discover an infringing domain hosted outside of Cloudflare, you can instantly generate, review, and download a custom-branded, pre-filled legal notice in seconds.</p>
<h4 id="why-this-matters">Why this matters</h4>
This update introduces a major shift from pure detection to actionable enforcement, eliminating the manual burden for your Trust & Safety and Legal teams:
<ul>
<li><strong>Instant WHOIS and Recipient Lookup:</strong> We automatically scrape registrar data and WHOIS contact information (such as the registrant or registrar abuse email) behind the scenes, highlighting exactly where your notice needs to be sent</li>
<li><strong>Smart Template Automation:</strong> We pre-fill your custom-branded templates with essential metadata, including the infringing domain, registrar name, and discovery date.</li>
<li><strong>Tailored Enforcement Tones:</strong> Choose from three default layout strategies depending on the severity of the infrastructure match:
<ul>
<li><em>Exact Match:</em> A formal demand for identical trademark infringements</li>
<li><em>Similar Match:</em> A standard notice optimized for typosquatting (one-character distance matches)</li>
<li><em>Friendly Tone:</em> An amicable initial outreach for potential unintentional or accidental infringements</li>
</ul>
</li>
<li><strong>Full Editing Control:</strong> Before creating the final PDF, a real-time review screen allows you to fine-tune the messaging, modify placeholders, and ensure your text aligns perfectly with internal legal standards</li>
</ul>
<h4 id="how-it-works">How it works</h4>
When reviewing a malicious domain match inside your dashboard, your enforcement path splits depending on where the attacker is located:
<ol>
<li><strong>On the Cloudflare Network:</strong> If the domain uses Cloudflare’s network or registrar, trigger our existing integrated abuse reporting flow with one click.</li>
<li><strong>Hosted Elsewhere:</strong> If the domain is hosted on an external provider, click the <strong>Generate C&amp;D Letter</strong> option to launch the new document builder, pick your template, verify the auto-populated recipient data, and download your finalized PDF.</li>
</ol>
<p>You can manage your templates and enforce matches by going to the <strong>Cloudflare Dashboard &gt; Application Security &gt; Brand Protection</strong> and selecting your detected Brand Protection matches.
For more information, read the <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>
<blockquote>
<p><strong>Note:</strong> Cloudflare does not represent you and cannot provide you with legal advice. Only you can decide whether your rights have been infringed, whether a cease and desist letter is appropriate, and what that letter should say.</p>
</blockquote>
</div></article></div>
