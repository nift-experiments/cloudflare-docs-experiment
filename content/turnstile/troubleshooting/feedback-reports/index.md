<p>When Cloudflare detects that a challenge has failed or the user cannot be verified on a page with Turnstile, the user will encounter an <a href="/turnstile/concepts/widget/#error-states">error</a> on the widget and may be asked to send feedback on the issue that they have encountered by choosing one of the options listed.</p>
<p>When debugging or submitting a feedback report for an unresolved issue, you must provide the Ray ID (a request identifier displayed on the challenge page) or QR code associated with the challenge. These identifiers are essential for Cloudflare Support to trace the specific event.</p>
<p>To obtain these identifiers:</p>
<ol>
<li>Ray ID: Find the Ray ID displayed at the end of the Challenge Page. The RayID is collected by the feedback report.</li>
<li>QR Code: Click the success, failure, or spinner logo on the Turnstile widget four times. This action will reveal the unique QR code for that challenge instance.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14995.md")
</aside>
<p>Available options include:</p>
<ul>
<li>The widget always fails</li>
<li>The widget sometimes fails</li>
<li>The widget is too slow</li>
<li>The widget keeps looping</li>
<li>Other</li>
</ul>
<p>Users can provide additional data in the text field and then select <strong>Submit</strong>.</p>
