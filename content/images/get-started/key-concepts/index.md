<p>Here is a summary of the key terms that we use throughout our guides.</p>
<table>
<thead>
<tr>
<th>Term</th>
<th>What this means</th>
</tr>
</thead>
<tbody>
<tr>
<td>Remote image</td>
<td>An image that is stored outside of Images storage, including images in <a href="/r2/">R2</a>.</td>
</tr>
<tr>
<td>Transformation</td>
<td>A request to optimize a remote image that is stored outside of Images.</td>
</tr>
<tr>
<td>Origin</td>
<td><p>The location where your image is stored.</p><p>When you optimize a remote image, Cloudflare will pull the original image from the origin and store it in cache.</p></td>
</tr>
<tr>
<td>Hosted image</td>
<td><p>An image that is stored in Images.</p><p>Cloudflare dynamically serves copies of your original image, optimized based on your requirements.</p></td>
</tr>
<tr>
<td>Parameter / Option</td>
<td><p>A parameter is a type of optimization that you can perform on an image.</p><p>An option is the value for the parameter.</p><p>For example, you can set the <code>width</code> parameter to a value of <code>100</code> to resize an image to a width of 100.</p></td>
</tr>
<tr>
<td>Variant</td>
<td><p>A predefined way to specify how a hosted image should be resized.</p><p>For example, you can create a variant called &quot;thumbnail&quot; that sets image dimensions to 100x100.</p><p>When you serve images with this variant, Cloudflare will serve a version of the original image that is resized to 100x100.</p><p>Predefined variants specify a limited set of parameters: <code>width</code>, <code>height</code>, <code>fit</code>, and <code>blur</code>.</p></td>
</tr>
</tbody>
</table>
