
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Bottle: Python Web Framework &#8212; Bottle 0.13-dev documentation</title>
    <link rel="stylesheet" href="_static/bottle.css" type="text/css" />
    <link rel="stylesheet" href="_static/pygments.css" type="text/css" />
    <script type="text/javascript">
      var DOCUMENTATION_OPTIONS = {
        URL_ROOT:    './',
        VERSION:     '0.13-dev',
        COLLAPSE_INDEX: false,
        FILE_SUFFIX: '.html',
        HAS_SOURCE:  true,
        SOURCELINK_SUFFIX: '.txt'
      };
    </script>
    <script type="text/javascript" src="_static/jquery.js"></script>
    <script type="text/javascript" src="_static/underscore.js"></script>
    <script type="text/javascript" src="_static/doctools.js"></script>
    <link rel="shortcut icon" href="_static/favicon.ico"/>
    <link rel="index" title="Index" href="genindex.html" />
    <link rel="search" title="Search" href="search.html" />
    <link rel="next" title="Tutorial" href="tutorial.html" />
    <link rel="shortcut icon" type="image/x-icon" href="_static/favicon.ico" />
    <link rel="image_src" type="image/png" href="_static/logo_reddit.png" />
    <script type="application/javascript" src="_static/default.js"></script>
    <meta name="description" content="Bottle is a fast, simple and lightweight WSGI micro web-framework for Python." />
    
     

  </head>
  <body>  

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body" role="main">
            
  <div></div>
  
  <div class="section" id="bottle-python-web-framework">
<h1>Bottle: Python Web Framework<a class="headerlink" href="#bottle-python-web-framework" title="Permalink to this headline">¶</a></h1>
<p>Bottle is a fast, simple and lightweight <a class="reference external" href="http://www.wsgi.org/">WSGI</a> micro web-framework for <a class="reference external" href="http://python.org/">Python</a>. It is distributed as a single file module and has no dependencies other than the <a class="reference external" href="http://docs.python.org/library/">Python Standard Library</a>.</p>
<ul class="simple">
<li><strong>Routing:</strong> Requests to function-call mapping with support for clean and  dynamic URLs.</li>
<li><strong>Templates:</strong> Fast and pythonic <a class="reference internal" href="tutorial.html#tutorial-templates"><span class="std std-ref">built-in template engine</span></a> and support for <a class="reference external" href="http://www.makotemplates.org/">mako</a>, <a class="reference external" href="http://jinja.pocoo.org/">jinja2</a> and <a class="reference external" href="http://www.cheetahtemplate.org/">cheetah</a> templates.</li>
<li><strong>Utilities:</strong> Convenient access to form data, file uploads, cookies, headers and other HTTP-related metadata.</li>
<li><strong>Server:</strong> Built-in HTTP development server and support for <a class="reference external" href="http://pythonpaste.org/">paste</a>, <a class="reference external" href="https://github.com/jonashaag/bjoern">bjoern</a>, <a class="reference external" href="https://developers.google.com/appengine/">gae</a>, <a class="reference external" href="http://www.cherrypy.org/">cherrypy</a> or any other <a class="reference external" href="http://www.wsgi.org/">WSGI</a> capable HTTP server.</li>
</ul>
<p class="rubric">Example: “Hello World” in a bottle</p>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">bottle</span> <span class="kn">import</span> <span class="n">route</span><span class="p">,</span> <span class="n">run</span><span class="p">,</span> <span class="n">template</span>

