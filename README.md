chartapi
========

# Introduction

This is a web chart api backed by graph engines to render code to images over the air.

The following two engines are supported by the time:

* graphviz (flow chart)
* mscgen (sequence chart)

# API

The chart api only accepts valid http GET requests. The following parameters are supported.

* engine: specifiy 'dot' or 'mscgen';
* code: specify valid code block here;
* action: specifiy 'geterrormsg' to redirect to the error message page, otherwise to redirect to url of image.

# Auxiliaries

* /examples/: gallery page with example code and images;
* /playground/: an interactive editor rendering code to image on the fly. Embedding HTML code block is generated as well.

# Examples

* (http://chartapi.dinghaifeng.me:8000/api/)
* (http://chartapi.dinghaifeng.me:8000/playground/)
* (http://chartapi.dinghaifeng.me:8000/examples/)
