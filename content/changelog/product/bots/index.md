<h1 id="changelog">Changelog</h1>

<h2 id="precursor-introduces-session-based-bot-detection"><a href="/changelog/post/2026-07-13-precursor-session-based-detection/">Precursor introduces session-based bot detection</a></h2>
<p><em>2026-07-13</em></p>
<p>Precursor is rolling out to all customers starting today. Precursor is client-side JavaScript that enables session-based bot detection.</p>
<p>You can <a href="https://blog.cloudflare.com/introducing-precursor">read the announcement blog</a> for background on why we built Precursor and how session-level behavioral detection works.</p>
<p>With Precursor enabled, Cloudflare can:</p>
<ul>
<li>Continuously evaluate behavioral signals across a session</li>
<li>Re-validate challenge clearance as behavior changes</li>
<li>Update bot scores with session context</li>
<li>Provide client-side visibility where none previously existed</li>
</ul>
<p>It integrates with existing protections, including Security Rules, and can be enabled directly from the Cloudflare dashboard with configurable modes to balance security and user experience.</p>
<img src="/images/precursor/enabling_precursor.gif" alt="Animated walkthrough of enabling Precursor in the Cloudflare dashboard" style="border:1px solid #e5e7eb;border-radius:6px;display:block;margin:16px 0;" />
<p>To learn more, refer to the <a href="/cloudflare-challenges/precursor/">Precursor documentation</a>.</p>


<h2 id="new-options-to-manage-ai-traffic"><a href="/changelog/post/2026-07-01-ai-traffic-options/">New options to manage AI traffic</a></h2>
<p><em>2026-07-01</em></p>
<p>Not all AI traffic is the same. Now, all customers — including those on the Free plan — can manage AI crawlers based on what they actually do on your site. Cloudflare groups AI traffic into three behaviors you can control independently: <a href="/bots/concepts/bot/#ai-bots">Search, Agent, and Training</a>. This lets you keep the automated traffic that sends readers and revenue back to you, while blocking the traffic that only takes from your content.</p>
<p>Each behavior maps to a real use case. <strong>Search</strong> covers crawlers that index your content so they can answer questions about it later, where you should expect referral traffic or other equitable compensation in return. <strong>Agent</strong> covers automated activity acting in real time on a person's behalf, such as chat fetch bots and browser-use agents. <strong>Training</strong> covers crawlers that take your content to train or fine-tune a model. For each preset you can choose to block on all pages, block only on pages that display ads, or choose not to block.</p>
<p><img src="/assets/upstream/images/changelog/bots/ai-bot-traffic-policies.png" alt="The Configure AI bot traffic policies screen, where Search, Agent, and Training can each be set to allow, block, or block only on pages with ads" /></p>
<p>Starting <strong>September 15, 2026</strong>, new domains onboarding to Cloudflare receive updated defaults: Bots classified as Training or as Agent are blocked on pages that display ads, while <strong>Search</strong> remains allowed. On that date, multi-purpose crawlers that combine Search and Training will be affected by the new defaults to block Training. All customers can <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/settings">opt out of the new defaults</a> at any time before September 15.</p>


<h2 id="more-visibility-into-bot-traffic-with-botbase-and-business-insights"><a href="/changelog/post/2026-07-01-botbase-attribution-business-insights/">More visibility into bot traffic with BotBase and Business Insights</a></h2>
<p><em>2026-07-01</em></p>
<p>With Content Independence Day 2026, <a href="/bots/get-started/bot-management/">Enterprise Bot Management</a> customers get two new tools that make bot traffic far easier to see and reason about: <a href="/bots/botbase/">BotBase</a>, a searchable directory of every bot Cloudflare tracks, and <a href="/bots/business-insights/">Business Insights</a>, a dashboard that shows how much value each crawler sends back to your business.</p>
<p>BotBase is Cloudflare's directory of all known bots and agents, available directly in the dashboard. It shows how Cloudflare classifies each bot by behavior — Search, Agent, Training, and other categories such as Transact, Data Collection, SEO, and Ads Verification — so you can understand why a given crawler is visiting you. You can search and filter the full catalogue, filter your own traffic down to a single bot to investigate its activity on your zone, and copy any bot's detection ID to target it precisely in <a href="/security/rules/">Security rules</a>. Every tracked bot in BotBase is also published in <a href="https://radar.cloudflare.com/bots/directory">Cloudflare Radar's bots and agents directory</a>.</p>
<p>Business Insights is built for content owners and business decision-makers who want to know which bots help or harm their business, without reading rule syntax. The dashboard reports crawl-to-referral ratios both site-wide and per bot operator — comparing how often a company crawls your content against how many visitors it actually refers back — over the last 24 hours, 7 days, or 30 days. Each operator is labeled with Cloudflare's <a href="/bots/concepts/bot/verified-bots/">updated classification</a> and an action status of Allowed, Blocked, or Partially blocked, giving stakeholders a shared, at-a-glance view of the AI traffic reaching your site.</p>
<p><img src="/assets/upstream/images/changelog/bots/attribution-business-insights.png" alt="The Business Insights dashboard, showing bot traffic, content page requests, crawl-to-referral ratio, and a per-operator bot activity table" /></p>



