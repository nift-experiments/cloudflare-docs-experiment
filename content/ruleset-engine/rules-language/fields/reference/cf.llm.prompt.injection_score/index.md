<h1 id="cf-llm-prompt-injection-score">cf.llm.prompt.injection_score</h1>

**Data type:** Number

<p>A score from 1–99 that represents the likelihood that the LLM prompt in the request is trying to perform a prompt injection attack.</p>

<p>A low score (for example, below <code>20</code>) indicates that there is a high probability that the LLM prompt in the request is trying to perform a prompt injection attack.</p>
<p>The special score <code>100</code> indicates that Cloudflare did not score the request.</p>
<p>Requires a Cloudflare Enterprise plan. You must also enable <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a>.</p>

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, ai, client, visitor

