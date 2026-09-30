<p>AI Security for Apps can detect when an LLM prompt touches on unsafe or unwanted subjects. There are two layers of topic detection:</p>
<ul>
<li><a href="#default-unsafe-topics">Default unsafe topics</a>: A built-in set of safety categories that detect harmful content such as violent crimes, hate speech, and sexual content.</li>
<li><a href="#custom-topics">Custom topics</a>: Topics you define to match your organization's specific policies, such as &quot;competitors&quot; or &quot;financial-advice&quot;.</li>
</ul>
<h2 id="default-unsafe-topics">Default unsafe topics</h2>
<p>When AI Security for Apps is enabled, it automatically evaluates prompts against a set of default unsafe topic categories and populates two fields:</p>
<ul>
<li><strong>LLM Unsafe topic detected</strong> (<a href="/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_detected/"><code>cf.llm.prompt.unsafe_topic_detected</code></a>): <code>true</code> if any unsafe topic was found.</li>
<li><strong>LLM Unsafe topic categories</strong> (<a href="/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/"><code>cf.llm.prompt.unsafe_topic_categories</code></a>): An array of the specific categories detected.</li>
</ul>
<details class="nb-details"><summary>Default unsafe topic categories</summary><div class="nb-details-body">
@input("content/.markup/bodies/15552.md")
</div></details>
<hr />
<h2 id="custom-topics">Custom topics</h2>
<p>Custom topic detection lets you define your own topics and AI Security for Apps will score each prompt against them. You can then use these scores in <a href="/waf/custom-rules/">custom rules</a> or <a href="/waf/rate-limiting-rules/">rate limiting rules</a> to block, challenge, or log requests based on a relevance score that you define.</p>
<p>This capability uses a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15553.md")
</div> that evaluates prompts at runtime. No model training is required.
<h3 id="how-custom-topics-work">How custom topics work</h3>
<ol>
<li>You define a list of up to 20 custom topics. Each topic consists of:
<ul>
<li><strong>Label</strong>: A short, hyphenated identifier used in rule expressions and analytics (for example, <code>financial-advice</code>).</li>
<li><strong>Topic description</strong>: The descriptive text the model uses to classify prompts (for example, <code>seeking financial advice</code>).</li>
</ul>
</li>
<li>When a request arrives at a <code>cf-llm</code> labeled endpoint, the model evaluates the prompt against all defined topic descriptions and returns a relevance score for each.</li>
<li>Scores are written to the <a href="/waf/detections/ai-security-for-apps/fields/"><code>cf.llm.prompt.custom_topic_categories</code></a> map field, keyed by label. You use labels (not topic descriptions) in rule expressions and analytics.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="inverted-relevance-scale">Inverted relevance scale</h3>
@markup("md", "content/.markup/bodies/15551.md")
</aside>
<h3 id="define-custom-topics">Define custom topics</h3>
<p>You can manage custom topics from two places in the dashboard:</p>
<ol>
<li><strong>Security Settings page</strong>: Go to <strong>Security</strong> &gt; <strong>Settings</strong> and search for the <strong>AI Security for Apps</strong> section. Under <strong>Custom Topics</strong>, select <strong>Manage topics</strong> to add, edit, or remove topics.</li>
<li><strong>Expression builder sidebar</strong>: When creating or editing a <a href="/waf/custom-rules/create-dashboard/">custom rule</a>, select the <strong>LLM Custom topic</strong> field. Then, select <strong>Manage custom topics</strong> to open a sidebar where you can manage topics without leaving the rule creation page.</li>
</ol>
<p>Both methods will update the same underlying topic list. Changes made in one are immediately reflected in the other.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15557.md")
</div></div>
<h3 id="constraints">Constraints</h3>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum number of topics</td>
<td>20</td>
</tr>
<tr>
<td>Topic string length</td>
<td>2–50 printable ASCII characters</td>
</tr>
<tr>
<td>Label length</td>
<td>2–20 characters</td>
</tr>
<tr>
<td>Label format</td>
<td>Lowercase letters, numbers, and hyphens (<code>-</code>) only</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15549.md")
</aside>
<h2 id="best-practices-for-defining-custom-topics">Best practices for defining custom topics</h2>
<p>The quality of custom topic detection depends on how you write your topic descriptions. The underlying model is a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15558.md")
</div> that compares the semantic meaning of the prompt against your topic description.
<p>The most important thing to do is to describe the user's intent, not just the subject.</p>
<h3 id="lead-with-intent">Lead with intent</h3>
<p>The model performs semantic classification, not keyword matching. Topic descriptions that capture what the user is <em>trying to do</em> are significantly more accurate than descriptions that simply name a subject area. A short verb phrase (3–6 words) is usually the best trade-off between precision and coverage.</p>
<p>Compare how the same two topic descriptions perform against two prompts that both mention finance but with very different intent:</p>
<table>
<thead>
<tr>
<th>Topic description</th>
<th>Prompt: <em>&quot;Should I invest my savings in index funds?&quot;</em></th>
<th>Prompt: <em>&quot;Our finance team just finished the Q3 report.&quot;</em></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>financial advice</code> (noun only)</td>
<td>Matches</td>
<td>Also matches. The word &quot;finance&quot; appears, even though no advice is being sought</td>
</tr>
<tr>
<td><code>seeking financial advice</code> (intent phrase)</td>
<td>Matches</td>
<td>Correctly ignored. Mentions finance but has no advice-seeking intent</td>
</tr>
</tbody>
</table>
<h4 id="example-competitors">Example: <code>competitors</code></h4>
<table>
<thead>
<tr>
<th>Quality</th>
<th>Topic description</th>
<th>Why</th>
</tr>
</thead>
<tbody>
<tr>
<td>Best</td>
<td><code>seeking info on competitors</code></td>
<td>Captures intent. Only fires when users are actively asking about competitors</td>
</tr>
<tr>
<td>Okay</td>
<td><code>Acme Corp, Banana Co, Candy &amp; Sons</code></td>
<td>Works for known names but misses unnamed competitors and catches casual mentions</td>
</tr>
<tr>
<td>Avoid</td>
<td><code>other companies</code></td>
<td>Far too vague. Matches nearly any prompt that mentions a business</td>
</tr>
</tbody>
</table>
<h4 id="example-financial-advice">Example: <code>financial-advice</code></h4>
<table>
<thead>
<tr>
<th>Quality</th>
<th>Topic description</th>
<th>Why</th>
</tr>
</thead>
<tbody>
<tr>
<td>Best</td>
<td><code>seeking financial advice</code></td>
<td>Intent-driven. Matches users asking for guidance, ignores passive mentions of finance</td>
</tr>
<tr>
<td>Okay</td>
<td><code>securities and investments</code></td>
<td>Reasonable subject scope but fires on news articles and factual mentions, not just advice-seeking</td>
</tr>
<tr>
<td>Avoid</td>
<td><code>finance</code></td>
<td>Extremely broad. Matches almost everything from expense reports to pricing questions</td>
</tr>
</tbody>
</table>
<h3 id="more-best-practices">More best practices</h3>
<ul>
<li><strong>Be specific.</strong> Overly broad topics cause false positives; overly narrow topics cause false negatives.</li>
<li><strong>Avoid semantic overlap.</strong> If two topics mean nearly the same thing (for example, <code>seeking financial advice</code> and <code>asking for investment guidance</code>), they will score similarly on the same prompts and waste your 20-topic budget.</li>
<li><strong>Test and iterate.</strong> Send test prompts and review scores in <a href="/waf/analytics/security-analytics/">Security Analytics</a>. You can tune by adjusting the topic description (more or less specific) or the score threshold in your rule (<code>lt 20</code> is strict, <code>lt 50</code> is permissive).</li>
<li><strong>Do not list multiple values in one topic description.</strong> The model only evaluates against the first item in a comma-separated list. For example, <code>Toyota, Ford, Audi, BMW</code> will only match prompts about <code>Toyota</code> — the remaining items are ignored. Removing the commas does not improve results. Use a single intent-driven phrase such as <code>seeking info on competitors</code>, or create separate topics for each value.</li>
</ul>
<h3 id="example-custom-topics">Example custom topics</h3>
<table>
<thead>
<tr>
<th>Label</th>
<th>Topic description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>competitors</code></td>
<td><code>seeking info on competitors</code></td>
</tr>
<tr>
<td><code>financial-advice</code></td>
<td><code>seeking financial advice</code></td>
</tr>
<tr>
<td><code>legal-advice</code></td>
<td><code>asking for legal or regulatory advice</code></td>
</tr>
<tr>
<td><code>sensitive-data</code></td>
<td><code>requesting passwords or API keys</code></td>
</tr>
<tr>
<td><code>job-seeking</code></td>
<td><code>asking about job openings or careers</code></td>
</tr>
<tr>
<td><code>bias</code></td>
<td><code>comparing demographic groups as better or worse</code></td>
</tr>
</tbody>
</table>
