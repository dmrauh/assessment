assessment
==========

assessment helps the stressed research assistant by calculating the final grade
of theses, according to sub grades which are weighted by sections. The whole
grade calculation is done as defined in the [evaluation
sheet](https://git.rz.uni-augsburg.de/hoffmada/korrektur).

This tool will almost certainly only used by the Organic Computing Group at the
University of Augsburg but maybe it is also helpful for someone else.

Requirements
------------

You need Python 3.6 or later to run `assessment`.

Quick start
-----------

`assessment` can be installed directly from git:

    $ python3 -m pip install -U git+ssh://git@git.rz.uni-augsburg.de/oc-m/assessment.git

Now, if python on your system is configured properly, you can calculate the
grades based on your grades file like this:

    $ assessment GRADES

In case you don't have a grades file in INI format to start with, you can ask
`assessment` to copy a default one into your working directory:

    $ assessment --copy-grades

Now you can adapt the sub-grades and the weightings of their respective sections
of your evaluation sheet and use `assessment` as shown above.

Usage
-----

```
Usage: assessment [OPTIONS] GRADES

Options:
  -o, --out PATH  Save assessment to file.
  --copy-grades   Copy default grades to the current working
                  directory.
  --weights       Show the section's weights and exit.
  --version       Show the version and exit.
  --help          Show this message and exit.
```

Development status
------------------

Although assessment was tested extensively during daily use, it is still lacking
test cases, that verify its correct behavior.
