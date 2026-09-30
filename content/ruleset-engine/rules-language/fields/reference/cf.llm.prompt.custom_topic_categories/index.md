<h1 id="cf-llm-prompt-custom-topic-categories">cf.llm.prompt.custom_topic_categories</h1>

**Data type:** Map<Number>

<p>A map of custom topic labels to relevance scores (1–99) for the LLM prompt in the request.</p>

<p>Lower scores indicate the prompt is more relevant to that topic. Only populated when <a href="/waf/detections/ai-security-for-apps/unsafe-topics/#custom-topics">custom topics</a> are configured.</p>
<p>Requires a Cloudflare Enterprise plan. You must also enable <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a>.</p>

**Example usage:**

```txt
# Matches requests where the prompt is highly relevant to the "competitors" custom topic:
(cf.llm.prompt.custom_topic_categories["competitors"] lt 30)
```

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, ai, client, visitor

