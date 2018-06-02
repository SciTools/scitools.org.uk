function cf_units_redirect(path) {
  if (path.match('cf\-units/docs/(latest|v[0-9\.]*)')) {
      // The URL is using the correct form.
      return null;
  }

  String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.replace(new RegExp(search, 'g'), replacement);
  };

  new_path = path.replaceAll('cf_units', 'cf-units');

  // Identify old-style URLs that don't have cf-units[/docs/latest|v...]
  path_split = new_path.split("/");

  for (i=path_split.length; i>0; --i) {
      if (path_split[i] == 'cf-units') {
          // If docs doesn't immediately follow cf-units, insert it into the path.
          if (path_split[i+1] != 'docs') {
              path_split.splice(i+1, 0, 'docs');
          }

          vn_str = path_split[i+2];
          not_latest_or_vXX = (vn_str != 'latest' & !vn_str.match('v[0-1\.]+.*'))
          if (not_latest_or_vXX) {
              path_split.splice(i+2, 0, 'latest');
          }
          break;
      }
  }
  new_path =  path_split.join('/');
  if (path == new_path) {
      new_path = null;
  }
  return new_path;
}


function handle_redirects() {
  current_location = document.location.toString();

  new_location = cf_units_redirect(current_location);
  if (new_location) {
      window.location.replace(new_location);
  }
}
