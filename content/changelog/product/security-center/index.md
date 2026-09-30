---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/security-center/
  description: '2026-06-10'
  full_title: security-center changelog | Cloudflare Docs
  head_html: <title>security-center changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-06-10"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/security-center/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="security-center changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-06-10"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/security-center/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/security-center/#page","headline":"security-center changelog | Cloudflare Docs","description":"2026-06-10","url":"https://developers.cloudflare.com/changelog/product/security-center/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/security-center/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="automated-cease-and-desist-templates-for-brand-protection"><a href="/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/">Automated Cease and Desist templates for Brand Protection</a></h2>
<p><em>2026-06-10</em></p>
<p><strong>TL;DR:</strong> Brand Protection now features an <strong>Automated Cease &amp; Desist (C&amp;D)</strong> workflow. When you discover an infringing domain hosted outside of Cloudflare, you can instantly generate, review, and download a custom-branded, pre-filled legal notice in seconds.</p>
<h4 id="2026-06-08-brand-protection-cease-and-desist-letters-why-this-matters">Why this matters</h4>
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
<h4 id="2026-06-08-brand-protection-cease-and-desist-letters-how-it-works">How it works</h4>
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


<h2 id="create-waf-rules-directly-from-threat-events-saved-views"><a href="/changelog/post/2026-06-08-create-waf-rules-from-threat-events/">Create WAF rules directly from Threat Events saved views</a></h2>
<p><em>2026-06-08</em></p>
<p>Cloudforce One users can now turn <a href="/security-center/cloudforce-one/#analyze-threat-events">Threat Events indicators</a> into active defense. With this update, users can instantly generate a WAF rule that matches the dynamic list of IP addresses returned by any of their <strong>Saved Views</strong>.</p>
<h4 id="2026-06-08-create-waf-rules-from-threat-events-why-this-matters">Why this matters</h4>
<p>Threat intelligence is most effective when it is immediately actionable. Previously, blocking threat actors required manually extracting indicators from threat events and copying them into your firewall rules.
This new integration bridges the gap between threat discovery and threat mitigation:</p>
<ul>
<li>When you identify an active threat pattern - such as an ongoing campaign targeting a specific industry, or using a known indicator type - you can pivot from investigation to mitigation in a single click.</li>
<li>Instead of writing complex, static IP rules, this functionality allows you to leverage the specific filtering logic you have already defined and saved within your Threat Events ecosystem.</li>
<li>Automating the generation of the WAF rule expression from your threat views eliminates manual copying errors, ensuring that the right malicious infrastructure is blocked instantly.</li>
</ul>
<h4 id="2026-06-08-create-waf-rules-from-threat-events-how-to-use-it">How to use it</h4>
<p>You can implement these rules through both the dashboard UI and via the API / Terraform.</p>
<p>Go to <strong>Cloudflare Dashboard</strong> &gt; <strong>Application Security</strong> &gt; <strong>Threat Intelligence</strong> &gt; <strong>Manage Views</strong>, select your desired view, and select <strong>Create WAF Rule</strong>.</p>
<p>This will automatically pre-populate the <a href="/firewall/cf-dashboard/create-edit-delete-rules/">WAF rule builder</a> with the matching threat event IP indicators.</p>
<p>You can also automate this workflow by utilizing the <a href="/firewall/api/cf-firewall-rules/"><strong>WAF Rule Builder API</strong></a> alongside your <a href="/firewall/api/cf-firewall-rules/">Threat Events saved views endpoints</a>.</p>


