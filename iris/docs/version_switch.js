// Copyright 2013 PSF. Licensed under the PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
// File originates from the cpython source found in Doc/tools/sphinxext/static/version_switch.js

(function() {
  'use strict';

  var url_re = /\/iris\/docs\/(latest|(v\d+\.\d+\.?\d?))\//;

  var all_versions = {
    'latest': 'latest (2.4)',
    // nb. Also include the latest version explictly as well as under "latest",
    // so that users can get to the versioned (non-latest) URL.

    'v2.4.0': '2.4',
    'v2.3.0': '2.3',
    'v2.2.1': '2.2',
    'v2.1': '2.1',
    'v2.0': '2.0',
    'v1.13.0': '1.13',
    'v1.12.0': '1.12',
    'v1.11.0': '1.11',
    'v1.10.0': '1.10',
    'v1.9.2': '1.9',
    'v1.8.1': '1.8',
    'v1.7': '1.7',
    'v1.6': '1.6',
    'v1.5': '1.5',
    'v1.4': '1.4',
    'v1.3': '1.3',
    'v1.2': '1.2',
    'v1.1': '1.1',
    'v1.0': '1.3',
    'v0.9.1': '0.9',
    'dev': 'dev',
  };

  function build_select(current_version, current_release) {
    var buf = ['<select>'];

    var url = window.location.href;

    var match = url_re.exec(url);
    if (match && match[1] == 'latest') {
        current_version = match[1];
    }

    $.each(all_versions, function(path, version) {
      buf.push('<option value="' + path + '"');
      if (version == current_version)
        buf.push(' selected="selected">' + current_version + '</option>');
      else
        buf.push('>' + version + '</option>');
    });

    buf.push('</select>');
    return buf.join('');
  }

  function patch_url(url, new_version) {
    function replacer(match, part1, offset, string) {
        return match[0].replace(part1, new_version);
    }
    var new_url = url.replace(url_re, '/iris/docs/' + new_version + '/');
    return new_url;
  }

  function on_switch() {
    var selected = $(this).children('option:selected').attr('value');

    var url = window.location.href,
        new_url = patch_url(url, selected);

    if (new_url != url) {
      // check beforehand if url exists, else redirect to version's start page
      $.ajax({
        url: new_url,
        success: function() {
           window.location.href = new_url;
        },
        error: function() {
           window.location.href = '/iris/docs/' + selected;
        }
      });
    }
  }

  $(document).ready(function() {
    var release = DOCUMENTATION_OPTIONS.VERSION;
    // Take the first 2 parts of the release (e.g. "0.6.0" -> "0.6")
    var version = release.split('.').slice(0, 2).join('.');
    var select = build_select(version, release);

    // Insert the version switcher into the right-hand-side of the top pane.
    var index_li = $('li.right:contains("index")');
    index_li.append('|&nbsp;'); 
    index_li.before('<li class="version_switcher right">' + select + '</li>');
    $('.version_switcher select').bind('change', on_switch);
  });
})();
