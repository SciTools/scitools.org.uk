# SciTools Projects

## Licensing

All projects under the SciTools[-incubator] GitHub organisations are to be
developed in the open (i.e. via small pull requests which are open to
public review) and released under an OSI (Open Source Initiative) approved
license.


## Copyright

All SciTools projects operate a shared ownership model as specified
in the [SciTools CLA](https://scitools.org.uk/cla/v4).
The copyright statement is:

```
Copyright <start year>(-<end year>) <project> contributors
```

For example:

```
Copyright 2010-2019 Iris contributors
```


## Source preamble

All non-trivial source files in a SciTools repository must reference the
license of the repository. The wording of the preamble should be:

```
# Copyright <project> contributors
#
# This file is part of <project> and is released under the <OSI license> license.
# See LICENSE in the root of the repository for full licensing details.
```

**Note:** start and end dates are *not* required in the source preamble


## Default license

The default license for all SciTools projects is the BSD 3-clause license. 
The full text of a BSD 3-clause LICENSE file should be:

```
BSD 3-Clause License

Copyright <YEAR_START>-<YEAR_END> <project> contributors

See "Credits, copyright and license" in README.<ext> for full credits
<(if appropriate) and any exceptions to the following terms>.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```


In the situation where vendored / third-party tools have been packaged
into the repository, full terms should be documented in the License section of
the README.
As always, due care with licensing *MUST* be taken when vendoring in this way.


## Readme credits and license section

All repositories should include a "Credits, copyright and License"
section in the README.[md|rst|txt].

The Credits section should be used to document significant institutional
development of the project and to provide a link
pointing to the GitHub contributors list.

The Copyright and License section should re-iterate the copyright found
in the LICENSE file.

For example, Iris's README.md may include the following:

```

## Credits, copyright and license

Iris is developed collaboratively under the SciTools umberella.

A full list of code contributors ("Iris contributors") can be found at
https://github.com/SciTools/iris/graphs/contributors.

Code is just one of many ways of positively contributing to Iris, please see
our [contributing guide](.github/CONTRIBUTING.md) for more details on how
you can get involved.

Iris is released under a LGPL license with a shared copyright model.
See [LICENSE](LICENSE) for full terms.

The [Met Office](https://metoffice.gov.uk) has made a significant
contribution to the development, maintenance and support of this library.
All Met Office contributions are copyright on behalf of the British Crown.

```

