<p>Instant Bank Payments (IBP) via <a href="https://link.co/">Link</a> lets you pay for Cloudflare services directly from your bank account. Link is a one-click checkout wallet that stores your payment details. If you already have a bank account saved in Link, it appears as a payment option at checkout. If not, you can connect one during the checkout flow.</p>
<h2 id="how-instant-bank-payments-works">How Instant Bank Payments works</h2>
<ol>
<li><strong>Checkout</strong>: Cloudflare presents your saved Link payment methods. You can also connect your bank with Link if not already set up.</li>
<li><strong>Select bank account</strong>: Your bank account appears as a payment option alongside your existing cards.</li>
<li><strong>Confirm payment</strong>: Select your bank account and confirm.</li>
<li><strong>Processing</strong>: The payment is authenticated and processed on your behalf.</li>
</ol>
<p>After your first Link authentication, your bank account is available for future purchases without re-entering details.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3403.md")
</aside>
<h2 id="eligibility">Eligibility</h2>
<p>Instant Bank Payments via Link is available to US-based self-serve accounts across all Cloudflare products. You can connect your bank account through Link during checkout.</p>
<h2 id="identify-bank-payments">Identify bank payments</h2>
<p>Bank-based Link payments appear in your billing history with these identifiers:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Payment method</td>
<td><code>link</code></td>
</tr>
<tr>
<td>Last four digits</td>
<td><code>0000</code></td>
</tr>
</tbody>
</table>
<p>Card-based Link payments display your card's last four digits, distinguishing them from bank payments.</p>
<h2 id="view-your-payment-history">View your payment history</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</li>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Billing</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Select <strong>Invoices</strong> to view your invoice and payment history.</li>
</ol>
<h2 id="failed-bank-payments">Failed bank payments</h2>
<p>If a bank payment cannot be processed:</p>
<ol>
<li><strong>Retry or switch</strong>: You are prompted to select a different payment method. You can retry with the same bank account or choose a card.</li>
<li><strong>Update payment method</strong>: If the issue persists, update your payment method in billing settings.</li>
</ol>
<div class="nb-dash-button"></div>
<p>Ensure your bank account has sufficient funds and supports instant payments.</p>
<h2 id="faq">FAQ</h2>
<h3 id="payment-identification">Payment identification</h3>
<p>Your billing history shows the payment method as <code>link</code> with last four digits <code>0000</code>. Card-based Link payments show your card's actual last four digits.</p>
<h3 id="bank-account-security">Bank account security</h3>
<p>Your bank credentials are stored in the Link wallet using encryption and multi-factor authentication. Your raw bank details are never shared with Cloudflare or other merchants.</p>
<h3 id="card-payment-availability">Card payment availability</h3>
<p>Instant Bank Payments is an additional option. Cards saved in Link or added manually remain available at checkout.</p>
<h3 id="processing-time">Processing time</h3>
<p>Bank payments through Link process in the same checkout flow as card payments. Your purchase is confirmed immediately.</p>
<h3 id="bank-account-removal">Bank account removal</h3>
<p>You can manage your saved payment methods, including bank accounts, through the <a href="https://link.co/">Link wallet</a>. Removing a bank account does not affect previously completed payments.</p>
<h3 id="incorrect-charges">Incorrect charges</h3>
<p><a href="/support/contacting-cloudflare-support/">Contact Cloudflare support</a> with your invoice number and payment details.</p>
