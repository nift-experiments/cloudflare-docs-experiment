<h1 id="cf-llm-prompt-token-count">cf.llm.prompt.token_count</h1>

**Data type:** Number

<p>An estimated token count for the LLM prompt in the request.</p>

<p>The count is calculated using a general-purpose tokenizer and may not exactly match the count reported by your LLM provider.</p>
<p>Requires a Cloudflare Enterprise plan. You must also enable <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a>.</p>

**Example usage:**

```txt
# Matches requests where the estimated token count exceeds 4,000:
(cf.llm.prompt.token_count gt 4000)
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, ai, client, visitor

