
""" 
  *The example below illustrate the simple table
  
  .. note::
	This Documentation is created by M.Faisal Junaid Butt.
	
	
====================  ==========  ==========
Header row, column 1  Header 2    Header 3
====================  ==========  ==========
body row 1, column 1  column 2    column 3
body row 2            Cells may span columns
====================  ======================


--long		opt
			and long desc
			
			
			
			
InLine Markups
===============
  
	*emphasis*
	
	**Strong Emphasis**
	
	'interpreted text'
	
	''inline literal''
	
	\*escape*, \**escape**
	
	\A backlash literal: \\
	
	
=====	
Title
=====

Subtitle
--------

The First Para graph

The Second Paragraph

Lists
=====

- Enumerated Lists
- Bullet Lists
- Definition Lists
- option Lists

===============
Enumerated List
===============

	3. The First Item
	4. The Second Item
	#. The Third Item
	
===========
Bullet List
===========

	This is Item one
	----------------
	This is Item two
	----------------
	"-", "*" or "+".
	----------------
	continuing text must be aligned	  
	  
	
	Two Blank lines will be required

===============	 
Definition List
===============

	Python
		Python is a 
		programming language.
		
	reStructuredText
		reStructuredText is a
		markup syntax and parser
		system.
		
Blocks
======

	* Literal Blocks
	* Line Blocks
	* Block Quote
	* Doctest Block
	
Literal Block
=============
	A Literal Block: ::
	  
	  Everything will be
	  kept here.
	  
	Out of the literal block.
	
	A Literal Block: ::
	
	  Everything will be
	  kept here.
		
	Out of the literal block
	
Line Block
==========
	| 	Line Breaks and 
	|		initial indents
	|	are preserved
	
Block Quote
===========

	Block Quote are just:
		Indented Paragraph.
	

Explicit Markups
================

.. warning::
	This Documentation is created by M.Faisal Junaid Butt. 


**Footnotes**:
	- Numerical Footnote
	- Symbol Footnote
			
Numerical Footnote
==================

.. note::
	This Documentation is created by M.Faisal Junaid Butt.

PyHUG [1]_ and Taipei.py [2]_ are both the Python
user groups in Taiwan.
	.. [1] http://www.meetup.com/pythonhug/
	.. [2] http://taipei.python.org.tw/



PyHUG [#]_ and Taipei.py [#]_ are both the Python
user groups in Taiwan.
	.. [#] http://www.meetup.com/pythonhug/
	.. [#] http://taipei.python.org.tw/



Symbol Footnote
===============

.. note::
	This Documentation is created by M.Faisal Junaid Butt.
	
PyHUG [*]_ and Taipei.py [*]_ are both the Python
user groups in Taiwan.
	.. [*] http://www.meetup.com/pythonhug/
	.. [*] http://taipei.python.org.tw/


Citation
========

.. note::
	This Documentation is created by M.Faisal Junaid Butt.
	
[PyHUG]_ and [Taipei.py]_ are both the Python user groups in Taiwan.
	..  [Taipei.py] http://taipei.python.org.tw/
	
	

Hyperlink Targets
=================
	- External
	- Internal
	- Indirect
	- Implicit
	
External HyperLink Target
=========================

	[external-hyperlink]_ and [internal-hyperlink]_ are both the `Python <http://python.org/>`_ user groups in Taiwan.
		
	


Internal HyperLink Target
=========================

	- The Internal HyperLink Target are given below
		.. see also:: 
		    Internal HyperLink Target
		
	.. note::
		This Documentation is created by M.Faisal Junaid Butt.
	
	PyHUG_ and Taipei.py_ are both the Python user groups in Taiwan.
.. _PyHUG:
	PyHUG is ...


.. _Taipei.py:
	Taipei.py is ...
	
	
Comment
=======

	PyHUG and Taipei.py are both the Python user groups
	in Taiwan.
.. This is comment: Put Tainan.py in this paragraph.
	
	
	

**Images**:
	- Screen Shots can be added in the documentation
	- Logo can be added to the documentation
	* The Example is given below
	
	.. image:: _static\code.jpg


	..  [PyHUG] Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
	
"""


