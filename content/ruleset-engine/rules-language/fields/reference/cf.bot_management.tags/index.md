<h1 id="cf-bot-management-tags">cf.bot_management.tags</h1>

**Data type:** Array<String>

<p>Provides the tags associated with bot traffic.</p>

<p>Use this field to match requests associated with a specific bot tag.</p>
<p>Requires a Cloudflare Enterprise plan with <a href="/bots/plans/bm-subscription/">Bot Management</a> enabled.</p>

**Example usage:**

```txt
any(cf.bot_management.tags[*] eq "API")
```

<h2 id="categories">Categories</h2>

- Request
- Bots

**Keywords:** request, bots, client, visitor, tags

