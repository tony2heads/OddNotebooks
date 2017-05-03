# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # A brief introductory tour of the IPython notebook (the screencast version)
# 
# This document will give you a brief tour of the capabilities of the IPython notebook.  
# You can view its contents by scrolling around, or execute each cell by typing `Shift-Enter`.
# 
# ## What is the ipython notebook?
# 
# At its most basic, the ipynb gives you a way to interactively edit & execute Python code in a Web notebook, and see the output.

# <codecell>

print 'hello, world!'

# <markdowncell>

# (You can also include text comments like this, as you may have noticed.)
# 
# The notebook runs Python in the normal manner -- nothing special needs to be done.  Just type in your Python code and hit Shift-Enter to run it.

# <codecell>

for i in range(5):
    print 'i is', i
    
import re
re.split('\d', 'the 1 is 2 for 3 foo')

# <markdowncell>

# The Python code is being executed on the computer running the ipython notebook - in this case, on an Amazon rental machine.
# 
# So that's neat, right?  But there's more...
# 
# # Plotting
# 
# You can also do interactive plotting, if you're into that kind of thing.

# <codecell>

x = linspace(0, 3*pi, 500)
plot(x, sin(x**2))
title('A simple chirp');

# <markdowncell>

# You can also paste blocks of input with prompt markers, such as those from
# [the official Python tutorial](http://docs.python.org/tutorial/interpreter.html#interactive-mode)

# <codecell>

>>> the_world_is_flat = 1
>>> if the_world_is_flat:
...     print "Be careful not to fall off!"

# <markdowncell>

# Errors are shown in informative ways:

# <codecell>

x = 1
y = 4
z = y/(1-x)

# <markdowncell>

# You can do tab completions, ask for help, and get details:

# <codecell>

open

# <markdowncell>

# (You can just click on the pane bar opened by '?' to close it again.)

# <markdowncell>

# ## See output as it's generated
# 
# If you execute the next cell, you will see the output arriving as it is generated, not all at the end.

# <codecell>

import time, sys
for i in range(8):
    print i,
    time.sleep(0.5)

# <markdowncell>

# ## Clean crash and restart
# 
# We call the low-level system libc.time routine with the wrong argument via
# ctypes to segfault the Python interpreter:

# <codecell>

from ctypes import CDLL
# This will crash a linux system; equivalent calls can be made on Windows or Mac
libc = CDLL("libc.so.6") 
libc.time(-1)  # BOOM!!

# <markdowncell>

# ## Markdown cells can contain formatted text and code
# 
# You can *italicize*, **boldface**
# 
# * build
# * lists
# 
# and embed code meant for illustration instead of execution in Python:
# 
#     def f(x):
#         """a docstring"""
#         return x**2
# 
# or other languages:
# 
#     if (i=0; i<n; i++) {
#       printf("hello %d\n", i);
#       x += 4;
#     }

# <markdowncell>

# Courtesy of MathJax, you can include mathematical expressions both inline: 
# $e^{i\pi} + 1 = 0$  and displayed:
# 
# $$e^x=\sum_{i=0}^\infty \frac{1}{i!}x^i$$

# <markdowncell>

# # More advanced features

# <markdowncell>

# Note that you are in the IPython shell, so if you know IPython you can use all the commands you're used to,
# including things like shell aliases and magic commands:

# <codecell>

pwd

# <codecell>

%run non_existent_file

# <codecell>

ls

# <codecell>

message = 'The IPython notebook is great!'
# note: the echo command does not run on Windows, it's a unix command.
!echo $message

# <markdowncell>

# ## Rich displays: include anything a browser can show
# 
# ### Images

# <markdowncell>

# An image can be displayed inline from a file, from raw data, or from a url:

# <codecell>

from IPython.core.display import Image
Image('http://python.org/images/python-logo.gif')

# <markdowncell>

# SVG images are also supported out of the box (since modern browsers do a good job of rendering them):

# <codecell>

from IPython.core.display import SVG
SVG(filename='python-logo.svg')

# <markdowncell>

# ### Video

# <markdowncell>

# And more exotic objects can also be displayed, as long as their representation supports 
# the IPython display protocol.
# 
# For example, videos hosted externally on YouTube are easy to load (and writing a similar wrapper for other
# hosted content is trivial):

