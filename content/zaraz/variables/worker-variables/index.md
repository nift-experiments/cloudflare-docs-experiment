---
cp9:
  canonical: https://developers.cloudflare.com/zaraz/variables/worker-variables/
  description: Create server-side variables using Workers for use in Zaraz actions.
  full_title: Worker Variables · Cloudflare Zaraz docs
  head_html: <title>Worker Variables · Cloudflare Zaraz docs</title><meta name="generator" content="Nift"><meta name="description" content="Create server-side variables using Workers for use in Zaraz actions."><link rel="canonical" href="https://developers.cloudflare.com/zaraz/variables/worker-variables/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/zaraz/variables/worker-variables/index.md"><meta property="og:title" content="Worker Variables · Cloudflare Zaraz docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create server-side variables using Workers for use in Zaraz actions."><meta property="og:url" content="https://developers.cloudflare.com/zaraz/variables/worker-variables/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Zaraz"><meta name="algolia_product_filter" content="Zaraz"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/zaraz/variables/worker-variables/#page","headline":"Worker Variables \u00b7 Cloudflare Zaraz docs","description":"Create server-side variables using Workers for use in Zaraz actions.","url":"https://developers.cloudflare.com/zaraz/variables/worker-variables/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /zaraz/variables/worker-variables/
  schema: 1
---
<p>Zaraz Worker Variables are a powerful type of variable that you can configure and then use in your actions and triggers. Unlike string and masked variables, Worker Variables are dynamic. This means you can use a Cloudflare Worker to determine the value of the variable, allowing you to use them for countless purposes. For example:</p>
<ol>
<li>A Worker Variable that calculates the sum of all products in the cart</li>
<li>A Worker Variable that takes a cookie, makes a request to your backend, and returns the User ID</li>
<li>A Worker Variable that hashes a value before sending it to a third-party vendor</li>
</ol>
<h2 id="creating-a-worker">Creating a Worker</h2>
<p>To use a Worker Variable, you first need to create a new Cloudflare Worker. You can do this through the Cloudflare dashboard or by using <a href="/workers/get-started/guide/">Wrangler</a>.</p>
<p>To create a new Worker in the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers and Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select **Create application**.
3. Give a name to your Worker and select **Deploy**.
4. Select **Edit code**.
<p>You have now created a basic Worker that responds with &quot;Hello world.&quot; If you use this Worker as a Variable, your Variable will always output &quot;Hello world.&quot; The response body coming from your Worker will be the value of your Worker Variable. To make this Worker useful, you will usually want to use information coming from Zaraz, which is known as the Zaraz Context.</p>
<p>Zaraz forwards the Zaraz Context object to your Worker as a JSON payload with a POST request. You can access any property like this:</p>
<pre tabindex="0"><code class="language-js">const { system, client } = await request.json()&#10;&#10;/* System parameters */&#10;system.page.url.href // URL of the current page&#10;system.page.query.gclid // Value of the gclid query parameter&#10;system.device.resolution // Device screen resolution&#10;system.device.language // Browser preferred language&#10;&#10;/* Zaraz Track values */&#10;client.value // value from `zaraz.track(&quot;foo&quot;, {value: &quot;bar&quot;})`&#10;client.products[0].name // name of the first product in an ecommerce call&#10;</code></pre>
<p>Keep reading for more complete examples of different use cases or refer to <a href="/zaraz/reference/context/">Zaraz Context</a>.</p>
<h2 id="configuring-a-worker-variable">Configuring a Worker Variable</h2>
<p>Once your Worker is published, configuring a Worker Variable is easy.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tag setup</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select the domain for which you want to configure variables.
3. Select the **Variables** tab.
4. Select **Create variable**.
5. Give your variable a name, choose **Worker** as the Variable type, and select your newly created Worker.
6. Save your variable.
<h2 id="using-your-worker-variable">Using your Worker Variable</h2>
<p>Now that your Worker Variable is configured, you can use it in your actions and triggers.</p>
<p>To use your Worker Variable:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tag setup</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select the domain for which you want to configure variables.
3. Select **Edit** next to a tool that you have already configured.
4. Select an action or add a new one.
5. Select the plus sign at the right of the text fields.
6. Select your Worker Variable from the list.
<h2 id="example-worker-variables">Example Worker Variables</h2>
<h3 id="calculates-the-sum-of-all-products-in-the-cart">Calculates the sum of all products in the cart</h3>
<p>Assuming we are sending a list of products in a cart, like this:</p>
<pre tabindex="0"><code class="language-js">zaraz.ecommerce(&quot;Cart Viewed&quot;, {&#10;  products: [&#10;    { name: &quot;shirt&quot;, price: &quot;50&quot; },&#10;    { name: &quot;jacket&quot;, price: &quot;20&quot; },&#10;    { name: &quot;hat&quot;, price: &quot;30&quot; },&#10;  ],&#10;});&#10;</code></pre>
<p>Calculating the sum can be done like this:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request, env) {&#10;    // Parse the Zaraz Context object&#10;    const { system, client } = await request.json();&#10;&#10;    // Get an array of all prices&#10;    const productsPrices = client.products.map((p) =&gt; p.price);&#10;&#10;    // Calculate the sum&#10;    const sum = productsPrices.reduce((partialSum, a) =&gt; partialSum + a, 0);&#10;&#10;    return new Response(sum);&#10;  },&#10;};&#10;</code></pre>
<h3 id="match-a-cookie-with-a-user-in-your-backend">Match a cookie with a user in your backend</h3>
<p>Zaraz exposes all cookies automatically under the <code>system.cookies</code> object, so they are always available. Accessing the cookie and using it to query your backend might look like this:</p>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request, env) {&#10;    // Parse the Zaraz Context object&#10;    const { system, client } = await request.json();&#10;&#10;    // Get the value of the cookie &quot;login-cookie&quot;&#10;    const cookieValue = system.cookies[&quot;login-cookie&quot;];&#10;&#10;    const userId = await fetch(&quot;https://example.com/api/getUserIdFromCookie&quot;, {&#10;      method: POST,&#10;      body: cookieValue,&#10;    });&#10;&#10;    return new Response(userId);&#10;  },&#10;};&#10;</code></pre>
<h3 id="hash-a-value-before-sending-it-to-a-third-party-vendor">Hash a value before sending it to a third-party vendor</h3>
<p>Assuming you're sending a value that you want to hash, for example, an email address:</p>
<pre tabindex="0"><code class="language-js">zaraz.track(&quot;user_logged_in&quot;, { email: &quot;user@example.com&quot; });&#10;</code></pre>
<p>You can access this property and hash it like this:</p>
<pre tabindex="0"><code class="language-js">async function digestMessage(message) {&#10;  const msgUint8 = new TextEncoder().encode(message); // encode as (utf-8) Uint8Array&#10;  const hashBuffer = await crypto.subtle.digest(&quot;SHA-256&quot;, msgUint8); // hash the message&#10;  const hashArray = Array.from(new Uint8Array(hashBuffer)); // convert buffer to byte array&#10;  const hashHex = hashArray&#10;    .map((b) =&gt; b.toString(16).padStart(2, &quot;0&quot;))&#10;    .join(&quot;&quot;); // convert bytes to hex string&#10;  return hashHex;&#10;}&#10;&#10;export default {&#10;  async fetch(request, env) {&#10;    // Parse the Zaraz Context object&#10;    const { system, client } = await request.json();&#10;&#10;    const { email } = client;&#10;&#10;    return new Response(await digestMessage(email));&#10;  },&#10;};&#10;</code></pre>