<h2 id="introducing-threat-actor-profiles-in-threat-events"><a href="/changelog/post/2026-06-08-threat-actor-profiles/">Introducing Threat Actor Profiles in Threat Events</a></h2>
<p><em>2026-06-08</em></p>
<p><strong>TL;DR:</strong> We’ve launched <strong>Threat Actor Profiles</strong> directly inside the Threat Events dashboard. You can now immediately pivot from a generic alert or blocked event to a profile that unmasks the &quot;Who, Why, and How&quot; behind a threat event.</p>
<h4 id="2026-06-08-threat-actor-profiles-why-this-matters">Why this matters</h4>
Security teams often suffer from a visibility gap. When an attack is blocked, it's difficult to know if it was a random automated bot or a sophisticated advanced persistent threat (APT) campaign specifically targeting your industry. Finding out usually means leaving your security dashboard to hunt through external OSINT feeds or static, out-of-date threat reports.
Threat Actor Profiles solve this by sharing Cloudforce One’s deep adversary research directly inside your workflow:
* Cloudflare sees the traffic in real-time across approximately 20% of the web. This means actor profiles display active malicious infrastructure the moment it touches our global edge.
* Every profile provides clear strategic and tactical modules including alternative aliases, origin tracking, historical threat event volume, and MITRE ATT&CK mapping detailing the adversary's technical methods.
* You can search the dedicated threat actor directory or click an actor's name inside any threat event to view all details and related events to the specific threat actor.
<h4 id="2026-06-08-threat-actor-profiles-how-to-use-it">How to use it</h4>
Adversary tracking is now available in the Cloudflare Dashbboard and ready to be included in your daily investigation workflow:
* Click on the **Threat Actor** name in the Threat Events table to open their full identity profile and review their aliases and attack stats.
* Navigate to **Cloudflare Dashboard > Application Security > Threat Intelligence** to explore the new **Threat Actors** tab. Here, you can browse a card-based directory of all established entities tracked by Cloudforce One.
<p>Learn more in the <a href="https://developers.cloudflare.com/security-center/cloudforce-one/#identify-the-adversary">Cloudforce One documentation</a>.</p>


<h2 id="security-scans-more-frequent"><a href="/changelog/post/2026-05-29-security-insights-default-scans/">Security scans more frequent</a></h2>
<p><em>2026-05-29</em></p>
<p>Security Insights scans now run more often. Cloudflare scans Free accounts <strong>every 7 days</strong>, Pro and Business accounts <strong>every 3 days</strong>, and Enterprise accounts <strong>daily</strong>.</p>
<p>In addition, all accounts and zones now receive scans by default. You no longer need to enable scans before Cloudflare checks your account for misconfigurations, vulnerabilities, and other security risks.</p>
<p>Granular on-demand scans are now available on any plan. You can trigger an on-demand scan for any zone, insight, insight type from the Cloudflare dashboard in order to quickly re-check your security posture after remediating an issue.</p>
<p>To learn more, refer to the <a href="/security/security-insights/">Security Insights documentation</a>.</p>


<h2 id="agent-readiness-scores-now-available-in-url-scanner-via-the-cloudflare-dashboard"><a href="/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/">Agent Readiness scores now available in URL Scanner via the Cloudflare Dashboard</a></h2>
<p><em>2026-05-12</em></p>
<p>We’ve added a new <strong>Agent Readiness</strong> tab to URL Scanner reports accessible via the Cloudflare dashboard. This feature evaluates your site against emerging AI standards and provides six specialized scores to help you optimize for the next generation of AI agents and automated discovery.</p>
<p>The Internet is shifting from a human-read web to a machine-read web. AI agents now browse, interact with, and even perform transactions on websites. If a site isn't &quot;agent-ready,&quot; these bots may consume excessive bandwidth, fail to find critical information, or be unable to navigate your services efficiently.</p>
<p>This update provides material value by breaking down readiness into six actionable categories:</p>
<ul>
<li><strong>Basic Web Presence</strong></li>
<li><strong>Discoverability</strong></li>
<li><strong>Content Accessibility</strong></li>
<li><strong>Bot Access Control</strong></li>
<li><strong>Protocol Discovery</strong></li>
<li><strong>Commerce</strong></li>
</ul>
<h4 id="2026-05-12-URL-scanner-report-agent-readiness-accessing-the-report">Accessing the report</h4>
<p>You can view these scores for any scanned URL directly in the dashboard or via our API.</p>
<ul>
<li><strong>Dashboard:</strong> Go to <strong>Protect &amp; Connect &gt; Application Security &gt; Investigate</strong>. After running a scan, select the <strong>Agent Readiness</strong> tab in the report.</li>
<li><strong>API:</strong> Use the <a href="https://developers.cloudflare.com/radar/investigate/url-scanner/">URL Scanner API</a> to programmatically retrieve these scores for your infrastructure.</li>
</ul>
<p>To learn more about the methodology behind these scores, refer to the <a href="https://blog.cloudflare.com/agent-readiness/">blogpost</a>.</p>


