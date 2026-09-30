<p>Configure your Turnstile widget's appearance, behavior, and functionality using data attributes or JavaScript render parameters.</p>
<h2 id="rendering-methods">Rendering methods</h2>
<p>Turnstile widgets can be implemented using implicit or explicit rendering.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15052.md")
</div></div>
<hr />
<h2 id="widget-sizes">Widget sizes</h2>
<p>The Turnstile widget can have two different fixed sizes or a flexible width size when using the Managed or Non-Interactive modes.</p>
<table>
<thead>
<tr>
<th>Size</th>
<th>Width</th>
<th>Height</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td>Normal</td>
<td>300px</td>
<td>65px</td>
<td>Standard implementation</td>
</tr>
<tr>
<td>Flexible</td>
<td>100% (min: 300px)</td>
<td>65px</td>
<td>Responsive design</td>
</tr>
<tr>
<td>Compact</td>
<td>150px</td>
<td>140px</td>
<td>Space-constrained layouts</td>
</tr>
</tbody>
</table>
<ul>
<li><code>normal</code>: The default size works well for most desktop and mobile layouts. Use this if you have adequate horizontal space on your website or form.</li>
<li><code>flexible</code>: Automatically adapts to the container width while maintaining minimum usability. Use this for responsive designs that need to work across all screen sizes.</li>
<li><code>compact</code>: Ideal for mobile interfaces, sidebars, or any space where horizontal space is limited. The compact widget is taller than normal to accommodate the smaller width.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15047.md")
</aside>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15055.md")
</div></div>
<hr />
<h2 id="theme-options">Theme options</h2>
<p>Customize the widget's visual appearance to match your website's design.</p>
<ul>
<li><code>auto</code> (default): Automatically matches the visitor's system theme preference. Auto is recommended for most implementations as it respects the visitor's preferences and provides the best accessibility experience.</li>
<li><code>light</code>: Light theme with bright colors and clear contrast. Light theme works best on bright backgrounds and provides high contrast for readability.</li>
<li><code>dark</code>: Dark theme optimized for dark interfaces. Dark theme is ideal for dark interfaces, gaming sites, or applications with dark color schemes.</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15058.md")
</div></div>
<hr />
<h2 id="appearance-modes">Appearance modes</h2>
<p>Control when the widget becomes visible to visitors using the appearance mode.</p>
<ul>
<li><code>always</code> (default): The widget is always visible from page load. This is the best option for most implementations where you want your visitors to see the widget immediately as it provides clear visual feedback that security verification is in place.</li>
<li><code>execute</code>: The widget only becomes visible after the challenge begins. This is useful for when you need to control the timing of widget appearance, such as showing it only when a visitor starts filling out a form or selecting a submit button.</li>
<li><code>interaction-only</code>: The widget becomes visible only when visitor interaction is required and provides the cleanest visitor experience. Most visitors will never see the widget, but suspected bots will encounter the interactive challenge.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15046.md")
</aside>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15061.md")
</div></div>
<hr />
<h2 id="execution-modes">Execution modes</h2>
<p>Control when the challenge runs and a token is generated.</p>
<ul>
<li>
<p><code>render</code> (default): The challenge runs automatically after calling the <code>render()</code> function and provides immediate protection as soon as the widget loads. The challenge runs in the background while the page loads, ensuring the token is ready when the visitor submits data.</p>
</li>
<li>
<p><code>execute</code>: The challenge runs after calling the <code>turnstile.execute()</code> function separately and gives you precise control over when verification occurs. This option is useful for multi-step forms, conditional verification, or when you want to defer the challenge until the visitor actually attempts to submit data. This can improve page load performance and visitor experience by only running verification when needed.</p>
<p><strong>Common scenarios</strong></p>
<ul>
<li>Multi-step forms: Run verification only on the final step.</li>
<li>Conditional protection: Only verify visitors who meet certain criteria.</li>
<li>Performance optimization: Defer verification to reduce initial page load time.</li>
<li>User-triggered verification: Let visitors manually start the verification process.</li>
</ul>
</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15064.md")
</div></div>
<hr />
<h2 id="language-configuration">Language configuration</h2>
<p>Set the language for the widget interface.</p>
<ul>
<li><code>auto</code> (default): Uses the visitor's browser language preference.</li>
<li>Specific language codes: ISO 639-1 two-letter codes, such as <code>es</code>, <code>fr</code>, <code>de</code>.</li>
<li>Language and region: Combined codes for regional variants, such as <code>en-US</code>, <code>es-MX</code>, <code>pt-BR</code>.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/15045.md")
</aside>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15067.md")
</div></div>
<hr />
<h2 id="callback-configuration">Callback configuration</h2>
<p>Handle widget events with callbacks.</p>
<ul>
<li><code>callback</code>: Triggered when the challenge is successfully completed.</li>
<li><code>error-callback</code>: Triggered when an error occurs during the challenge.</li>
<li><code>expired-callback</code>: Triggered when a token expires (before timeout).</li>
<li><code>timeout-callback</code>: Triggered when an interactive challenge times out.</li>
</ul>
<p>The success callback receives a token that must be validated on your server using the Siteverify API. Tokens are single-use and expire after 300 seconds (five minutes).</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15070.md")
</div></div>
<h3 id="best-practices">Best practices</h3>
<ul>
<li>Always implement the success callback to handle the token and proceed with form submission or next steps.</li>
<li>Use error callbacks for graceful error handling and visitor feedback.</li>
<li>Monitor expired tokens to refresh challenges before they become invalid.</li>
<li>Handle timeouts to guide visitors through challenge resolution.</li>
</ul>
<hr />
<h2 id="advanced-configuration-options">Advanced configuration options</h2>
<h3 id="retry-behavior">Retry behavior</h3>
<p>Control how Turnstile handles failed challenges.</p>
<ul>
<li><code>auto</code> (default): Automatically retries failed challenges. Auto retry provides better visitor experience by automatically recovering from temporary network issues or processing errors.</li>
<li><code>never</code>: Disables automatic retry. This requires manual intervention and gives you full control over error handling in applications that need custom retry logic.</li>
<li><code>retry-interval</code>: Controls the time between retry attempts (default: 8000ms) and lets you balance between quick recovery and server load.</li>
</ul>
<pre><code class="language-html">&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot; data-retry=&quot;never&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot; data-retry-interval=&quot;0000&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<h3 id="refresh-behavior">Refresh behavior</h3>
<p>Control how Turnstile handles token expiration and interactive timeouts.</p>
<ul>
<li><code>refresh-expired</code>: Controls behavior when tokens expire (<code>auto</code>, <code>manual</code>, <code>never</code>).</li>
<li><code>refresh-timeout</code>: Controls behavior when interactive challenges timeout (<code>auto</code>, <code>manual</code>, <code>never</code>).</li>
</ul>
<h4 id="benefits">Benefits</h4>
<ul>
<li><code>auto</code> refresh provides seamless visitor experience but uses more resources.</li>
<li><code>manual</code> refresh gives visitors control but requires them to take action.</li>
<li><code>never</code> refresh requires your application to handle all refresh logic.</li>
</ul>
<p>Different strategies can be used for token expiration versus interactive timeouts based on your visitor experience requirements.</p>
<pre><code class="language-html">&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot; data-refresh-expired=&quot;manual&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot; data-refresh-timeout=&quot;auto&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<h3 id="custom-data">Custom data</h3>
<p>Add custom identifiers and data to your challenges.</p>
<ul>
<li><code>action</code>: A custom identifier for analytics and differentiation (maximum 32 characters).</li>
<li><code>cData</code>: Custom payload data returned during validation (maximum 255 characters).</li>
</ul>
<h4 id="use-cases">Use cases</h4>
<ul>
<li>Action tracking: Differentiate between login, signup, contact forms, and more. in your analytics.</li>
<li>Visitor context: Pass visitor IDs, session information, or other contextual data.</li>
<li>A/B testing: Track different widget configurations or page variants.</li>
<li>Fraud detection: Include additional context for risk assessment.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15044.md")
</aside>
<pre><code class="language-html">&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot; data-action=&quot;login&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot; data-cdata=&quot;user-cdata&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<h3 id="form-integration">Form integration</h3>
<p>Configure how Turnstile integrates with HTML forms.</p>
<p>When enabled, Turnstile automatically creates a hidden <code>&lt;input&gt;</code> element with the verification token. This gets submitted along with your other form data, making server-side validation straightforward.</p>
<ul>
<li><code>response-field</code>: Determines whether to create a hidden form field with the token (<code>default: true</code>)</li>
<li><code>response-field-name</code>: Custom name for the hidden form field (<code>default: cf-turnstile-response</code>)</li>
</ul>
<h4 id="benefits-1">Benefits</h4>
<ul>
<li>Automatic form integration means that the token is included when the form is submitted, requiring no additional JavaScript.</li>
<li>Custom field names helps avoid conflicts with existing form fields.</li>
<li>Disabled response fields give you full control over token handling for complex form scenarios.</li>
</ul>
<pre><code class="language-html">&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot; data-response-field-name=&quot;turnstile-token&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot; data-response-field=&quot;false&quot;&gt;&lt;/div&gt;&#10;</code></pre>
<hr />
<h2 id="complete-configuration-reference">Complete configuration reference</h2>
<table>
<thead>
<tr>
<th>JavaScript Render Parameters</th>
<th>Data Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sitekey</code></td>
<td><code>data-sitekey</code></td>
<td>Every widget has a sitekey. This sitekey is associated with the corresponding widget configuration and is created upon the widget creation.</td>
</tr>
<tr>
<td><code>action</code></td>
<td><code>data-action</code></td>
<td>A customer value that can be used to differentiate widgets under the same sitekey in analytics and which is returned upon validation. This can only contain up to 32 alphanumeric characters including <code>_</code> and <code>-</code>.</td>
</tr>
<tr>
<td><code>cData</code></td>
<td><code>data-cdata</code></td>
<td>A customer payload that can be used to attach customer data to the challenge throughout its issuance and which is returned upon validation. This can only contain up to 255 alphanumeric characters including <code>_</code> and <code>-</code>.</td>
</tr>
<tr>
<td><code>callback</code></td>
<td><code>data-callback</code></td>
<td>A JavaScript callback invoked upon success of the challenge. The callback is passed a token that can be validated.</td>
</tr>
<tr>
<td><code>error-callback</code></td>
<td><code>data-error-callback</code></td>
<td>A JavaScript callback invoked when there is an error (e.g. network error or the challenge failed). Refer to <a href="/turnstile/troubleshooting/client-side-errors/">Client-side errors</a>.</td>
</tr>
<tr>
<td><code>execution</code></td>
<td><code>data-execution</code></td>
<td>Execution controls when to obtain the token of the widget and can be on <code>render</code> (default) or on <code>execute</code>. Refer to <a href="/turnstile/get-started/client-side-rendering/#execution-modes">Execution Modes</a> for more information.</td>
</tr>
<tr>
<td><code>expired-callback</code></td>
<td><code>data-expired-callback</code></td>
<td>A JavaScript callback invoked when the token expires and does not reset the widget.</td>
</tr>
<tr>
<td><code>before-interactive-callback</code></td>
<td><code>data-before-interactive-callback</code></td>
<td>A JavaScript callback invoked before the challenge enters interactive mode.</td>
</tr>
<tr>
<td><code>after-interactive-callback</code></td>
<td><code>data-after-interactive-callback</code></td>
<td>A JavaScript callback invoked when challenge has left interactive mode.</td>
</tr>
<tr>
<td><code>unsupported-callback</code></td>
<td><code>data-unsupported-callback</code></td>
<td>A JavaScript callback invoked when a given client/browser is not supported by Turnstile.</td>
</tr>
<tr>
<td><code>theme</code></td>
<td><code>data-theme</code></td>
<td>The widget theme. Can take the following values: <code>light</code>, <code>dark</code>, <code>auto</code>. <br/><br/>The default is <code>auto</code>, which respects the visitor preference. This can be forced to light or dark by setting the theme accordingly.</td>
</tr>
<tr>
<td><code>language</code></td>
<td><code>data-language</code></td>
<td>Language to display, must be either: <code>auto</code> (default) to use the language that the visitor has chosen, or an ISO 639-1 two-letter language code (e.g. <code>en</code>) or language and country code (e.g. <code>en-US</code>). Refer to the <a href="/turnstile/reference/supported-languages/">list of supported languages</a> for more information.</td>
</tr>
<tr>
<td><code>tabindex</code></td>
<td><code>data-tabindex</code></td>
<td>The tabindex of Turnstile's iframe for accessibility purposes. The default value is <code>0</code>.</td>
</tr>
<tr>
<td><code>timeout-callback</code></td>
<td><code>data-timeout-callback</code></td>
<td>A JavaScript callback invoked when the challenge presents an interactive challenge but was not solved within a given time. A callback will reset the widget to allow a visitor to solve the challenge again.</td>
</tr>
<tr>
<td><code>response-field</code></td>
<td><code>data-response-field</code></td>
<td>A boolean that controls if an input element with the response token is created, defaults to <code>true</code>.</td>
</tr>
<tr>
<td><code>response-field-name</code></td>
<td><code>data-response-field-name</code></td>
<td>Name of the input element, defaults to <code>cf-turnstile-response</code>.</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>data-size</code></td>
<td>The widget size. Can take the following values: <code>normal</code>, <code>flexible</code>, <code>compact</code>.</td>
</tr>
<tr>
<td><code>retry</code></td>
<td><code>data-retry</code></td>
<td>Controls whether the widget should automatically retry to obtain a token if it did not succeed. The default is <code>auto</code>, which will retry automatically. This can be set to <code>never</code> to disable retry on failure.</td>
</tr>
<tr>
<td><code>retry-interval</code></td>
<td><code>data-retry-interval</code></td>
<td>When <code>retry</code> is set to <code>auto</code>, <code>retry-interval</code> controls the time between retry attempts in milliseconds. Value must be a positive integer less than <code>900000</code>, defaults to <code>8000</code>.</td>
</tr>
<tr>
<td><code>refresh-expired</code></td>
<td><code>data-refresh-expired</code></td>
<td>Automatically refreshes the token when it expires. Can take <code>auto</code>, <code>manual</code>, or <code>never</code>, defaults to <code>auto</code>.</td>
</tr>
<tr>
<td><code>refresh-timeout</code></td>
<td><code>data-refresh-timeout</code></td>
<td>Controls whether the widget should automatically refresh upon entering an interactive challenge and observing a timeout. Can take <code>auto</code> (automatically refreshes upon encountering an interactive timeout), <code>manual</code> (prompts the visitor to manually refresh) or <code>never</code> (will show a timeout), defaults to <code>auto</code>. Only applies to widgets of Managed mode.</td>
</tr>
<tr>
<td><code>appearance</code></td>
<td><code>data-appearance</code></td>
<td>Appearance controls when the widget is visible. It can be <code>always</code> (default), <code>execute</code>, or <code>interaction-only</code>. Refer to <a href="/turnstile/get-started/client-side-rendering/#appearance-modes">Appearance modes</a> for more information.</td>
</tr>
<tr>
<td><code>feedback-enabled</code></td>
<td><code>data-feedback-enabled</code></td>
<td>Allows Cloudflare to gather visitor feedback upon widget failure. It can be <code>true</code> (default) or <code>false</code>.</td>
</tr>
<tr>
<td><code>offlabel-show-privacy</code></td>
<td><code>data-offlabel-show-privacy</code></td>
<td>Displays privacy link for unbranded Turnstile widgets. Can be <code>true</code> (default) or <code>false</code>.</td>
</tr>
<tr>
<td><code>offlabel-show-help</code></td>
<td><code>data-offlabel-show-help</code></td>
<td>Displays help link for unbranded Turnstile widgets. Can be <code>true</code> (default) or <code>false</code>.</td>
</tr>
</tbody>
</table>
<h3 id="examples">Examples</h3>
<pre><code class="language-html">&lt;div style=&quot;max-width: 500px;&quot;&gt;&#10;  &lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot; data-size=&quot;flexible&quot; data-theme=&quot;auto&quot;&gt;&lt;/div&gt;&#10;&lt;/div&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;div class=&quot;cf-turnstile&quot; data-sitekey=&quot;&lt;YOUR-SITE-KEY&gt;&quot; data-size=&quot;compact&quot; data-theme=&quot;light&quot; data-language=&quot;en&quot;&gt;&#10;&lt;/div&gt;&#10;</code></pre>
