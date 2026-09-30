---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/
  description: Capture a screenshot of a fully rendered webpage using the Browser Run /screenshot endpoint.
  full_title: /screenshot - Capture screenshot · Cloudflare Browser Run docs
  head_html: <title>/screenshot - Capture screenshot · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Capture a screenshot of a fully rendered webpage using the Browser Run /screenshot endpoint."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/index.md"><meta property="og:title" content="/screenshot - Capture screenshot · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Capture a screenshot of a fully rendered webpage using the Browser Run /screenshot endpoint."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/#page","headline":"/screenshot - Capture screenshot \u00b7 Cloudflare Browser Run docs","description":"Capture a screenshot of a fully rendered webpage using the Browser Run /screenshot endpoint.","url":"https://developers.cloudflare.com/browser-run/quick-actions/screenshot-endpoint/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/quick-actions/screenshot-endpoint/
  schema: 1
---
<p>The <code>/screenshot</code> endpoint renders the webpage by processing its HTML and JavaScript, then captures a screenshot of the fully rendered page.</p>
<p>You can use this endpoint in two ways:</p>
<ul>
<li><strong>REST API</strong>: <a href="/fundamentals/api/get-started/create-token/">Create a custom API Token</a> with <code>Browser Rendering - Edit</code> permission.</li>
<li><strong>Workers Bindings</strong>: Call the endpoint directly from a <a href="/workers/">Cloudflare Worker</a> using the <a href="/browser-run/reference/wrangler/#bindings">Workers Bindings</a>. No API token is needed.</li>
</ul>
<p>For more information, refer to <a href="/browser-run/quick-actions/#before-you-begin">Quick Actions: Before you begin</a>.</p>
<h2 id="endpoint">Endpoint</h2>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#10;</code></pre>
<h2 id="required-fields">Required fields</h2>
<p>You must provide either <code>url</code> or <code>html</code>:</p>
<ul>
<li><code>url</code> (string)</li>
<li><code>html</code> (string)</li>
</ul>
<h2 id="common-use-cases">Common use cases</h2>
<ul>
<li>Generate previews for websites, dashboards, or reports</li>
<li>Capture screenshots for automated testing, QA, or visual regression</li>
</ul>
<h2 id="basic-usage">Basic usage</h2>
<h3 id="take-a-screenshot-from-custom-html">Take a screenshot from custom HTML</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3602.md")
</div></div>
<h3 id="take-a-screenshot-from-a-url">Take a screenshot from a URL</h3>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.png&quot;&#10;</code></pre>
<p>For more options to control the final screenshot, like <code>clip</code>, <code>captureBeyondViewport</code>, <code>fullPage</code> and others, check the endpoint <a href="/api/resources/browser_rendering/subresources/screenshot/methods/create/">reference</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes-for-basic-usage">Notes for basic usage</h3>
@markup("md", "content/.markup/bodies/3598.md")
</aside>
<h2 id="advanced-usage">Advanced usage</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="looking-for-more-parameters">Looking for more parameters?</h3>
@markup("md", "content/.markup/bodies/3597.md")
</aside>
<h3 id="capture-a-screenshot-of-an-authenticated-page">Capture a screenshot of an authenticated page</h3>
<p>Some webpages require authentication before you can view their content. Browser Run supports three authentication methods, which work across all <a href="/browser-run/quick-actions/">Quick Actions</a> endpoints. For a quick reference of all methods, refer to <a href="/browser-run/faq/#how-do-i-render-authenticated-pages-using-quick-actions">How do I render authenticated pages using Quick Actions?</a>.</p>
<h4 id="cookie-based-authentication">Cookie-based authentication</h4>
<p>Provide valid session cookies to access pages that require login:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com/protected-page&quot;,&#10;    &quot;cookies&quot;: [&#10;      {&#10;        &quot;name&quot;: &quot;session_id&quot;,&#10;        &quot;value&quot;: &quot;your-session-cookie-value&quot;,&#10;        &quot;domain&quot;: &quot;example.com&quot;,&#10;        &quot;path&quot;: &quot;/&quot;&#10;      }&#10;    ]&#10;  }&#x27; \&#10;  &#45;-output &quot;authenticated-screenshot.png&quot;&#10;</code></pre>
<h4 id="http-basic-auth">HTTP Basic Auth</h4>
<p>Use the <code>authenticate</code> parameter for pages behind HTTP Basic Authentication:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com/protected-page&quot;,&#10;    &quot;authenticate&quot;: {&#10;      &quot;username&quot;: &quot;user&quot;,&#10;      &quot;password&quot;: &quot;pass&quot;&#10;    }&#10;  }&#x27; \&#10;  &#45;-output &quot;authenticated-screenshot.png&quot;&#10;</code></pre>
<h4 id="token-based-authentication">Token-based authentication</h4>
<p>Add custom authorization headers using <code>setExtraHTTPHeaders</code>:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com/protected-page&quot;,&#10;    &quot;setExtraHTTPHeaders&quot;: {&#10;      &quot;Authorization&quot;: &quot;Bearer your-token&quot;&#10;    }&#10;  }&#x27; \&#10;  &#45;-output &quot;authenticated-screenshot.png&quot;&#10;</code></pre>
<h3 id="navigate-and-capture-a-full-page-screenshot">Navigate and capture a full-page screenshot</h3>
<p>Navigate to <code>https://cloudflare.com/</code>, change the page size (<code>viewport</code>) and wait until there are no active network connections (<code>waitUntil</code>) or up to a maximum of <code>4500ms</code> (<code>timeout</code>) before capturing a <code>fullPage</code> screenshot.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://cloudflare.com/&quot;,&#10;    &quot;screenshotOptions&quot;: {&#10;       &quot;fullPage&quot;: true&#10;    },&#10;    &quot;viewport&quot;: {&#10;      &quot;width&quot;: 1280,&#10;      &quot;height&quot;: 720&#10;    },&#10;    &quot;gotoOptions&quot;: {&#10;      &quot;waitUntil&quot;: &quot;networkidle0&quot;,&#10;      &quot;timeout&quot;: 45000&#10;    }&#10;  }&#x27; \&#10;  &#45;-output &quot;advanced-screenshot.png&quot;&#10;</code></pre>
<h3 id="improve-blurry-screenshot-resolution">Improve blurry screenshot resolution</h3>
<p>If you set a large viewport width and height, your screenshot may appear blurry or pixelated. This can happen if your browser's default <code>deviceScaleFactor</code> (which defaults to 1) is not high enough for the viewport.</p>
<p>To fix this, increase the value of the <code>deviceScaleFactor</code>.</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;url&quot;: &quot;https://cloudflare.com/&quot;,&#10;  &quot;viewport&quot;: {&#10;    &quot;width&quot;: 3600,&#10;    &quot;height&quot;: 2400,&#10;    &quot;deviceScaleFactor&quot;: 2&#10;  }&#10;}&#10;</code></pre>
<h3 id="customize-css-and-embed-custom-javascript">Customize CSS and embed custom JavaScript</h3>
<p>Instruct the browser to go to <code>https://example.com</code>, embed custom JavaScript (<code>addScriptTag</code>) and add extra styles (<code>addStyleTag</code>), both inline (<code>addStyleTag.content</code>) and by loading an external stylesheet (<code>addStyleTag.url</code>).</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com/&quot;,&#10;    &quot;addScriptTag&quot;: [&#10;      { &quot;content&quot;: &quot;document.querySelector(`h1`).innerText = `Hello World!!!`&quot; }&#10;    ],&#10;    &quot;addStyleTag&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;div { background: linear-gradient(45deg, #2980b9  , #82e0aa  ); }&quot;&#10;      },&#10;      {&#10;        &quot;url&quot;: &quot;https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css&quot;&#10;      }&#10;    ]&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.png&quot;&#10;</code></pre>
<h3 id="capture-a-specific-element-using-the-selector-option">Capture a specific element using the selector option</h3>
<p>To capture a screenshot of a specific element on a webpage, use the <code>selector</code> option with a valid CSS selector. You can also configure the <code>viewport</code> to control the page dimensions during rendering.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-rendering/screenshot&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;,&#10;    &quot;selector&quot;: &quot;#example_element_name&quot;,&#10;    &quot;viewport&quot;: {&#10;      &quot;width&quot;: 1200,&#10;      &quot;height&quot;: 1600&#10;    }&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.png&quot;&#10;</code></pre>
<p>Many more options exist, like setting HTTP credentials using <code>authenticate</code>, setting <code>cookies</code>, and using <code>gotoOptions</code> to control page load behaviour - check the endpoint <a href="/api/resources/browser_rendering/subresources/screenshot/methods/create/">reference</a> for all available parameters.</p>
<h3 id="handling-javascript-heavy-pages">Handling JavaScript-heavy pages</h3>
<p>For JavaScript-heavy pages or Single Page Applications (SPAs), the default page load behavior may return empty or incomplete results. This happens because the browser considers the page loaded before JavaScript has finished rendering the content.</p>
<p>The simplest solution is to use the <code>gotoOptions.waitUntil</code> parameter set to <code>networkidle0</code> or <code>networkidle2</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;url&quot;: &quot;https://example.com&quot;,&#10;	&quot;gotoOptions&quot;: {&#10;		&quot;waitUntil&quot;: &quot;networkidle0&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For faster responses, advanced users can use <code>waitForSelector</code> to wait for a specific element instead of waiting for all network activity to stop. This requires knowing which CSS selector indicates the content you need has loaded. For more details, refer to <a href="/browser-run/reference/timeouts/">Quick Actions timeouts</a>.</p>
<h3 id="set-a-custom-user-agent">Set a custom user agent</h3>
<p>You can change the user agent at the page level by passing <code>userAgent</code> as a top-level parameter in the JSON body. This is useful if the target website serves different content based on the user agent.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3596.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
