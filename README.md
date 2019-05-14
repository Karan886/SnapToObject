<h1>Snap To Object Add-On</h1>
<p>
This project is a small tool made for a <em>3D art and animation</em> suite called <em><b>"Blender"</b></em>.
</p>
<p>
Imagine a scenario where you are an artist working on multiple 3D models that need to be organized along the <em><b>x, y, or z</b></em> axis in the final scene. ie. designing a <em>small city block</em> may require organizing 3 or 4 <em>building models</em> along the <em><b>x axis</b></em>. This <em>tool</em> eases an artist's job by <em><b>"snapping"</em></b> selected meshes together - that is, properly stacking them along the specified axis. Currently, this tool works for every <em><b>two selected meshes</b></em>(so you cannot stack more than two meshes at a time). The last selected mesh will maintain its location in <em>3D space</em>, while the first selected mesh will be pulled towards it. Additionally, this tool allows some room for flexibility by allowing artists to add <em><b>offset values</b></em>. For example, when each building in the city block have some space between them, you can stack them with some offset between them.
</p>

<hr/>

<h2>Demos</h2> 
<b><a href="https://drive.google.com/open?id=1XZWzhMYMYe8kgVR4VJOxroGvKPBnxYR-">First look at the tool</a></b>

<hr/>

<h2>Main Issues</h2>
<ol>
<li>
To implement this tool to work on more than two meshes at a time, we need to know the order in which the artist selected 
those meshes in the first place. This information is not available with the blender python API - (looking into implementing a 
sub-tool for this, if possible).
</li>
</ol>
