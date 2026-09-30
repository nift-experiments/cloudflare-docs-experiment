<h1 id="cf-bot-management-corporate-proxy">cf.bot_management.corporate_proxy</h1>

**Data type:** Boolean

<p>Indicates whether the incoming request comes from an identified Enterprise-only cloud-based corporate proxy or secure web gateway.</p>

<p>Requires a Cloudflare Enterprise plan with <a href="/bots/plans/bm-subscription/">Bot Management</a> enabled.</p>

**Example usage:**

```txt
not cf.bot_management.verified_bot
and not cf.bot_management.static_resource
and not cf.bot_management.corporate_proxy
and cf.bot_management.score lt 30
```

<h2 id="categories">Categories</h2>

- Request
- Bots

**Keywords:** request, bots, proxy, client, visitor