<span class="nd">@route</span><span class="p">(</span><span class="s1">&#39;/hello/&lt;name&gt;&#39;</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">index</span><span class="p">(</span><span class="n">name</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">template</span><span class="p">(</span><span class="s1">&#39;&lt;b&gt;Hello {{name}}&lt;/b&gt;!&#39;</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">)</span>

<span class="n">run</span><span class="p">(</span><span class="n">host</span><span class="o">=</span><span class="s1">&#39;localhost&#39;</span><span class="p">,</span> <span class="n">port</span><span class="o">=</span><span class="mi">8080</span><span class="p">)</span>
</pre></div>
</div>
<p>Run this script or paste it into a Python console, then point your browser to <a class="reference external" href="http://localhost:8080/hello/world">http://localhost:8080/hello/world</a>. That’s it.</p>
<p class="rubric">Download and Install</p>
<p>Install the latest stable release with <code class="docutils literal"><span class="pre">pip</span> <span class="pre">install</span> <span class="pre">bottle</span></code> or download <a class="reference external" href="https://github.com/bottlepy/bottle/raw/master/bottle.py">bottle.py</a> (unstable) into your project directory. There are no hard <a class="footnote-reference" href="#id3" id="id2">[1]</a> dependencies other than the Python standard library. Bottle supports <strong>Python 2.7 and Python 3</strong>.</p>
<div class="deprecated">
<p><span class="versionmodified">Deprecated since version 0.13: </span>Support for Python 2.5 and 2.6 was dropped with this release.</p>
</div>
<div class="section" id="user-s-guide">
<h2>User’s Guide<a class="headerlink" href="#user-s-guide" title="Permalink to this headline">¶</a></h2>
<p>Start here if you want to learn how to use the bottle framework for web development. If you have any questions not answered here, feel free to ask the <a class="reference external" href="mailto:bottlepy&#37;&#52;&#48;googlegroups&#46;com">mailing list</a>.</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="tutorial.html">Tutorial</a><ul>
<li class="toctree-l2"><a class="reference internal" href="tutorial.html#installation">Installation</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial.html#quickstart-hello-world">Quickstart: “Hello World”</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial.html#request-routing">Request Routing</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial.html#generating-content">Generating content</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial.html#request-data">Request Data</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial.html#templates">Templates</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial.html#plugins">Plugins</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial.html#development">Development</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial.html#deployment">Deployment</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial.html#glossary">Glossary</a></li>
</ul>
</li>
<li class="toctree-l1"><a class="reference internal" href="configuration.html">Configuration (DRAFT)</a><ul>
<li class="toctree-l2"><a class="reference internal" href="configuration.html#configuration-basics">Configuration Basics</a></li>
<li class="toctree-l2"><a class="reference internal" href="configuration.html#naming-convention">Naming Convention</a></li>
<li class="toctree-l2"><a class="reference internal" href="configuration.html#loading-configuration-from-a-file">Loading Configuration from a File</a></li>
<li class="toctree-l2"><a class="reference internal" href="configuration.html#loading-configuration-from-a-python-module">Loading Configuration from a python module</a></li>
<li class="toctree-l2"><a class="reference internal" href="configuration.html#loading-configuration-from-a-nested-dict">Loading Configuration from a nested <code class="docutils literal"><span class="pre">dict</span></code></a></li>
<li class="toctree-l2"><a class="reference internal" href="configuration.html#listening-to-configuration-changes">Listening to configuration changes</a></li>
<li class="toctree-l2"><a class="reference internal" href="configuration.html#filters-and-other-meta-data">Filters and other Meta Data</a></li>
<li class="toctree-l2"><a class="reference internal" href="configuration.html#api-documentation">API Documentation</a></li>
</ul>
</li>
<li class="toctree-l1"><a class="reference internal" href="routing.html">Request Routing</a><ul>
<li class="toctree-l2"><a class="reference internal" href="routing.html#rule-syntax">Rule Syntax</a></li>
<li class="toctree-l2"><a class="reference internal" href="routing.html#wildcard-filters">Wildcard Filters</a></li>
<li class="toctree-l2"><a class="reference internal" href="routing.html#legacy-syntax">Legacy Syntax</a></li>
<li class="toctree-l2"><a class="reference internal" href="routing.html#explicit-routing-configuration">Explicit routing configuration</a></li>
</ul>
</li>
<li class="toctree-l1"><a class="reference internal" href="stpl.html">SimpleTemplate Engine</a><ul>
<li class="toctree-l2"><a class="reference internal" href="stpl.html#simpletemplate-syntax"><code class="docutils literal"><span class="pre">SimpleTemplate</span></code> Syntax</a></li>
<li class="toctree-l2"><a class="reference internal" href="stpl.html#template-functions">Template Functions</a></li>
<li class="toctree-l2"><a class="reference internal" href="stpl.html#simpletemplate-api"><code class="docutils literal"><span class="pre">SimpleTemplate</span></code> API</a></li>
</ul>
</li>
<li class="toctree-l1"><a class="reference internal" href="deployment.html">Deployment</a><ul>
<li class="toctree-l2"><a class="reference internal" href="deployment.html#server-options">Server Options</a></li>
<li class="toctree-l2"><a class="reference internal" href="deployment.html#switching-the-server-backend">Switching the Server Backend</a></li>
<li class="toctree-l2"><a class="reference internal" href="deployment.html#good-old-cgi">Good old CGI</a></li>
</ul>
</li>
<li class="toctree-l1"><a class="reference internal" href="api.html">API Reference</a><ul>
<li class="toctree-l2"><a class="reference internal" href="api.html#module-contents">Module Contents</a></li>
<li class="toctree-l2"><a class="reference internal" href="api.html#the-bottle-class">The <code class="docutils literal"><span class="pre">Bottle</span></code> Class</a></li>
<li class="toctree-l2"><a class="reference internal" href="api.html#the-request-object">The <code class="docutils literal"><span class="pre">Request</span></code> Object</a></li>
<li class="toctree-l2"><a class="reference internal" href="api.html#the-response-object">The <code class="docutils literal"><span class="pre">Response</span></code> Object</a></li>
<li class="toctree-l2"><a class="reference internal" href="api.html#templates">Templates</a></li>
</ul>
</li>
<li class="toctree-l1"><a class="reference internal" href="plugins/index.html">List of available Plugins</a></li>
</ul>
</div>
</div>
<div class="section" id="knowledge-base">
<h2>Knowledge Base<a class="headerlink" href="#knowledge-base" title="Permalink to this headline">¶</a></h2>
<p>A collection of articles, guides and HOWTOs.</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="tutorial_app.html">Tutorial: Todo-List Application</a><ul>
<li class="toctree-l2"><a class="reference internal" href="tutorial_app.html#goals">Goals</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial_app.html#before-we-start">Before We Start…</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial_app.html#using-bottle-for-a-web-based-todo-list">Using Bottle for a Web-Based ToDo List</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial_app.html#server-setup">Server Setup</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial_app.html#final-words">Final Words</a></li>
<li class="toctree-l2"><a class="reference internal" href="tutorial_app.html#complete-example-listing">Complete Example Listing</a></li>
</ul>
</li>
<li class="toctree-l1"><a class="reference internal" href="async.html">Primer to Asynchronous Applications</a><ul>
<li class="toctree-l2"><a class="reference internal" href="async.html#the-limits-of-synchronous-wsgi">The Limits of Synchronous WSGI</a></li>
<li class="toctree-l2"><a class="reference internal" href="async.html#greenlets-to-the-rescue">Greenlets to the rescue</a></li>
<li class="toctree-l2"><a class="reference internal" href="async.html#event-callbacks">Event Callbacks</a></li>
<li class="toctree-l2"><a class="reference internal" href="async.html#finally-websockets">Finally: WebSockets</a></li>
</ul>
</li>
<li class="toctree-l1"><a class="reference internal" href="recipes.html">Recipes</a><ul>
<li class="toctree-l2"><a class="reference internal" href="recipes.html#keeping-track-of-sessions">Keeping track of Sessions</a></li>
<li class="toctree-l2"><a class="reference internal" href="recipes.html#debugging-with-style-debugging-middleware">Debugging with Style: Debugging Middleware</a></li>
<li class="toctree-l2"><a class="reference internal" href="recipes.html#unit-testing-bottle-applications">Unit-Testing Bottle Applications</a></li>
<li class="toctree-l2"><a class="reference internal" href="recipes.html#functional-testing-bottle-applications">Functional Testing Bottle Applications</a></li>
<li class="toctree-l2"><a class="reference internal" href="recipes.html#embedding-other-wsgi-apps">Embedding other WSGI Apps</a></li>
<li class="toctree-l2"><a class="reference internal" href="recipes.html#ignore-trailing-slashes">Ignore trailing slashes</a></li>
<li class="toctree-l2"><a class="reference internal" href="recipes.html#keep-alive-requests">Keep-alive requests</a></li>
<li class="toctree-l2"><a class="reference internal" href="recipes.html#gzip-compression-in-bottle">Gzip Compression in Bottle</a></li>
<li class="toctree-l2"><a class="reference internal" href="recipes.html#using-the-hooks-plugin">Using the hooks plugin</a></li>
<li class="toctree-l2"><a class="reference internal" href="recipes.html#using-bottle-with-heroku">Using Bottle with Heroku</a></li>
</ul>
</li>
<li class="toctree-l1"><a class="reference internal" href="faq.html">Frequently Asked Questions</a><ul>
<li class="toctree-l2"><a class="reference internal" href="faq.html#about-bottle">About Bottle</a></li>
<li class="toctree-l2"><a class="reference internal" href="faq.html#common-problems-and-pitfalls">Common Problems and Pitfalls</a></li>
</ul>
</li>
</ul>
</div>
</div>
<div class="section" id="development-and-contribution">
<h2>Development and Contribution<a class="headerlink" href="#development-and-contribution" title="Permalink to this headline">¶</a></h2>
<p>These chapters are intended for developers interested in the bottle development and release workflow.</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="changelog.html">Release Notes and Changelog</a><ul>
<li class="toctree-l2"><a class="reference internal" href="changelog.html#release-0-13">Release 0.13</a></li>
<li class="toctree-l2"><a class="reference internal" href="changelog.html#release-0-12">Release 0.12</a></li>
<li class="toctree-l2"><a class="reference internal" href="changelog.html#release-0-11">Release 0.11</a></li>
<li class="toctree-l2"><a class="reference internal" href="changelog.html#release-0-10">Release 0.10</a></li>
<li class="toctree-l2"><a class="reference internal" href="changelog.html#release-0-9">Release 0.9</a></li>
<li class="toctree-l2"><a class="reference internal" href="changelog.html#release-0-8">Release 0.8</a></li>
</ul>
</li>
<li class="toctree-l1"><a class="reference internal" href="changelog.html#contributors">Contributors</a></li>
<li class="toctree-l1"><a class="reference internal" href="development.html">Developer Notes</a><ul>
<li class="toctree-l2"><a class="reference internal" href="development.html#get-involved">Get involved</a></li>
<li class="toctree-l2"><a class="reference internal" href="development.html#get-the-sources">Get the Sources</a></li>
<li class="toctree-l2"><a class="reference internal" href="development.html#releases-and-updates">Releases and Updates</a></li>
<li class="toctree-l2"><a class="reference internal" href="development.html#repository-structure">Repository Structure</a></li>
<li class="toctree-l2"><a class="reference internal" href="development.html#submitting-patches">Submitting Patches</a></li>
<li class="toctree-l2"><a class="reference internal" href="development.html#building-the-documentation">Building the Documentation</a></li>
<li class="toctree-l2"><a class="reference internal" href="development.html#git-workflow-examples">GIT Workflow Examples</a></li>
</ul>
</li>
<li class="toctree-l1"><a class="reference internal" href="plugindev.html">Plugin Development Guide</a><ul>
<li class="toctree-l2"><a class="reference internal" href="plugindev.html#how-plugins-work-the-basics">How Plugins Work: The Basics</a></li>
<li class="toctree-l2"><a class="reference internal" href="plugindev.html#plugin-api">Plugin API</a></li>
<li class="toctree-l2"><a class="reference internal" href="plugindev.html#the-route-context">The Route Context</a></li>
<li class="toctree-l2"><a class="reference internal" href="plugindev.html#runtime-optimizations">Runtime optimizations</a></li>
<li class="toctree-l2"><a class="reference internal" href="plugindev.html#plugin-example-sqliteplugin">Plugin Example: SQLitePlugin</a></li>
</ul>
</li>
</ul>
</div>
<div class="toctree-wrapper compound">
</div>
</div>
<div class="section" id="license">
<h2>License<a class="headerlink" href="#license" title="Permalink to this headline">¶</a></h2>
<p>Code and documentation are available according to the MIT License:</p>
<div class="highlight-python"><div class="highlight"><pre><span></span><span class="n">Copyright</span> <span class="p">(</span><span class="n">c</span><span class="p">)</span> <span class="mi">2009</span><span class="o">-</span><span class="mi">2018</span><span class="p">,</span> <span class="n">Marcel</span> <span class="n">Hellkamp</span><span class="o">.</span>

<span class="n">Permission</span> <span class="ow">is</span> <span class="n">hereby</span> <span class="n">granted</span><span class="p">,</span> <span class="n">free</span> <span class="n">of</span> <span class="n">charge</span><span class="p">,</span> <span class="n">to</span> <span class="nb">any</span> <span class="n">person</span> <span class="n">obtaining</span> <span class="n">a</span> <span class="n">copy</span>
<span class="n">of</span> <span class="n">this</span> <span class="n">software</span> <span class="ow">and</span> <span class="n">associated</span> <span class="n">documentation</span> <span class="n">files</span> <span class="p">(</span><span class="n">the</span> <span class="s2">&quot;Software&quot;</span><span class="p">),</span> <span class="n">to</span> <span class="n">deal</span>
<span class="ow">in</span> <span class="n">the</span> <span class="n">Software</span> <span class="n">without</span> <span class="n">restriction</span><span class="p">,</span> <span class="n">including</span> <span class="n">without</span> <span class="n">limitation</span> <span class="n">the</span> <span class="n">rights</span>
<span class="n">to</span> <span class="n">use</span><span class="p">,</span> <span class="n">copy</span><span class="p">,</span> <span class="n">modify</span><span class="p">,</span> <span class="n">merge</span><span class="p">,</span> <span class="n">publish</span><span class="p">,</span> <span class="n">distribute</span><span class="p">,</span> <span class="n">sublicense</span><span class="p">,</span> <span class="ow">and</span><span class="o">/</span><span class="ow">or</span> <span class="n">sell</span>
<span class="n">copies</span> <span class="n">of</span> <span class="n">the</span> <span class="n">Software</span><span class="p">,</span> <span class="ow">and</span> <span class="n">to</span> <span class="n">permit</span> <span class="n">persons</span> <span class="n">to</span> <span class="n">whom</span> <span class="n">the</span> <span class="n">Software</span> <span class="ow">is</span>
<span class="n">furnished</span> <span class="n">to</span> <span class="n">do</span> <span class="n">so</span><span class="p">,</span> <span class="n">subject</span> <span class="n">to</span> <span class="n">the</span> <span class="n">following</span> <span class="n">conditions</span><span class="p">:</span>

<span class="n">The</span> <span class="n">above</span> <span class="n">copyright</span> <span class="n">notice</span> <span class="ow">and</span> <span class="n">this</span> <span class="n">permission</span> <span class="n">notice</span> <span class="n">shall</span> <span class="n">be</span> <span class="n">included</span> <span class="ow">in</span>
<span class="nb">all</span> <span class="n">copies</span> <span class="ow">or</span> <span class="n">substantial</span> <span class="n">portions</span> <span class="n">of</span> <span class="n">the</span> <span class="n">Software</span><span class="o">.</span>

<span class="n">THE</span> <span class="n">SOFTWARE</span> <span class="n">IS</span> <span class="n">PROVIDED</span> <span class="s2">&quot;AS IS&quot;</span><span class="p">,</span> <span class="n">WITHOUT</span> <span class="n">WARRANTY</span> <span class="n">OF</span> <span class="n">ANY</span> <span class="n">KIND</span><span class="p">,</span> <span class="n">EXPRESS</span> <span class="n">OR</span>
<span class="n">IMPLIED</span><span class="p">,</span> <span class="n">INCLUDING</span> <span class="n">BUT</span> <span class="n">NOT</span> <span class="n">LIMITED</span> <span class="n">TO</span> <span class="n">THE</span> <span class="n">WARRANTIES</span> <span class="n">OF</span> <span class="n">MERCHANTABILITY</span><span class="p">,</span>
<span class="n">FITNESS</span> <span class="n">FOR</span> <span class="n">A</span> <span class="n">PARTICULAR</span> <span class="n">PURPOSE</span> <span class="n">AND</span> <span class="n">NONINFRINGEMENT</span><span class="o">.</span> <span class="n">IN</span> <span class="n">NO</span> <span class="n">EVENT</span> <span class="n">SHALL</span> <span class="n">THE</span>
<span class="n">AUTHORS</span> <span class="n">OR</span> <span class="n">COPYRIGHT</span> <span class="n">HOLDERS</span> <span class="n">BE</span> <span class="n">LIABLE</span> <span class="n">FOR</span> <span class="n">ANY</span> <span class="n">CLAIM</span><span class="p">,</span> <span class="n">DAMAGES</span> <span class="n">OR</span> <span class="n">OTHER</span>
<span class="n">LIABILITY</span><span class="p">,</span> <span class="n">WHETHER</span> <span class="n">IN</span> <span class="n">AN</span> <span class="n">ACTION</span> <span class="n">OF</span> <span class="n">CONTRACT</span><span class="p">,</span> <span class="n">TORT</span> <span class="n">OR</span> <span class="n">OTHERWISE</span><span class="p">,</span> <span class="n">ARISING</span> <span class="n">FROM</span><span class="p">,</span>
<span class="n">OUT</span> <span class="n">OF</span> <span class="n">OR</span> <span class="n">IN</span> <span class="n">CONNECTION</span> <span class="n">WITH</span> <span class="n">THE</span> <span class="n">SOFTWARE</span> <span class="n">OR</span> <span class="n">THE</span> <span class="n">USE</span> <span class="n">OR</span> <span class="n">OTHER</span> <span class="n">DEALINGS</span> <span class="n">IN</span>
<span class="n">THE</span> <span class="n">SOFTWARE</span><span class="o">.</span>
</pre></div>
</div>
<p>The Bottle logo however is <em>NOT</em> covered by that license. It is allowed to
use the logo as a link to the bottle homepage or in direct context with
the unmodified library. In all other cases please ask first.</p>
<p class="rubric">Footnotes</p>
<table class="docutils footnote" frame="void" id="id3" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id2">[1]</a></td><td>Usage of the template or server adapter classes requires the corresponding template or server modules.</td></tr>
</tbody>
</table>
</div>
</div>



          </div>
        </div>
      </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
            <p class="logo"><a href="#">
              <img class="logo" src="_static/logo_nav.png" alt="Logo"/>
            </a></p><p>
   Bottle is a fast, simple and lightweight WSGI micro web-framework for Python.
</p>
<h3>Installation</h3>
<p>Install Bottle with <code>pip&nbsp;install&nbsp;bottle</code> or download the source package at <a href="https://pypi.python.org/pypi/bottle">PyPI</a>.</p>
<h3>Releases</h3>
  
  <p style='font-size: 0.75em; color: darkred'><b>Warning:</b> This is a preview for <b>Bottle-0.13-dev</b>, which is
    not released yet. Switch to the latest <a href="/docs/stable/"><b>stable release</b></a>?</p>
  
<ul>
  
    
      <li><a href="/docs/dev/">Bottle dev</a> (development)</li>
  
  
    
      <li><a href="/docs/0.12/">Bottle 0.12</a> (stable)</li>
  
  
    
      <li><a href="/docs/0.11/">Bottle 0.11</a> (old stable)</li>
  
  
</ul>
<h3>Download Docs</h3>
  <p>Download this documentation as <a href="bottle-docs.pdf">PDF</a> or <a href="bottle-docs.zip">HTML (zip)</a> for offline use.</p>

<h3>Resources</h3>
<ul>
  <li><a target="_blank" href="https://twitter.com/bottlepy">Twitter news</a></li>
  <li><a target="_blank" href="http://blog.bottlepy.org">Development blog</a></li>
  <li><a target="_blank" href="https://github.com/bottlepy/bottle">GitHub repository</a></li>
  <li><a target="_blank" href="https://groups.google.de/group/bottlepy">Mailing list archive</a></li>
  <li><a target="_blank" href="https://webchat.freenode.net/?channels=bottlepy">Freenode chat</a></li>
</ul>

<h3>Like it?</h3>
<ul>
  <li>
    <form action="https://www.paypal.com/cgi-bin/webscr" method="post">
      <a href="https://flattr.com/thing/21888/Bottle-A-Python-Web-Framework" target="_blank">
        <img src="_static/flattr-badge-large.png" alt="Flattr this" title="Flattr this" border="0" />
      </a>

      <input type="hidden" name="cmd" value="_s-xclick">
      <input type="hidden" name="hosted_button_id" value="10013866">
      <input type="image" src="_static/paypal.png" border="0" name="submit" alt="Donate with PayPal!" style="vertical-align: top;">

    </form>
  </li>
</ul>
<h3>Hosted by:</h3>
<a href="http://www.webland.ro" target="_blank" title="Cloud VPS Servers">
    <img src="_static/banner_webland.png" alt="Cloud VPS Servers" />
</a> 
<div id="searchbox" style="display: none" role="search">
  <h3>Quick search</h3>
    <form class="search" action="search.html" method="get">
      <div><input type="text" name="q" /></div>
      <div><input type="submit" value="Go" /></div>
      <input type="hidden" name="check_keywords" value="yes" />
      <input type="hidden" name="area" value="default" />
    </form>
</div>
<script type="text/javascript">$('#searchbox').show(0);</script>
        </div>
      </div>
      <div class="clearer"></div>
    </div>
    <div class="footer">
    &copy; <a href="##license">Copyright</a> 2009-2021, Marcel Hellkamp - <a href="contact.html">Contact</a><br />
    Last updated on Apr 20, 2021. Created using <a href="http://sphinx.pocoo.org/">Sphinx</a> 1.6.7.<br />
    Powered by Bottle 0.13-dev
    </div>

  </body>
</html>