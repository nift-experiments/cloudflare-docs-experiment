<h1 id="cf-waf-score">cf.waf.score</h1>

**Data type:** Number

<p>A global score from 1–99 that combines the score of each WAF attack vector into a single score.</p>

<p>The special score <code>100</code> indicates that Cloudflare did not score the request.</p>
<p>This is the standard <a href="/waf/detections/attack-score/">WAF attack score</a> to detect variants of attack patterns.</p>
<p>Requires a Cloudflare Enterprise plan. You must also enable <a href="/waf/detections/attack-score/">attack score detection</a>.</p>

<h2 id="categories">Categories</h2>

- Request

**Keywords:** request, cloudflare, attack score, waf score, client, visitor

