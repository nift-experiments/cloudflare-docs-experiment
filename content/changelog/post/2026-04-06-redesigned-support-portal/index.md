<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 7, 2026</time><h2 id="post-title">Redesigned Support Portal for faster, personalized help</h2>
<div class="changelog-badges"><span>support</span></div><div class="changelog-body"><h4 id="redesigned-get-help-portal-for-faster-personalized-help">Redesigned &quot;Get Help&quot; Portal for faster, personalized help</h4>
<p>Cloudflare has officially launched a redesigned &quot;Get Help&quot; Support Portal to eliminate friction and get you to a resolution faster. Previously, navigating support meant clicking through multiple tiles, categorizing your own technical issues across 50+ conditional fields, and translating your problem into Cloudflare's internal taxonomy.</p>
<p>The new experience replaces that complexity with a personalized front door built around your specific account plan. Whether you are under a DDoS attack or have a simple billing question, the portal now presents a single, clean page that surfaces the direct paths available to you — such as &quot;Ask AI&quot;, &quot;Chat with a human&quot;, or &quot;Community&quot; — without the manual triage.</p>
<h4 id="what-s-new">What's New</h4>
<ul>
<li><strong>One Page, Clear Choices</strong>: No more navigating a grid of overlapping categories. The portal now uses action cards tailored to your plan (Free, Pro, Business, or Enterprise), ensuring you only see the support channels you can actually use.</li>
<li><strong>A Radically Simpler Support Form</strong>: We've reduced the ticket submission process from four+ screens and 50+ fields to a single screen with five critical inputs. You describe the issue in your own words, and our backend handles the categorization.</li>
<li><strong>AI-Driven Triage</strong>: Using <a href="https://developers.cloudflare.com/workers-ai/">Cloudflare Workers AI</a> and <a href="https://developers.cloudflare.com/vectorize/">Vectorize</a>, the portal now automatically generates case subjects and predicts product categories.</li>
</ul>
<h4 id="moving-complexity-to-the-backend">Moving complexity to the backend</h4>
<p>Behind the scenes, we've moved the complexity from the user to our own developer stack. When you describe an issue, we use semantic embeddings to capture intent rather than just keywords.</p>
<p>By leveraging case-based reasoning, our system compares your request against millions of resolved cases to route your inquiry to the specialist best equipped to help. This ensures that while the front-end experience is simpler for you, the back-end routing is more accurate than ever.</p>
<p>To learn more, refer to the <a href="/support/contacting-cloudflare-support/">Support documentation</a> or select <strong>Get Help</strong> directly in the <a href="https://dash.cloudflare.com/">Cloudflare Dashboard</a>.</p>
</div></article></div>
