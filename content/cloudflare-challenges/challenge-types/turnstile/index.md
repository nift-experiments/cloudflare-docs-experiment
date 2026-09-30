<p><a href="/turnstile/">Turnstile</a> is Cloudflare's CAPTCHA-alternative solution. You can embed Turnstile as a widget on your website or application, where it runs a client-side challenge directly in the background of the visitor's browser.</p>
<p>Turnstile differs from Challenges Pages in that the challenge does not pause the request or interrupt the user's experience. Since the widget is embedded onto the webpage and only runs on a specific part of the HTML, the visitor will have already arrived at the destination URL and is viewing the page when they encounter a Turnstile widget. Instead of blocking the visitor from accessing the entire website, the Turnstile widget prevents the visitor from certain actions such as completing login or sign up forms, and more, until the widget is solved.</p>
<p>In most cases, nothing further is required from the visitor. However, if necessary, Turnstile may display a simple checkbox that the visitor must click to proceed.</p>
<p>After the challenge passes, Turnstile issues a clearance token to the visitor that must be validated via the <a href="/turnstile/get-started/server-side-validation/">Siteverify API</a> before completing a sensitive action like login, sign up, or other form submissions.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/4035.md")
</aside>
<h2 id="widget-types">Widget types</h2>
<p>While there are three types of widgets that you can choose to implement on your website or application, the challenge logic behind them remains the same.</p>
<ul>
<li>
<p><strong>Managed (recommended)</strong>: Functions similar to a Managed Challenge Page. It selects a challenge based on the signals gathered from the visitor's browser and presents an interaction only if it detects potentially automated traffic.</p>
</li>
<li>
<p><strong>Non-Interactive</strong>: The widget is displayed, but the visitor does not need to interact with it to verify their identity.</p>
</li>
<li>
<p><strong>Invisible</strong>: The widget is completely invisible to the visitor, but the challenge still runs in the background.</p>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="link-to-cloudflare-s-turnstile-privacy-policy">Link to Cloudflare's Turnstile Privacy Policy</h3>
@markup("md", "content/.markup/bodies/4034.md")
</aside>
<h2 id="implementation">Implementation</h2>
<p>When you create a widget for your website or application via the Cloudflare dashboard, you will receive a sitekey.</p>
<p>The sitekey is used with <a href="/turnstile/get-started/client-side-rendering/#implicitly-render-the-turnstile-widget">client-side rendering</a> by adding it to the <code>&lt;div&gt; </code> container placeholder. You will then place that <code>&lt;div&gt; </code> code snippet where you want to add the widget to your site page or form.</p>
<h2 id="get-started">Get started</h2>
<p>Refer to the <a href="/turnstile/get-started/">Turnstile documentation</a> for guidance on implementing a widget to your website or application.</p>
