<p>By default, all users are on the Images Free plan. The Free plan includes access to the transformations feature, which lets you optimize images stored outside of Images, like in <a href="/r2/">R2</a>.</p>
<p>The Paid plan allows transformations, as well as access to storage in Images.</p>
<p>Pricing is dependent on which features you use. The table below shows which metrics are used for each use case.</p>
<table>
<thead>
<tr>
<th>Use case</th>
<th>Metrics</th>
<th>Availability</th>
</tr>
</thead>
<tbody>
<tr>
<td>Optimize images stored outside of Images</td>
<td>Images Transformed</td>
<td>Free and Paid plans</td>
</tr>
<tr>
<td>Optimize images that are stored in Cloudflare Images</td>
<td>Images Stored, Images Delivered</td>
<td>Only Paid plans</td>
</tr>
</tbody>
</table>
<h2 id="images-free">Images Free</h2>
<p>On the Free plan, you can request up to 5,000 unique transformations each month for free.</p>
<p>Once you exceed 5,000 unique transformations:</p>
<ul>
<li>Existing transformations in cache will continue to be served as expected.</li>
<li>New transformations will return a <code>9422</code> error. If your source image is from the same domain where the transformation is served, then you can use the <a href="/images/optimization/features/#onerror"><code>onerror</code> parameter</a> to redirect to the original image.</li>
<li>You will not be charged for exceeding the limits in the Free plan.</li>
</ul>
<p>To request more than 5,000 unique transformations each month, you can purchase an Images Paid plan.</p>
<h2 id="images-paid">Images Paid</h2>
<p>When you purchase an Images Paid plan, you can choose your own storage or add storage in Images.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Pricing</th>
</tr>
</thead>
<tbody>
<tr>
<td>Images Transformed</td>
<td>First 5,000 unique transformations included + $0.50 / 1,000 unique transformations / month</td>
</tr>
<tr>
<td>Images Stored</td>
<td>$5 / 100,000 images stored / month</td>
</tr>
<tr>
<td>Images Delivered</td>
<td>$1 / 100,000 images delivered / month</td>
</tr>
</tbody>
</table>
<p>If you optimize an image stored outside of Images, then you will be billed only for Images Transformed.</p>
<p>Images Stored and Images Delivered apply only to images that are stored in your Images bucket. When you optimize a hosted image through the image delivery URL, then this counts toward Images Delivered — not Images Transformed. However, if you optimize a hosted image through the Images binding, then this counts toward Images Transformed.</p>
<h2 id="metrics">Metrics</h2>
<h3 id="images-transformed">Images Transformed</h3>
<p>A unique transformation is a request to transform an original image based on a set of <a href="/images/optimization/features/">supported parameters</a>. This metric is used when using the <a href="/images/optimization/binding/">Images binding</a> or optimizing images that are stored outside of Images.</p>
<p>For example, if you transform <code>thumbnail.jpg</code> as 100x100, then this counts as one unique transformation. If you transform the same <code>thumbnail.jpg</code> as 200x200, then this counts as a separate unique transformation.</p>
<p>You are billed on the number of unique transformations that are requested within each calendar month. Repeat requests for the same transformation within the same month are counted only once for that month. Calls to the Images binding's <a href="/images/optimization/binding/#infostream"><code>.info()</code></a> method are not billed.</p>
<p>The <code>format</code> parameter counts as only one billable transformation, even if multiple copies of an image are served. In other words, if <code>width=100,format=auto/thumbnail.jpg</code> is served to some users as AVIF and to others as WebP, then this counts as one unique transformation instead of two.</p>
<h4 id="example-1">Example #1</h4>
<p>If you serve 2,000 remote images in five different sizes each month, then this results in 10,000 unique transformations. Your estimated cost for the month would be:</p>
<table>
<thead>
<tr>
<th></th>
<th>Usage</th>
<th>Included</th>
<th>Billable quantity</th>
<th>Price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Transformations</td>
<td>10,000 unique transformations <sup><a href="#footnote-5">5</a></sup></td>
<td>5,000</td>
<td>5,000</td>
<td>$2.50 <sup><a href="#footnote-6">6</a></sup></td>
</tr>
</tbody>
</table>
<h4 id="example-2">Example #2</h4>
<p>If you use <a href="/r2/">R2</a> for storage then your estimated monthly costs will be the sum of your monthly Images costs and monthly <a href="/r2/pricing/#storage-usage">R2 costs</a>.</p>
<p>For example, if you upload 5,000 images to R2 with an average size of 5 MB, and serve 2,000 of those images in five different sizes, then your estimated cost for the month would be:</p>
<table>
<thead>
<tr>
<th></th>
<th>Usage</th>
<th>Included</th>
<th>Billable quantity</th>
<th>Price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Storage</td>
<td>25 GB <sup><a href="#footnote-1">1</a></sup></td>
<td>10 GB</td>
<td>15 GB</td>
<td>$0.22 <sup><a href="#footnote-7">7</a></sup></td>
</tr>
<tr>
<td>Class A operations</td>
<td>5,000 writes <sup><a href="#footnote-2">2</a></sup></td>
<td>1 million</td>
<td>0</td>
<td>$0.00 <sup><a href="#footnote-8">8</a></sup></td>
</tr>
<tr>
<td>Class B operations</td>
<td>10,000 reads <sup><a href="#footnote-3">3</a></sup></td>
<td>10 million</td>
<td>0</td>
<td>$0.00 <sup><a href="#footnote-9">9</a></sup></td>
</tr>
<tr>
<td>Transformations</td>
<td>10,000 unique transformations <sup><a href="#footnote-4">4</a></sup></td>
<td>5,000</td>
<td>5,000</td>
<td>$2.50 <sup><a href="#footnote-10">10</a></sup></td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$2.72</strong></td>
</tr>
</tbody>
</table>
<h3 id="images-stored">Images Stored</h3>
<p>Storage in Images is available only with an Images Paid plan. You can purchase storage in increments of $5 for every 100,000 images stored per month.</p>
<p>You can create predefined variants to specify how an image should be resized, such as <code>thumbnail</code> as 100x100 and <code>hero</code> as 1600x500.</p>
<p>Only uploaded images count toward Images Stored; defining variants will not impact your storage limit.</p>
<h3 id="images-delivered">Images Delivered</h3>
<p>For images that are stored in Images, you will incur $1 for every 100,000 images delivered per month. This metric does not include transformed images that are stored in remote sources.</p>
<p>Every image requested by the browser counts as one billable request.</p>
<h4 id="example">Example</h4>
<p>A retail website has a product page that uses Images to serve 10 images. If the page was visited 10,000 times this month, then this results in 100,000 images delivered — or $1.00 in billable usage.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">5,000 objects × 5 MB per object</li>
<li id="footnote-2">5,000 objects × 1 write per object</li>
<li id="footnote-3">2,000 objects × 5 reads per object</li>
<li id="footnote-4">2,000 original images × 5 sizes</li>
<li id="footnote-5">2,000 original images × 5 sizes</li>
<li id="footnote-6">(5,000 transformations / 1,000) × $0.50</li>
<li id="footnote-7">15 GB × $0.015 / GB-month</li>
<li id="footnote-8">0 × $4.50 / million requests</li>
<li id="footnote-9">0 × $0.36 / million requests</li>
<li id="footnote-10">(5,000 transformations / 1,000) × $0.50</li></ol></section>
