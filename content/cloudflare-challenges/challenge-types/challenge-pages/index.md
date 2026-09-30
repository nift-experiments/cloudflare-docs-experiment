<p>An interstitial Challenge Page (a full-page screen that appears before the visitor reaches the destination URL) acts as a gate between the visitor and your website or application while Cloudflare verifies the authenticity of the visitor.</p>
<p>The Challenge Page intercepts the visitor from getting to the destination URL by holding the request and evaluating the browser environment for automated signals, and serving a challenge. The visitor cannot reach their destination without passing the challenge. Based on the signals indicated by their browser environment, the visitor may be asked to perform an interaction such as checking a box or selecting a button for further probing.</p>
<p>You can implement a Challenge Page to your website or application by creating a <a href="/waf/custom-rules/">WAF custom rule</a>.</p>
<p>Challenges are triggered by a rule in the <a href="/waf/">Web Application Firewall (WAF)</a>, <a href="/bots/">Bot Management</a>, or <a href="/waf/rate-limiting-rules/">Rate limiting</a>.</p>
<p>The level of interactivity and visibility of the Challenge Page depends on the Action that you select when creating the WAF rule for your website or application.</p>
<h2 id="actions">Actions</h2>
<p>The following challenge types are the available actions when you create a WAF rule for a Challenge Page.</p>
<h3 id="non-interactive-challenges">Non-Interactive Challenges</h3>
<p>With a Non-Interactive Challenge, Cloudflare makes the determination on whether or not the visitor is automated based on the limited information attained from their browser signals via an injected JavaScript. Then, it presents a Challenge Page that requires no interaction from a visitor except the JavaScript processed by their browser.</p>
<p>The visitor must wait until their browser finishes processing the JavaScript, which typically takes less than five seconds.</p>
<p>If the visitor passes the challenge, the original request continues to the destination URL. If the challenge fails or cannot be completed, the visitor is presented with another interstitial Challenge Page.</p>
<h3 id="managed-challenges">Managed Challenges</h3>
<p>Managed Challenges are where Cloudflare dynamically chooses the appropriate type of challenge served to the visitor based on the characteristics of a request from the signals indicated by their browser. This helps avoid <a href="https://www.cloudflare.com/learning/bots/how-captchas-work/">CAPTCHAs</a>, which also reduces the lifetimes of human time spent solving CAPTCHAs across the Internet.</p>
<p>Most human visitors are automatically verified and the Challenge Page will display <strong>Successful</strong>. However, if Cloudflare detects non-human attributes from the visitor's browser, they may be required to interact with the challenge to solve it.</p>
<p>Cloudflare recommends Managed Challenges for most WAF rules. Unless there are specific compatibility issues, do not use other challenge types.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4048.md")
</aside>
<h3 id="interactive-challenges">Interactive Challenges</h3>
<p>Interactive Challenge Pages require a visitor to interact with the challenge to pass.</p>
<p>Cloudflare always recommends using a Managed Challenge. For more information, refer to the <a href="https://blog.cloudflare.com/end-cloudflare-captcha/">Cloudflare blog post</a>.</p>
<h2 id="compatibility-limitations">Compatibility limitations</h2>
<p>Challenge Pages interrupt the request flow by returning a full HTML page for the user's browser to render and solve. This mechanism fails when the browser expects a non-HTML response, such as an AJAX or XHR (fetch) request.</p>
<p>To ensure your API calls are protected without breaking single-page applications (SPAs) or API integrations, Cloudflare recommends using Turnstile Pre-clearance.</p>
<p>By enabling Pre-clearance, the Turnstile widget issues a persistent clearance cookie (<code>cf_clearance</code>) upon successful human verification on an initial HTML page. This cookie pre-clears the visitor to interact with sensitive API endpoints secured by WAF rules, allowing you to deploy granular security without forcing a disruptive Challenge Page response.</p>
<p>For implementation details, refer to the <a href="/cloudflare-challenges/concepts/clearance/#pre-clearance-support-in-turnstile">guidance on Pre-clearance for Turnstile</a>.</p>