<h2 id="csv-export-and-adjustable-page-density-for-rfis"><a href="/changelog/post/2026-05-07-CSV-export-for-RFIs/">CSV export and adjustable page density for RFIs</a></h2>
<p><em>2026-05-07</em></p>
<p>You can now export your Requests for Information (RFI) history to a <strong>CSV document</strong> and customize your dashboard view by choosing how many RFI records to load per page.</p>
<h4 id="2026-05-07-CSV-export-for-RFIs-why-this-matters">Why this matters</h4>
These quality-of-life updates focus on data portability and dashboard performance, allowing power users to manage high volumes of requests more efficiently:
<ul>
<li>The new <strong>CSV export</strong> allows you to move RFI data into external tools for custom reporting, internal auditing, or cross-referencing with other security projects without manual data entry</li>
<li>With <strong>adjustable page density</strong>, you can now choose to load more records at once (10, 25 or 50) to scan through history faster</li>
</ul>
<p>Cloudforce One subscribers can find these new options in <a href="https://dash.cloudflare.com/?to=/:account/application-security/threat-intelligence/requests">Cloudflare Dashboard &gt; Application Security &gt; Threat Intelligence &gt; Requests for Information</a>.</p>


<h2 id="taxii-support-added-to-threat-events-api"><a href="/changelog/post/2026-05-06-TAXII-support-for-threat-events-api/">TAXII support added to Threat Events API</a></h2>
<p><em>2026-05-06</em></p>
<p>The Cloudforce One Threat Events API now supports <a href="https://www.cloudflare.com/en-gb/learning/security/what-is-stix-and-taxii/"><strong>TAXII</strong></a> as an output format, enabling standardized, automated sharing of cyber threat intelligence with your existing security stack.</p>
<h4 id="2026-05-06-TAXII-support-for-threat-events-api-why-this-matters">Why this matters</h4>
<ul>
<li>You can now ingest Cloudforce One threat data directly into your SIEM, TIP or SOAR tools that prefer TAXII-formatted streams without needing custom translation scripts.</li>
<li>By supporting the TAXII format parameter in our API, security teams can automate the synchronization of indicator data, reducing the manual overhead of updating blocklists and detection rules.</li>
<li>This alignment with industry standards ensures that your threat data remains consistent across different security ecosystems and partner integrations.</li>
</ul>
<h4 id="2026-05-06-TAXII-support-for-threat-events-api-how-to-use-it">How to use it</h4>
<p>When calling the Threat Events API, you can now specify <code>taxii</code> in the <code>format</code> query parameter:</p>
<p><code>GET /accounts/{account_id}/cloudforce_one/threat_events?format=taxii</code></p>
<p>You can find the updated documentation in the <a href="https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list#%28resource%29%20cloudforce_one.threat_events%20%3E%20%28method%29%20list%20%3E%20%28params%29%20default%20%3E%20%28param%29%20format%20%3E%20%28schema%29">Cloudflare API Reference</a>.</p>


<h2 id="unified-workspace-for-brand-protection"><a href="/changelog/post/2026-04-27-unified-workspace-brand-protection/">Unified workspace for Brand Protection</a></h2>
<p><em>2026-04-27</em></p>
<p>We have introduced a unified investigation workspace within Brand Protection to help analysts manage complex brand portfolios. Instead of jumping between individual queries, you can now consolidate your workflow into a single, cohesive view.</p>
<h4 id="2026-04-27-unified-workspace-brand-protection-what-s-new">What's new</h4>
<ul>
<li>You can now elect multiple saved queries from your dashboard to generate a consolidated &quot;Combined Matches&quot; view. This allows you to triage results from different brand queries in one unified table</li>
<li>You can open query extended views in distinct tabs within the Brand Protection dashboard. This enables you to maintain multiple investigation contexts simultaneously and switch between them without losing your place.</li>
<li>You can reset your workspace using the new &quot;Clear Selection&quot; action, making it easier to pivot between different investigation sets.</li>
</ul>
<h4 id="2026-04-27-unified-workspace-brand-protection-key-benefits">Key benefits</h4>
<ul>
<li>Eliminate fragmented workflows by viewing all matches across different query buckets in a single table, reducing the need to click through dozens of individual query pages</li>
<li>Correlate related campaigns by seeing similar domains or infrastructure patterns that appear across multiple saved queries</li>
</ul>
<p>Learn more in our <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>


