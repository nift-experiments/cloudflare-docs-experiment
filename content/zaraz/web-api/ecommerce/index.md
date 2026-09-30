<p>You can use <code>zaraz.ecommerce()</code> anywhere inside the <code>&lt;body&gt;</code> tag of a page.</p>
<p><code>zaraz.ecommerce()</code> allows you to track common events of the e-commerce user journey, such as when a user adds a product to cart, starts the checkout funnel or completes an order on your website. It is an <code>async</code> function, so you can choose to <code>await</code> it if you would like to make sure it completed before running other code.</p>
<p>To start using <code>zaraz.ecommerce()</code>, you first need to enable it in your Zaraz account and enable the E-commerce action for the tool you plan to send e-commerce data to. Then, add <code>zaraz.ecommerce()</code> to the <code>&lt;body&gt;</code> element of your website.</p>
<p>Right now, Zaraz e-commerce is compatible with Google Analytics 3 (Universal Analytics), Google Analytics 4, Bing, Facebook Pixel, Amplitude, Pinterest Conversions API, TikTok and Branch.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/17596.md")
</aside>
<h2 id="enable-e-commerce-tracking">Enable e-commerce tracking</h2>
<p>You do not need to map e-commerce events to triggers. Zaraz automatically forwards data using the right format to the tools with e-commerce support.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Enable **E-commerce tracking**.
3. Select **Save**.
4. Go to **Zaraz** > **Tools Configuration** > **Third-party tools**.
5. Locate the tool you want to use with e-commerce tracking and select **Edit**.
6. Select **Settings**.
7. Under **Advanced**, enable **E-commerce tracking**.
8. Select **Save**.
<p>E-commerce tracking is now enabled. If you add additional tools to your website that you want to use with <code>zaraz.ecommerce()</code>, you will need to repeat steps 6-9 for that tool.</p>
<h2 id="add-e-commerce-tracking-to-your-website">Add e-commerce tracking to your website</h2>
<p>After enabling e-commerce tracking on your Zaraz dashboard, you need to add <code>zaraz.ecommerce()</code> to the <code>&lt;body&gt;</code> element of your website:</p>
<pre><code class="language-js">zaraz.ecommerce(&quot;Event Name&quot;, { parameters });&#10;</code></pre>
<p>To create a complete tracking event, you need to add an event and one or more parameters. Below you will find a list of events and parameters Zaraz supports, as well as code examples for different types of events.</p>
<h2 id="list-of-supported-events">List of supported events</h2>
<ul>
<li><code>Product List Viewed</code></li>
<li><code>Products Searched</code></li>
<li><code>Product Clicked</code></li>
<li><code>Product Added</code></li>
<li><code>Product Added to Wishlist</code></li>
<li><code>Product Removed</code></li>
<li><code>Product Viewed</code></li>
<li><code>Cart Viewed</code></li>
<li><code>Checkout Started</code></li>
<li><code>Checkout Step Viewed</code></li>
<li><code>Checkout Step Completed</code></li>
<li><code>Payment Info Entered</code></li>
<li><code>Order Completed</code></li>
<li><code>Order Updated</code></li>
<li><code>Order Refunded</code></li>
<li><code>Order Cancelled</code></li>
<li><code>Clicked Promotion</code></li>
<li><code>Viewed Promotion</code></li>
<li><code>Shipping Info Entered</code></li>
</ul>
<h2 id="list-of-supported-parameters">List of supported parameters:</h2>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>product_id</code></td>
<td>String</td>
<td>Product ID.</td>
</tr>
<tr>
<td><code>sku</code></td>
<td>String</td>
<td>Product SKU number.</td>
</tr>
<tr>
<td><code>category</code></td>
<td>String</td>
<td>Product category.</td>
</tr>
<tr>
<td><code>name</code></td>
<td>String</td>
<td>Product name.</td>
</tr>
<tr>
<td><code>brand</code></td>
<td>String</td>
<td>Product brand name.</td>
</tr>
<tr>
<td><code>variant</code></td>
<td>String</td>
<td>Product variant (depending on the product, it could be product color, size, etc.).</td>
</tr>
<tr>
<td><code>price</code></td>
<td>Number</td>
<td>Product price.</td>
</tr>
<tr>
<td><code>quantity</code></td>
<td>Number</td>
<td>Product number of units.</td>
</tr>
<tr>
<td><code>coupon</code></td>
<td>String</td>
<td>Name or serial number of coupon code associated with product.</td>
</tr>
<tr>
<td><code>position</code></td>
<td>Number</td>
<td>Product position in the product list (for example, <code>2</code>).</td>
</tr>
<tr>
<td><code>products</code></td>
<td>Array</td>
<td>List of products displayed in the product list.</td>
</tr>
<tr>
<td><code>products.[].product_id</code></td>
<td>String</td>
<td>Product ID displayed on the product list.</td>
</tr>
<tr>
<td><code>products.[].sku</code></td>
<td>String</td>
<td>Product SKU displayed on the product list.</td>
</tr>
<tr>
<td><code>products.[].category</code></td>
<td>String</td>
<td>Product category displayed on the product list.</td>
</tr>
<tr>
<td><code>products.[].name</code></td>
<td>String</td>
<td>Product name displayed on the product list.</td>
</tr>
<tr>
<td><code>products.[].brand</code></td>
<td>String</td>
<td>Product brand displayed on the product list.</td>
</tr>
<tr>
<td><code>products.[].variant</code></td>
<td>String</td>
<td>Product variant displayed on the product list.</td>
</tr>
<tr>
<td><code>products.[].price</code></td>
<td>Number</td>
<td>Price of the product displayed on the product list.</td>
</tr>
<tr>
<td><code>products.[].quantity</code></td>
<td>Number</td>
<td>Quantity of a product displayed on the product list.</td>
</tr>
<tr>
<td><code>products.[].coupon</code></td>
<td>String</td>
<td>Name or serial number of coupon code associated with product displayed on the product list.</td>
</tr>
<tr>
<td><code>products.[].position</code></td>
<td>Number</td>
<td>Product position in the product list (for example, <code>2</code>).</td>
</tr>
<tr>
<td><code>checkout_id</code></td>
<td>String</td>
<td>Checkout ID.</td>
</tr>
<tr>
<td><code>order_id</code></td>
<td>String</td>
<td>Internal ID of order/transaction/purchase.</td>
</tr>
<tr>
<td><code>affiliation</code></td>
<td>String</td>
<td>Name of affiliate from which the order occurred.</td>
</tr>
<tr>
<td><code>total</code></td>
<td>Number</td>
<td>Revenue with discounts and coupons added in.</td>
</tr>
<tr>
<td><code>revenue</code></td>
<td>Number</td>
<td>Revenue excluding shipping and tax.</td>
</tr>
<tr>
<td><code>shipping</code></td>
<td>Number</td>
<td>Cost of shipping for transaction.</td>
</tr>
<tr>
<td><code>tax</code></td>
<td>Number</td>
<td>Total tax for transaction.</td>
</tr>
<tr>
<td><code>discount</code></td>
<td>Number</td>
<td>Total discount for transaction.</td>
</tr>
<tr>
<td><code>coupon</code></td>
<td>String</td>
<td>Name or serial number of coupon redeemed on the transaction-level.</td>
</tr>
<tr>
<td><code>currency</code></td>
<td>String</td>
<td>Currency code for the transaction.</td>
</tr>
<tr>
<td><code>value</code></td>
<td>Number</td>
<td>Total value of the product after quantity.</td>
</tr>
<tr>
<td><code>creative</code></td>
<td>String</td>
<td>Label for creative asset of promotion being tracked.</td>
</tr>
<tr>
<td><code>query</code></td>
<td>String</td>
<td>Product search term.</td>
</tr>
<tr>
<td><code>step</code></td>
<td>Number</td>
<td>The Number of the checkout step in the checkout process.</td>
</tr>
<tr>
<td><code>payment_type</code></td>
<td>String</td>
<td>The type of payment used.</td>
</tr>
</tbody>
</table>
<h2 id="event-code-examples">Event code examples</h2>
<h3 id="product-viewed">Product viewed</h3>
<pre><code class="language-js">zaraz.ecommerce(&quot;Product Viewed&quot;, {&#10;	product_id: &quot;999555321&quot;,&#10;	sku: &quot;2671033&quot;,&#10;	category: &quot;T-shirts&quot;,&#10;	name: &quot;V-neck T-shirt&quot;,&#10;	brand: &quot;Cool Brand&quot;,&#10;	variant: &quot;White&quot;,&#10;	price: 14.99,&#10;	currency: &quot;usd&quot;,&#10;	value: 18.99,&#10;});&#10;</code></pre>
<h3 id="product-list-viewed">Product List Viewed</h3>
<pre><code class="language-js">zaraz.ecommerce(&quot;Product List Viewed&quot;, {&#10;	products: [&#10;		{&#10;			product_id: &quot;999555321&quot;,&#10;			sku: &quot;2671033&quot;,&#10;			category: &quot;T-shirts&quot;,&#10;			name: &quot;V-neck T-shirt&quot;,&#10;			brand: &quot;Cool Brand&quot;,&#10;			variant: &quot;White&quot;,&#10;			price: 14.99,&#10;			currency: &quot;usd&quot;,&#10;			value: 18.99,&#10;			position: 1,&#10;		},&#10;		{&#10;			product_id: &quot;999555322&quot;,&#10;			sku: &quot;2671034&quot;,&#10;			category: &quot;T-shirts&quot;,&#10;			name: &quot;T-shirt&quot;,&#10;			brand: &quot;Cool Brand&quot;,&#10;			variant: &quot;Pink&quot;,&#10;			price: 10.99,&#10;			currency: &quot;usd&quot;,&#10;			value: 16.99,&#10;			position: 2,&#10;		},&#10;	],&#10;});&#10;</code></pre>
<h3 id="product-added">Product added</h3>
<pre><code class="language-js">zaraz.ecommerce(&quot;Product Added&quot;, {&#10;	product_id: &quot;999555321&quot;,&#10;	sku: &quot;2671033&quot;,&#10;	category: &quot;T-shirts&quot;,&#10;	name: &quot;V-neck T-shirt&quot;,&#10;	brand: &quot;Cool Brand&quot;,&#10;	variant: &quot;White&quot;,&#10;	price: 14.99,&#10;	currency: &quot;usd&quot;,&#10;	quantity: 1,&#10;	coupon: &quot;SUMMER-SALE&quot;,&#10;	position: 2,&#10;});&#10;</code></pre>
<h3 id="checkout-step-viewed">Checkout Step Viewed</h3>
<pre><code class="language-js">zaraz.ecommerce(&quot;Checkout Step Viewed&quot;, {&#10;	step: 1,&#10;});&#10;</code></pre>
<h3 id="order-completed">Order completed</h3>
<pre><code class="language-js">zaraz.ecommerce(&quot;Order Completed&quot;, {&#10;	checkout_id: &quot;616727740&quot;,&#10;	order_id: &quot;817286897056801&quot;,&#10;	affiliation: &quot;affiliate.com&quot;,&#10;	total: 30.0,&#10;	revenue: 20.0,&#10;	shipping: 3,&#10;	tax: 2,&#10;	discount: 5,&#10;	coupon: &quot;winter-sale&quot;,&#10;	currency: &quot;USD&quot;,&#10;	products: [&#10;		{&#10;			product_id: &quot;999666321&quot;,&#10;			sku: &quot;8251511&quot;,&#10;			name: &quot;Boy’s shorts&quot;,&#10;			price: 10,&#10;			quantity: 2,&#10;			category: &quot;shorts&quot;,&#10;		},&#10;		{&#10;			product_id: &quot;742566131&quot;,&#10;			sku: &quot;7251567&quot;,&#10;			name: &quot;Blank T-shirt&quot;,&#10;			price: 5,&#10;			quantity: 2,&#10;			category: &quot;T-shirts&quot;,&#10;		},&#10;	],&#10;});&#10;</code></pre>
