<p>If a subscription renewal payment fails on your primary payment method, Cloudflare automatically retries the payment using your additional payment methods on file. This keeps your services active without requiring you to take action.</p>
<h2 id="how-auto-retry-works">How auto-retry works</h2>
<ol>
<li><strong>Primary attempt</strong>: Cloudflare attempts your subscription renewal payment using your primary (default) payment method.</li>
<li><strong>Automatic retry</strong>: If the payment fails, Cloudflare attempts each of your other payment methods in sequence.</li>
<li><strong>Success notification</strong>: If a retry succeeds, your services remain active and you receive an email confirming which payment method was charged.</li>
<li><strong>All methods fail</strong>: If all payment methods fail, standard payment retry processes continue. You may receive an email asking you to update your payment information.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3408.md")
</aside>
<h2 id="eligibility">Eligibility</h2>
<p>Auto-retry is available to pay-as-you-go accounts with at least two payment methods on file — one primary and one or more additional methods. The feature is enabled automatically. No action is needed to turn it on.</p>
<h2 id="supported-payment-methods">Supported payment methods</h2>
<p>Auto-retry works with all payment methods supported by Cloudflare, including credit cards, debit cards, and PayPal. Auto-retry supports any combination of primary and additional payment method types.</p>
<h2 id="email-notification">Email notification</h2>
<p>When an additional payment method is charged, you receive an email with:</p>
<ul>
<li>The invoice amount and number</li>
<li>Which primary payment method failed</li>
<li>Which additional payment method was charged</li>
<li>A link to manage your payment methods</li>
</ul>
<h2 id="manage-your-payment-methods">Manage your payment methods</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3409.md")
</div>
<p>Add a second payment method to ensure auto-retry can keep your services active if your primary method fails.</p>
<h2 id="faq">FAQ</h2>
<h3 id="multiple-charges">Multiple charges</h3>
<p>You are never charged on more than one payment method for the same invoice. An additional payment method is only charged if your primary payment method fails.</p>
<h3 id="all-payment-methods-fail">All payment methods fail</h3>
<p>If your primary and all additional payment methods fail, the standard payment retry process continues. You may receive an email asking you to update your payment information.</p>
<h3 id="multiple-additional-payment-methods">Multiple additional payment methods</h3>
<p>All additional payment methods are tried in sequence if your primary payment method fails. The more payment methods you have on file, the more chances for your payment to succeed automatically.</p>
<h3 id="next-renewal-behavior">Next renewal behavior</h3>
<p>Your next renewal always attempts your primary (default) payment method first. Additional payment methods are only used if the primary fails.</p>
<h3 id="terminology">Terminology</h3>
<p>The label &quot;Backup payment method&quot; was renamed to &quot;Additional payment method&quot; in the Cloudflare dashboard. The auto-retry behavior described on this page is unchanged.</p>
