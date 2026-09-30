<p>You can use <code>zaraz.track()</code> anywhere inside the <code>&lt;body&gt;</code> tag of a page.</p>
<p><code>zaraz.track()</code> allows you to track custom events on your website, that might happen in real time. It is an <code>async</code> function, so you can choose to <code>await</code> it if you would like to make sure it completed before running other code.</p>
<p>Example of user events you might be interested in tracking are successful sign-ups, calls-to-action clicks, or purchases. Common examples for other types of events are tracking the impressions of specific elements on a page, or loading a specific widget.</p>
<p>To start tracking events, use the <code>zaraz.track()</code> function like this:</p>
<pre><code class="language-js">zaraz.track(eventName, [eventProperties]);&#10;</code></pre>
<p>The <code>eventName</code> parameter is a string, and the <code>eventProperties</code> parameter is an optional flat object of additional context you can attach to the event using your own keys of choice. For example, tracking a purchase with the value of 200 USD could look like this:</p>
<pre><code class="language-js">zaraz.track(&quot;purchase&quot;, { value: 200, currency: &quot;USD&quot; });&#10;</code></pre>
<p>Note that the name of the event (<code>purchase</code> in the above example), the names of the keys (<code>value</code> and <code>currency</code>) and the number of keys are customizable by you. You choose what variables to track and how you want to track these variables. However, picking meaningful names will help you when you configure your triggers, because the trigger configuration has to match the events your website is sending.</p>
<p>After using <code>zaraz.track()</code> in your website, you will usually want to create a trigger based on it, and then use the trigger in an action. Start by <a href="/zaraz/custom-actions/create-trigger/">creating a new trigger</a>, with <em>Event Name</em> as your trigger's <strong>Variable name</strong>, and the <code>eventName</code> you are tracking in <strong>Match string</strong>. Following the above example, your trigger will look like this:</p>
<p><strong>Trigger example: Match <code>zaraz.track(&quot;purchase&quot;)</code></strong></p>
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
<p>In every tool you want to use this trigger, add an action with this trigger <a href="/zaraz/custom-actions/">configured as a firing trigger</a>. Each action that uses this trigger can access the <code>eventProperties</code> you have sent. In the <strong>Action</strong> fields, you can use <code>{{ client.&lt;KEY_NAME&gt; }}</code> to get the value of <code>&lt;KEY_NAME&gt;</code>. In the above example, Zaraz will replace <code>{{ client.value }}</code> with <code>200</code>. If your key includes special characters or numbers, surround it with backticks like <code>{{ client.`&lt;KEY_NAME&gt;` }}</code>.</p>
<p>For more information regarding the properties you can use with <code>zaraz.track()</code>, refer to <a href="/zaraz/reference/properties-reference/">Properties reference</a>.</p>
