<h1 id="cf-llm-prompt-unsafe-topic-detected">cf.llm.prompt.unsafe_topic_detected</h1>

**Data type:** Boolean

<p>Indicates whether the incoming request includes any unsafe topic category in the LLM prompt.</p>

<p>Equivalent to checking if the <a href="/ruleset-engine/rules-language/fields/reference/cf.llm.prompt.unsafe_topic_categories/"><code>cf.llm.prompt.unsafe_topic_categories</code></a> field is not empty.</p>
<p>Requires a Cloudflare Enterprise plan. You must also enable <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a>.</p>

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, ai, client, visitor

