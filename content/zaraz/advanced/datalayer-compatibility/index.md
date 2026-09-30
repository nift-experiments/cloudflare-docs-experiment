<p>Cloudflare Zaraz offers backwards compatibility with the <code>dataLayer</code> function found in tag management software, used to track events and other parameters. This way you can keep your current implementation and Cloudflare Zaraz will automatically collect your events.</p>
<p>To keep the Zaraz script as small and fast as possible, the data layer compatibility mode is disabled by default. To enable it:</p>
<ol>
<li>Go to <a href="https://dash.cloudflare.com/?to=/:account/:zone/zaraz"><strong>Zaraz</strong></a> &gt; <strong>Settings</strong>.</li>
<li>Enable the <strong>Data layer compatibility mode</strong> toggle. Refer to <a href="/zaraz/reference/settings/">Zaraz settings</a> for more information.</li>
</ol>
<h2 id="using-the-data-layer-with-zaraz">Using the data layer with Zaraz</h2>
<p>After enabling the compatibility mode, Zaraz will automatically translate your <code>dataLayer.push()</code> calls to <code>zaraz.track()</code>, so you can keep using the <code>dataLayer.push()</code> function to send events from the browser to Zaraz.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/17611.md")
</aside>
<p>Events will only be sent to Zaraz if your pushed object includes an <code>event</code> key. The <code>event</code>key is used as the name for the Zaraz event. Other keys will become part of the <code>eventProperties</code> object. The following example shows how a purchase event will be sent using the data layer to Zaraz — note that the parameters inside the object depend on what you want to track:</p>
<pre><code class="language-js">dataLayer.push({&#10;  event: &#x27;purchase&#x27;,&#10;  price: &#x27;24&#x27;,&#10;  currency: &#x27;USD&#x27;,&#10;  transactionID: &#x27;12345678&#x27;,&#10;});&#10;</code></pre>
<p>Cloudflare Zaraz then translates the <code>dataLayer.push()</code> call to a <code>zaraz.track()</code> call. So, <code>dataLayer.push({event: &quot;purchase&quot;, price: &quot;24&quot;, &quot;currency&quot;: &quot;USD&quot;})</code> is equivalent to <code>zaraz.track(&quot;purchase&quot;, {&quot;price&quot;: &quot;24&quot;, &quot;currency&quot;: &quot;USD&quot;})</code>.</p>
<p>Because Zaraz converts the <code>dataLayer.push()</code> call to <code>zaraz.track()</code>, creating a trigger based on <code>dataLayer.push()</code> calls is the same as creating triggers for <code>zaraz.track()</code>. As an example, the trigger below will match the above <code>dataLayer.push()</code> call because it matches the event with <code>purchase</code>.</p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Variable name</th>
<th>Match operation</th>
<th>Match string</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Match rule</em></td>
<td><em>Event Name</em></td>
<td><em>Equals</em></td>
<td><code>purchase</code></td>
</tr>
</tbody>
</table>
<p>We do not recommend using <code>dataLayer</code>. However, as many websites employ it, Cloudflare Zaraz has this automatic translation layer that converts it to <code>zaraz.track()</code>.</p>