<h2 id="real-time-alerts-and-daily-digests-for-threat-events"><a href="/changelog/post/2026-04-08-threat-events-notification/">Real-time alerts and daily digests for Threat Events</a></h2>
<p><em>2026-04-08</em></p>
<p>You can now automate your threat monitoring by setting up custom alerts in your saved views. Instead of manually checking the dashboard for updates, you can subscribe to notifications that trigger whenever new data matches your specific filter sets, like new activity associated to a particular threat actor or spikes in activity within your industry.</p>
<h4 id="2026-04-08-threat-events-notification-stay-ahead-of-emerging-threats">Stay ahead of emerging threats</h4>
<p>By linking your saved views to the Cloudflare Notifications Center, you can ensure the right information reaches your team at the right time.</p>
<ul>
<li>
<p><strong>Immediate Alerts</strong>: receive real-time notifications the moment a critical event is detected that matches your saved criteria. This is essential for high-priority monitoring, such as tracking active campaigns from specific APT groups.</p>
</li>
<li>
<p><strong>Daily Digests</strong>: opt for a summarized report delivered once a day. This is ideal for maintaining situational awareness of broader trends, like regional activity shifts or industry-wide threat landscapes, without cluttering your inbox.</p>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-center/threat-events-notifications.png" alt="Threat Events notifications" /></p>
<h4 id="2026-04-08-threat-events-notification-how-to-get-started">How to get started</h4>
<p>To set up an alert, go to <strong>Application Security</strong> &gt; <strong>Threat Intelligence</strong> &gt; <strong>Threat Events</strong>. From there:</p>
<ol>
<li>Choose your datasets and apply your desired filters and select <strong>Save View</strong> (or select an existing one).</li>
<li>Open the <strong>Manage Saved Views</strong> menu.</li>
<li>Select <strong>Add Alert</strong> next to your chosen view to configure your notification preferences in the Cloudflare dashboard.</li>
</ol>
<p>For more technical details on configuring notifications, refer to the <a href="/security-center/cloudforce-one/">Threat Events documentation</a>.</p>


<h2 id="real-time-logo-match-preview"><a href="/changelog/post/2026-03-18-brand-protection-logo-match-preview/">Real-time logo match preview</a></h2>
<p><em>2026-03-18</em></p>
<p>We are introducing <strong>Logo Match Preview</strong>, bringing the same pre-save visibility to visual assets that was previously only available for string-based queries. This update allows you to fine-tune your brand detection strategy before committing to a live monitor.</p>
<h4 id="2026-03-18-brand-protection-logo-match-preview-what-s-new">What’s new:</h4>
<ul>
<li>Upload your brand logo and immediately see a sample of potential matches from recently detected sites before finalizing the query</li>
<li>Adjust your similarity score (from 75% to 100%) and watch the results refresh in real-time to find the balance between broad detection and noise reduction</li>
<li>Review the specific logos triggered by your current settings to ensure your query is capturing the right level of brand infringement</li>
</ul>
<p>If you are ready to test your brand assets, go to the <a href="https://developers.cloudflare.com/security-center/brand-protection/">Brand Protection dashboard</a> to try the new preview tool.</p>


