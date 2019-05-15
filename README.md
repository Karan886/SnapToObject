<h1>Snap To Object Add-On</h1>
<p>
This project is a small tool made for a <em>3D art and animation</em> suite called <cite><a href="https://www.blender.org"><b>"Blender 3D"</b></a></cite>.
</p>
<ul>
<li>
Imagine a scenario where you are an artist working on multiple 3D models that need to be organized along the <em><b>x, y, or z</b></em> axis in the final scene. ie. designing a <em>small city block</em> may require organizing 3 or 4 <em>building models</em> along the <em><b>x axis</b></em>. 
</li>
<li>
The <em>tool</em> eases an artist's job by <em><b>"snapping"</em></b> selected meshes together - that is, properly stacking them along the specified axis. Currently, this tool works for every <em><b>two selected meshes</b></em>(so you cannot stack more than two meshes at a time). The last selected mesh will maintain its location in <em>3D space</em>, while the first selected mesh will be pulled towards it. 
</li>
<li>
The tool allows some room for flexibility by allowing artists to add <em><b>offset values</b></em>. For example, when each building in the city block have some space between them, you can stack them with some offset between them.
</li>
</ul>

<hr/>

<h2>Demos</h2> 
<b><a href="https://drive.google.com/open?id=1XZWzhMYMYe8kgVR4VJOxroGvKPBnxYR-">First look at the tool</a></b>

<hr/>

<h2>Other Issues</h2>
<ul>
<li>
To implement this tool to work on more than two meshes at a time, we need to know the order in which the artist selected 
those meshes in the first place. This information is not available with the <cite><a href="https://docs.blender.org/api/2.79/"><b>Blender Python API</b></a></cite> - (looking into implementing a 
sub-tool for this, if possible).
</li>
</ul>

<hr/>

<h2>Testing</h2>
<ol>
<li>Download <cite><a href="https://www.blender.org/download/"><b>Blender 3D</b></a></cite>, if you haven't done already</li>
<li>
Clone the repository or download the file <cite><a href="https://github.com/Karan886/Blender-SnapToObject-AddOn/blob/master/SnapToObject-Tool/MeshAlign.py"><b>MeshAlign.py</b></a></cite> which can be found <cite><a href="https://github.com/Karan886/Blender-SnapToObject-AddOn/tree/master/SnapToObject-Tool"><b>here</b></a></cite>
</li>
<li>
Open a new project and create a text editor window in the viewport, if you don't know how to do this you can check out <cite><a href="https://www.blender.org/support/tutorials/"><b>free tutorials</b></a></cite> on the <cite><a href="https://www.blender.org"><b>website</b></a></cite>
</li>
<li>Upload the .py file and run the script</li>
<li>Once the script runs successfully, you can shift select any two object on the <em><b>3D viewport</b></em></li>
<li>Press space bar to bring up search menu and look for <em><b>"Snap To Object"</b></em></li>
<li>You can check out the <strong>Demo</strong> section of this document for assistance</li>
</ol>
