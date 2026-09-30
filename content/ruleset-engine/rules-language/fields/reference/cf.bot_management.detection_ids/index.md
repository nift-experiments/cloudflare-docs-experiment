<h1 id="cf-bot-management-detection-ids">cf.bot_management.detection_ids</h1>

**Data type:** Array<Number>

<p>List of IDs that correlate to the Bot Management heuristic detections made on a request.</p>

<p>Use this field to explicitly match a specific heuristic or to exclude a heuristic in a rule. You can have multiple heuristic detections on the same request.</p>
<p>Requires a Cloudflare Enterprise plan with <a href="/bots/plans/bm-subscription/">Bot Management</a> enabled.</p>

**Example usage:**

```txt
any(cf.bot_management.detection_ids[*] eq 33554817)
```

<h2 id="categories">Categories</h2>

- Request
- Bots

**Keywords:** request, bots, client, visitor