<h2 id="dismiss-and-filter-matches-in-brand-protection"><a href="/changelog/post/2026-03-06-brand-protection-dismiss-match/">Dismiss and filter matches in Brand Protection</a></h2>
<p><em>2026-03-06</em></p>
<p>We have introduced new triage controls to help you manage your Brand Protection results more efficiently. You can now clear out the noise by dismissing matches while maintaining full visibility into your historical decisions.</p>
<h4 id="2026-03-06-brand-protection-dismiss-match-what-s-new">What's new</h4>
<ul>
<li><strong>Dismiss matches</strong>: Users can now mark specific results as dismissed if they are determined to be benign or false positives, removing them from the primary triage view.</li>
<li><strong>Show/Hide toggle</strong>: A new visibility control allows you to instantly switch between viewing only active matches and including previously dismissed ones.</li>
<li><strong>Persistent review states</strong>: Dismissed status is saved across sessions, ensuring that your workspace remains organized and focused on new or high-priority threats.</li>
</ul>
<h4 id="2026-03-06-brand-protection-dismiss-match-key-benefits-of-the-dismiss-match-functionality">Key benefits of the dismiss match functionality:</h4>
<ul>
<li>Reduce alert fatigue by hiding known-safe results, allowing your team to focus exclusively on unreviewed or high-risk infringements.</li>
<li>Auditability and recovery through the visibility toggle, ensuring that no match is ever truly &quot;lost&quot; and can be re-evaluated if a site's content changes.</li>
<li>Improved collaboration as your team members can see which matches have already been vetted and dismissed by others.</li>
</ul>
<p>Ready to clean up your match queue? Learn more in our <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>


<h2 id="saved-views-for-threat-events"><a href="/changelog/post/2026-02-23-Saved-views-in-threat-events/">Saved views for Threat Events</a></h2>
<p><em>2026-02-23</em></p>
<p><strong>TL;DR:</strong> You can now create and save custom configurations of the Threat Events dashboard, allowing you to instantly return to specific filtered views — such as industry-specific attacks or regional Sankey flows — without manual reconfiguration.</p>
<h4 id="2026-02-23-Saved-views-in-threat-events-why-this-matters">Why this matters</h4>
<p>Threat intelligence is most effective when it is personalized. Previously, analysts had to manually re-apply complex filters (like combining specific industry datasets with geographic origins) every time they logged in. This update provides material value by:</p>
<ul>
<li>Analysts can now jump straight into &quot;Known Ransomware Infrastructure&quot; or &quot;Retail Sector Targets&quot; views with a single click, eliminating repetitive setup tasks</li>
<li>Teams can ensure everyone is looking at the same data subsets by using standardized saved views, reducing the risk of missing critical patterns due to inconsistent filtering.</li>
</ul>
<p>Cloudforce One subscribers can start saving their custom views now in <a href="https://dash.cloudflare.com/?to=/:account/security-center/threat-intelligence/threat-events">Application Security &gt; Threat Intelligence &gt; Threat Events</a>.</p>


<h2 id="cloudforce-one-threat-events-graphs-are-now-visible-in-the-dashboard"><a href="/changelog/post/2026-02-19-threat-events-graphs/">Cloudforce One Threat events graphs are now visible in the dashboard</a></h2>
<p><em>2026-02-19</em></p>
<p>We have introduced dynamic visualizations to the Threat Events dashboard to help you better understand the threat landscape and identify emerging patterns at a glance.</p>
<p>What's new:</p>
<ul>
<li><strong>Sankey Diagrams</strong>: Trace the flow of attacks from country of origin to target country to identify which regions are being hit hardest and where the threat infrastructure resides.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-center/2026-02-19-sankey-diagram.png" alt="Sankey Diagram" /></p>
<ul>
<li><strong>Dataset Distribution over time</strong>: Instantly pivot your view to understand if a specific campaign is targeting your sector or if it is a broad-spectrum commodity attack.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-center/2026-02-19-events-over-time.png" alt="Events over time" /></p>
<ul>
<li><strong>Enhanced Filtering</strong>: Use these visual tools to filter and drill down into specific attack vectors directly from the charts.</li>
</ul>
<p>Cloudforce One subscribers can explore these new views now in <a href="https://dash.cloudflare.com/?to=/:account/security-center/threat-intelligence/threat-events">Application Security &gt; Threat Intelligence &gt; Threat Events</a>.</p>


