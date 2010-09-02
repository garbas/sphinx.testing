`Sphinx`_ is one freaking great tool to write documentation. Not just python
documentation, all kinds of documentation. And there is a big reason why to
write documentation in `Sphinx`_. You can write code which will be nicely
formated for you with all the shines. 

.. contents

What happens if you want to test your documentation?
----------------------------------------------------

Well not much. There is a build-in plugin `sphinx.ext.docstest`_ which enables
you to do some testing, but is limited to only python. And how to test all that
console commands? Using python? I am pythonista, but testing console commands
with ptyhon os.system or similar sounds wrong and anybody doing this will burn
in hell anyway.

So here is where `sphinx.testing` comes in. It will use all those `..
code-block:: ` and `.. sourcecode::` blocks you have laying around in your
documentation and run them for you, optionaly if you want it ofcourse. For now
we only support python and console type of blocks, but its easy to extend and
provide general test runner for any language that is actually supported by `..
code-block:`, which is basicaly what `Pygments`_ support (`list of lexers`_).


TODO:  write how to use it

Credits
=======

 * `Rok Garbas`_, author

 * `Manuel`_, for inspiration and all the documentation i borrowed and implement it to be more tightly integrated with sphinx.
 * `plone.testing`_, for pusing me to do this. once you taste the sweetness of layers you want to use them anywhere 
 * `mrsd`_, to be first package to use this SphinxTestSuite

Todo
====

 * support for python and "python cosole" aka doctests


Changelog
=========

0.1 - 2010-09-01
----------------

 * support for shell console code-block testing
 * initial release


.. _`Sphinx`: http://sphinx.pocoo.org
.. _`sphinx.ext.doctest`: http://sphinx.pocoo.org/ext/doctest.html
.. _`Rok Garbas`: http://www.garbas.si
.. _`plone.testing`: http://pypi.python.org/pypi/plone.testing
.. _`mrsd`: http://pypi.python.org/pypi/mrsd
.. _`Manuel`: http://pypi.python.org/pypi/manuel
.. _`list of lexers`: http://pygments.org/docs/lexers