# <codecell>

from IPython.lib.display import YouTubeVideo
# a talk about IPython at Sage Days at U. Washington, Seattle.
# Video credit: William Stein.
YouTubeVideo('1j_HxD4iLn8')

# <markdowncell>

# Using the nascent video capabilities of modern browsers, you may also be able to display local
# videos.  At the moment this doesn't work very well in all browsers, so it may or may not work for you;
# we will continue testing this and looking for ways to make it more robust.  
# 
# The following cell loads a local file called  `animation.m4v`, encodes the raw video as base64 for http
# transport, and uses the HTML5 video tag to load it. On Chrome 15 it works correctly, displaying a control
# bar at the bottom with a play/pause button and a location slider.

# <codecell>

from IPython.core.display import HTML
video = open("animation.m4v", "rb").read()
video_encoded = video.encode("base64")
video_tag = '<video controls alt="test" src="data:video/x-m4v;base64,{0}">'.format(video_encoded)
HTML(data=video_tag)

# <markdowncell>

# ## Local Files
# 
# The above examples embed images and video from the notebook filesystem in the output
# areas of code cells.  It is also possible to request these files directly in markdown cells
# if they reside in the notebook directory via relative urls prefixed with `files/`:
# 
#     files/[subdirectory/]<filename>
# 
# 
# For example, in the example notebook folder, we have the Python logo, addressed as:
# 
#     <img src="files/python-logo.svg" />
# 
# <img src="/files/python-logo.svg" />
# 
# and a video with the HTML5 video tag:
# 
#     <video controls src="files/animation.m4v" />
# 
# <video controls src="/files/animation.m4v" />
# 
# These do not embed the data into the notebook file,
# and require that the files exist when you are viewing the notebook.

# <markdowncell>

# ### External sites
# 
# You can even embed an entire page from another site in an iframe; for example this is today's Wikipedia
# page for mobile users:

# <codecell>

HTML('<iframe src=http://en.mobile.wikipedia.org/?useformat=mobile width=700 height=350>')

# <markdowncell>

# ### Mathematics
# 
# And we also support the display of mathematical expressions typeset in LaTeX, which is rendered
# in the browser thanks to the [MathJax library](http://mathjax.org).  
# 
# Note that this is *different* from the above examples.  Above we were typing mathematical expressions
# in Markdown cells (along with normal text) and letting the browser render them; now we are displaying
# the output of a Python computation as a LaTeX expression wrapped by the `Math()` object so the browser
# renders it.  The `Math` object will add the needed LaTeX delimiters (`$$`) if they are not provided:

# <codecell>

from IPython.core.display import Math
Math(r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx')

# <markdowncell>

# With the `Latex` class, you have to include the delimiters yourself.  This allows you to use other LaTeX modes such as `eqnarray`:

# <codecell>

from IPython.core.display import Latex
Latex(r"""\begin{eqnarray}
\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\
\nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
\nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
\nabla \cdot \vec{\mathbf{B}} & = 0 
\end{eqnarray}""")

# <markdowncell>

# # SymPy: Open Source Symbolic Mathematics
# 
# This notebook uses the [SymPy](http://sympy.org) package to perform symbolic manipulations,
# and combined with numpy and matplotlib, also displays numerical visualizations of symbolically
# constructed expressions.
# 
# We first load sympy with pretty-print support, and define some symbols:

# <codecell>

%load_ext sympyprinting

from __future__ import division
import sympy as sym
from sympy import *
x, y, z = symbols("x y z")

# <codecell>

Rational(3,2)*pi + exp(I*x) / (x**2 + y)

# <markdowncell>

# # Loading external codes
# * Drag and drop a ``.py`` in the dashboard
# * Use ``%loadpy`` with any local or remote url: [the Matplotlib Gallery!](http://matplotlib.sourceforge.net/gallery.html)
# 
# In this notebook we've kept the output saved so you can see the result, but you should run the next
# cell yourself (with an active internet connection).

# <codecell>

%loadpy http://matplotlib.sourceforge.net/mpl_examples/pylab_examples/integral_demo.py

# <codecell>