<h2 id="enhanced-logo-matching-for-brand-protection"><a href="/changelog/post/2026-02-12-brand-protection-logo-matching-percentage-selector/">Enhanced Logo Matching for Brand Protection</a></h2>
<p><em>2026-02-12</em></p>
<p>We have significantly upgraded our Logo Matching capabilities within Brand Protection. While previously limited to approximately 100% matches, users can now detect a wider range of brand assets through a redesigned matching model and UI.</p>
<h4 id="2026-02-12-brand-protection-logo-matching-percentage-selector-what-s-new">What's new</h4>
<ul>
<li><strong>Configurable match thresholds</strong>: Users can set a minimum match score (starting at 75%) when creating a logo query to capture subtle variations or high-quality impersonations.</li>
<li><strong>Visual match scores</strong>: Allow users to see the exact percentage of the match directly in the results table, highlighted with color-coded lozenges to indicate severity.</li>
<li><strong>Direct logo previews</strong>: Available in the Cloudflare dashboard — similar to string matches — to verify infringements at a glance.</li>
</ul>
<h4 id="2026-02-12-brand-protection-logo-matching-percentage-selector-key-benefits">Key benefits</h4>
<ul>
<li><strong>Expose sophisticated impersonators</strong> who use slightly altered logos to bypass basic detection filters.</li>
<li><strong>Faster triage</strong> of the most relevant threats immediately using visual indicators, reducing the time spent manually reviewing matches.</li>
</ul>
<p>Ready to protect your visual identity? Learn more in our <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>


<h2 id="threat-actor-identification-with-also-known-as-aliases"><a href="/changelog/post/2026-02-03-threat-actor-name-mapping/">Threat actor identification with "also known as" aliases</a></h2>
<p><em>2026-02-03</em></p>
<p>Identifying threat actors can be challenging, because naming conventions often vary across the security industry. To simplify your research, <strong>Cloudflare Threat Events</strong> now include an <strong>Also known as</strong> field, providing a list of common aliases and industry-standard names for the groups we track.</p>
<p>This new field is available in both the Cloudflare dashboard and via the API. In the dashboard, you can view these aliases by expanding the event details side panel (under the <strong>Attacker</strong> field) or by adding it as a column in your configurable table view.</p>
<h4 id="2026-02-03-threat-actor-name-mapping-key-benefits">Key benefits</h4>
<ul>
<li>Easily map Cloudflare-tracked actors to the naming conventions used by other vendors without manual cross-referencing.</li>
<li>Quickly identify if a detected threat actor matches a group your team is already monitoring via other intelligence feeds.</li>
</ul>
<p>For more information on how to access this data, refer to the <a href="https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/">Threat Events API documentation</a>.</p>


<h2 id="url-scanner-now-supports-pdf-report-downloads"><a href="/changelog/post/2026-01-14-Download-URL-Scanner-Report-PDF/">URL Scanner now supports PDF report downloads</a></h2>
<p><em>2026-01-14</em></p>
<p>We have expanded the reporting capabilities of the Cloudflare URL Scanner. In addition to existing JSON and HAR exports, users can now generate and download a <strong>PDF report</strong> directly from the Cloudflare dashboard.
This update streamlines how security analysts can share findings with stakeholders who may not have access to the Cloudflare dashboard or specialized tools to parse JSON and HAR files.</p>
<p><strong>Key Benefits:</strong></p>
<ul>
<li>Consolidate scan results, including screenshots, security signatures, and metadata, into a single, portable document</li>
<li>Easily share professional-grade summaries with non-technical stakeholders or legal teams for faster incident response</li>
</ul>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>PDF Export Button:</strong> A new download option is available in the URL Scanner results page within the Cloudflare dashboard</li>
<li><strong>Unified Documentation:</strong> Access all scan details—from high-level summaries to specific security flags—in one offline-friendly file</li>
</ul>
<p>To get started with the URL Scanner and explore our reporting capabilities, visit the <a href="https://developers.cloudflare.com/api/resources/url_scanner/">URL Scanner API documentation</a>.</p>
<hr />


