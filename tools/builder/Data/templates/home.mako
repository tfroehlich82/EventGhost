<%inherit file="layout.mako"/>\
<%def name="title()">EventGhost</%def>
<%def name="content_rst()" buffered="True"> 
.. image:: /images/screenshot.jpg
   :align: right

What is EventGhost?
~~~~~~~~~~~~~~~~~~~

EventGhost is an advanced, easy to use and extensible automation tool for 
MS Windows. It can use different input devices like infrared or
wireless remote controls to trigger macros, that on their part control a
computer and its attached hardware. So it can be used to control a Media-PC with 
a normal consumer remote. But its possible uses go much beyond this.


Download
~~~~~~~~

EventGhost runs on Microsoft Windows 2000/XP/Vista. You can get EventGhost from 
the `download page </downloads/>`_.


License
~~~~~~~

EventGhost is released under the `GNU GPL, version 2 
<http://www.gnu.org/licenses/old-licenses/gpl-2.0.html>`_.
So EventGhost is open source software. You can get and use it without charge.


Support
~~~~~~~

* `Documentation </docs/>`_
* `Wiki </wiki/>`_
* `Forum </forum/>`_
</%def>
${rst2html(self.content_rst())}