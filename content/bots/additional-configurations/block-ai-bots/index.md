<h2 id="configure-ai-bot-policies">Configure AI bot policies</h2>
<h3 id="new-defaults-on-september-15-2026">New defaults on September 15, 2026</h3>
<p>On September 15, 2026, Cloudflare will set updated defaults for new domains: bots classified as Training or as Agent will be blocked on pages that display ads, and Search will remain allowed. Mixed-purpose crawlers that combine Search and Training will also be blocked by all configurations to block AI training, including the legacy &quot;Block AI bots&quot; option. Before September 15, all customers can <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/settings">opt out of these new defaults</a>.</p>
<p>All Cloudflare customers can choose to block AI bots and agents based on their behavior. Cloudflare offers presets for the most common AI behaviors to give customers the option to treat different AI use cases distinctly:</p>
<ul>
<li><strong>Search</strong>: crawlers that collect or index your content to answer questions about it later.</li>
<li><strong>Agent</strong>: automated activity acting in real time on a person's behalf, such as chat fetch bots and browser-use agents.</li>
<li><strong>Training</strong>: crawlers taking your content to train or fine-tune a model, including mixed-purpose crawlers that are used both for Training and for Search.</li>
</ul>
<p>Each blocking option will block Verified bots classified with that behavior, plus additional unverified bots that fall under these classifications.</p>
<p>Each setting includes three mitigation options:</p>
<ul>
<li><strong>Block (on all pages)</strong> - Issues the block across the entire zone.</li>
<li><strong>Block on pages with ads</strong> - Uses Cloudflare automated detection for pages that display ads on your zone to block only on those pages.</li>
<li><strong>Allow (do not block)</strong> - Does not add any blocking.</li>
</ul>
<p>To configure these policies, customers can go to <strong>Security Settings</strong> &gt; <strong>Configure AI bot policies</strong>.</p>
<h2 id="block-ai-bots-deprecating-on-september-15-2026">Block AI bots [Deprecating on September 15, 2026]</h2>
<p>This setting blocks verified bots that are classified as crawling for the purpose of AI training, as well as a number of unverified bots that behave similarly.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3540.md")
</aside>
<p>To configure this setting and set their preference for blocking mixed-purpose bots, customers can go to <strong>Security Settings</strong> &gt; <strong>Block AI bots</strong>.</p>