<h2 id="cloudflare-threat-events-now-support-stix2-format"><a href="/changelog/post/2026-01-12-STIX2-available-for-threat-events-api/">Cloudflare Threat Events now support STIX2 format</a></h2>
<p><em>2026-01-12</em></p>
<p>We are excited to announce that <strong>Cloudflare Threat Events</strong> now supports the <strong>STIX2 (Structured Threat Information Expression)</strong> format. This was a highly requested feature designed to streamline how security teams consume and act upon our threat intelligence.</p>
<p>By adopting this industry-standard format, you can now integrate Cloudflare's threat events data more effectively into your existing security ecosystem.</p>
<h4 id="2026-01-12-STIX2-available-for-threat-events-api-key-benefits">Key benefits</h4>
<ul>
<li>
<p>Eliminate the need for custom parsers, as STIX2 allows for &quot;out of the box&quot; ingestion into major <strong>Threat Intel Platforms (TIPs)</strong>, <strong>SIEMs</strong>, and <strong>SOAR</strong> tools.</p>
</li>
<li>
<p>STIX2 provides a standardized way to represent relationships between indicators, sightings, and threat actors, giving your analysts a clearer picture of the threat landscape.</p>
</li>
</ul>
<p>For technical details on how to query events using this format, please refer to our <a href="https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list/">Threat Events API Documentation</a>.</p>
<hr />


<h2 id="threat-insights-are-now-available-in-the-threat-events-platform"><a href="/changelog/post/2025-11-21-Threat-Events-now-show-events-insights/">Threat insights are now available in the Threat Events platform</a></h2>
<p><em>2025-11-21</em></p>
<p>The threat events platform now has threat insights available for some relevant parent events. Threat intelligence analyst users can access these insights for their threat hunting activity.
Insights are also highlighted in the Cloudflare dashboard by a small <code>lightning icon</code> and the insights can refer to multiple, connected events, potentially part of the same attack or campaign and associated with the same threat actor.</p>
<p>For more information, refer to <a href="/security-center/cloudforce-one/#analyze-threat-events">Analyze threat events</a>.</p>


<h2 id="report-logo-misuse-to-cloudflare-directly-from-the-brand-protection-dashboard"><a href="/changelog/post/2025-10-31-brand-protection-logo-dashboard-report-abuse/">Report logo misuse to Cloudflare directly from the Brand Protection dashboard</a></h2>
<p><em>2025-10-31</em></p>
<p>The Brand Protection logo query dashboard now allows you to use the <strong>Report to Cloudflare</strong> button to submit an Abuse report directly from the Brand Protection logo queries dashboard. While you could previously report new domains that were impersonating your brand before, now you can do the same for websites found to be using your logo without your permission. The abuse reports will be prefilled and you will only need to validate a few fields before you can click the submit button, after which our team process your request.</p>
<p>Ready to start? Check out the <a href="/security-center/brand-protection/">Brand Protection docs</a>.</p>


<h2 id="cloudforce-one-rfi-tokens-are-now-visible-in-the-dashboard"><a href="/changelog/post/2025-10-27-RFI-Tokens-in-Dash/">Cloudforce One RFI tokens are now visible in the dashboard</a></h2>
<p><em>2025-10-27</em></p>
<p>The Requests for Information (RFI) dashboard now shows users the number of tokens used by each submitted RFI to better understand usage of tokens and how they relate to each request submitted.</p>
<p><img src="/assets/upstream/images/changelog/security-center/2025-10-24RFITokens.png" alt="Cloudforce One RFI tokens" /></p>
<p>What’s new:</p>
<ul>
<li>Users can now see the number of tokens used for a submitted request for information.</li>
<li>Users can see the remaining tokens allocated to their account for the quarter.</li>
<li>Users can only select the Routine priority for the <code>Strategic Threat Research</code> request type.</li>
</ul>
<p>Cloudforce One subscribers can try it now in <a href="https://dash.cloudflare.com/?to=/:account/security-center/threat-intelligence/requests">Application Security &gt; Threat Intelligence &gt; Requests for Information</a>.</p>


