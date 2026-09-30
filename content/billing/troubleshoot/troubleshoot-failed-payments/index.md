<p>If a payment fails when purchasing a product, changing a subscription, or paying an invoice, you may see one of the following error messages:</p>
<ul>
<li>&quot;The payment has failed. Please contact your bank or use a different payment method.&quot;</li>
<li>&quot;Payment error: authorization failed for [“example.com”]&quot;</li>
</ul>
<p>You may also receive an email with the subject &quot;[Cloudflare]: We could not process your renewal payment&quot; when a recurring subscription charge fails.</p>
<h2 id="what-happens-next">What happens next</h2>
<p>If the failed payment relates to a recurring charge for a Cloudflare plan, add-on, or subscription, your account is automatically downgraded to a Free plan after a 5-day grace period. Downgrading to a Free plan does not suspend your website, but you lose any paid features associated with the Pro, Business, or Enterprise plan.</p>
<p>To avoid this, resolve the failed payment and retry using the steps below. If you do not resolve the issue within the 5-day grace period, you must manually re-subscribe to each product. You may also need to <a href="/billing/manage/pay-invoices-overdue-balances/#pay-an-outstanding-balance">pay an outstanding balance</a> from the grace period.</p>
<h2 id="causes">Causes</h2>
<ul>
<li>Your card details are incorrect.</li>
<li>Your account has insufficient funds.</li>
<li>The 3D Secure (3DS) authentication did not complete.</li>
<li>Your bank is rate limiting payments from Cloudflare.</li>
<li>Your bank is declining the payment.</li>
</ul>
<h2 id="fix-the-payment-method">Fix the payment method</h2>
<h3 id="check-your-payment-details">Check your payment details</h3>
<ul>
<li>Confirm that your billing address matches the address registered with your bank.</li>
<li>Confirm that the Card Verification Value (CVC) is correct.</li>
<li>If you use PayPal, check your PayPal email address for a verification email and follow the authorization instructions.</li>
</ul>
<h3 id="check-account-funds">Check account funds</h3>
<p>Verify that your payment method has enough funds to cover the charge.</p>
<h3 id="complete-3d-secure-authentication">Complete 3D Secure authentication</h3>
<p>Some banks require 3DS authentication for online card transactions. For one-time payments or first-time subscription payments, be ready to complete the 3DS prompt when you attempt payment in the Cloudflare dashboard. Your bank may contact you by SMS or push notification from its mobile application.</p>
<p>For customers of Indian banks, 3DS is mandatory for all transactions according to the Reserve Bank of India (RBI) mandate.</p>
<h3 id="contact-your-bank">Contact your bank</h3>
<p>Cloudflare's payment system does not know why a payment was declined. Contact your bank to find out the specific reason for the decline.</p>
<p>If you purchased or renewed multiple domains through <a href="/registrar/">Cloudflare Registrar</a>, each domain is charged as a separate transaction. Your credit card company may flag these charges as fraud. Contact your bank to confirm and resolve this.</p>
<h2 id="retry-the-payment">Retry the payment</h2>
<p>After you check the items above, retry your transaction in the Cloudflare dashboard. If the failed payment was for a renewal, Cloudflare retries automatically five times over five days. Retrying manually in the dashboard gives you instant feedback.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3384.md")
</div>
<h2 id="try-a-new-payment-method">Try a new payment method</h2>
<p>If you cannot resolve the issue with your current payment method, try an alternative payment method. Cloudflare accepts credit and debit cards (Visa, Mastercard, American Express, Discover), PayPal, Apple Pay, Google Pay, and Stripe Link. To try another payment method, refer to <a href="/billing/get-started/update-billing-info/#update-payment-methods">Update payment methods</a>.</p>
<h2 id="verify-the-fix">Verify the fix</h2>
<p>After payment succeeds, allow up to 24 hours for Cloudflare to recognize the payment and return your account to good standing. After that time, retry the purchase, subscription change, or invoice payment that failed.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/billing/manage/pay-invoices-overdue-balances/">Pay an outstanding balance</a> — Resolve unpaid invoices</li>
<li><a href="/billing/get-started/update-billing-info/">Update billing information</a> — Change your payment method</li>
<li><a href="/billing/troubleshoot/error-reference/">Error reference</a> — Look up other billing error messages</li>
</ul>
