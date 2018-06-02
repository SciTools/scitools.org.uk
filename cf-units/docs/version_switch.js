// Copyright 2013 PSF. Licensed under the PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
// File originates from the cpython source found in Doc/tools/sphinxext/static/version_switch.js

(function() {
  'use strict';

  var url_re = /\/cf-units\/docs\/(latest|(v\d+\.\d+\.?\d?))\//;

  var all_versions = {
    'latest': 'latest (2.0)',
    // nb. Also include the latest version explictly as well as under "latest",
    // so that users can get to the versioned (non-latest) URL.

    'v2.0': '2.0',
    'v1.2': '1.2',
    'v1.1': '1.1'
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
    var new_url = url.replace(url_re, '/cf-units/docs/' + new_version + '/');
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
           window.location.href = '/cf-units/docs/' + selected;
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
    console.log(index_li);
    if (index_li.length > 0) {
      index_li.append('|&nbsp;'); 
      index_li.before('<li class="version_switcher right">' + select + '</li>');
    } else {
        sidebar = $('div.sphinxsidebarwrapper');
        var version_section = $('<div role="note" class="version_switcher"><h3>Version</h3></div>');
        version_section.append(select);
        sidebar.append(version_section);
    }
    $('.version_switcher select').bind('change', on_switch);
  });
})();