<h2 id="new-application-security-reports-closed-beta"><a href="/changelog/post/2025-10-17-app-sec-reports/">New Application Security reports (Closed Beta)</a></h2>
<p><em>2025-10-17</em></p>
<p>Cloudflare's new <strong>Application Security report</strong>, currently in Closed Beta, is now available in the dashboard.</p>
<div class="nb-dash-button"></div>
<p>The reports are generated monthly and provide cyber security insights trends for all of the Enterprise zones in your Cloudflare account.</p>
<p>The reports also include an industry benchmark, comparing your cyber security landscape to peers in your industry.</p>
<p><img src="/assets/upstream/images/changelog/security-center/2025-10-17-application-security-report-mock-data.png" alt="Application Security report mock data" /></p>
<p>Learn more about the reports by referring to the <a href="/analytics/account-and-zone-analytics/app-security-reports/">Security Reports documentation</a>.</p>
<p>Use the feedback survey link at the top of the page to help us improve the reports.</p>
<p><img src="/assets/upstream/images/changelog/security-center/2025-10-17-report-feedback-survey.png" alt="Application Security report survey" /></p>


<h2 id="save-time-with-bulk-query-creation-in-brand-protection"><a href="/changelog/post/2025-08-15-brand-protection-bulk-endpoint/">Save time with bulk query creation in Brand Protection</a></h2>
<p><em>2025-08-15</em></p>
<p><a href="/security-center/brand-protection/">Brand Protection</a> detects domains that may be impersonating your brand — from common misspellings (<code>cloudfalre.com</code>) to malicious concatenations (<code>cloudflare-okta.com</code>). Saved search queries run continuously and alert you when suspicious domains appear.</p>
<p>You can now create and save multiple queries in a single step, streamlining setup and management. Available now via the <a href="/api/resources/brand_protection/subresources/queries/methods/bulk/">Brand Protection bulk query creation API</a>.</p>


<h2 id="new-apis-for-brand-protection-setup"><a href="/changelog/post/2025-07-18-brand-protection-api/">New APIs for Brand Protection setup</a></h2>
<p><em>2025-07-18</em></p>
<hr />
<h4 id="2025-07-18-brand-protection-api-title-new-apis-for-brand-protection-setup-description-you-can-now-use-the-brand-protection-api-endpoints-to-manage-your-brand-protection-queries-date-2025-07-18">title: New APIs for Brand Protection setup
description: You can now use the Brand Protection API endpoints to manage your Brand Protection queries
date: 2025-07-18</h4>
<p>The Brand Protection API is now available, allowing users to create new queries and delete existing ones, fetch matches and more!</p>
<p>What you can do:</p>
<ul>
<li><strong>create new string or logo query</strong></li>
<li><strong>delete string or logo queries</strong></li>
<li><strong>download matches for both logo and string queries</strong></li>
<li><strong>read matches for both logo and string queries</strong></li>
</ul>
<p>Ready to start? Check out the <a href="/api/resources/brand_protection/">Brand Protection API</a> in our documentation.</p>


<h2 id="url-scanner-now-supports-geo-specific-scanning"><a href="/changelog/post/2025-05-07-url-scanner-geoegress/">URL Scanner now supports geo-specific scanning</a></h2>
<p><em>2025-05-08</em></p>
<p>Enterprise customers can now choose the geographic location from which a URL scan is performed — either via <a href="/security-center/investigate/">Security Center</a> in the Cloudflare dashboard or via the <a href="/api/resources/url_scanner/subresources/scans/methods/create/">URL Scanner API</a>.</p>
<p>This feature gives security teams greater insight into how a website behaves across different regions, helping uncover targeted, location-specific threats.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li>Location Picker: Select a location for the scan via <strong>Security Center → Investigate</strong> in the dashboard or through the API.</li>
<li>Region-aware scanning: Understand how content changes by location — useful for detecting regionally tailored attacks.</li>
<li>Default behavior: If no location is set, scans default to the user’s current geographic region.</li>
</ul>
<p>Learn more in the <a href="/security-center/">Security Center documentation</a>.</p>



