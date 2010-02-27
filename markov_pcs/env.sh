#!/usr/bin/env/sh
declare script_dir script_path

# man bash 2>/dev/null | less -p 'BASH_SOURCE'
[[ ${BASH_VERSINFO[0]} -le 2 ]] && echo 'The BASH_SOURCE array variable is only available for Bash 3.0 and higher!' && exit 1

[[ "${BASH_SOURCE[0]}" != "${0}" ]] && echo "script ${BASH_SOURCE[0]} is running sourced ..."

# cf. Bash get self directory trick,
# http://stevemorin.blogspot.com/2007/10/bash-get-self-directory-trick.html

script_path="$(cd $(/usr/bin/dirname "${BASH_SOURCE[0]}"); pwd -P)/$(/usr/bin/basename "${BASH_SOURCE[0]}")"

[[ ! -f "$script_path" ]] && script_path="$(cd $(/usr/bin/dirname "$0"); pwd -P)/$(/usr/bin/basename "$0")"

[[ ! -f "$script_path" ]] && script_path="" && echo 'No full path to running script found!' && exit 1

# full path to executing script's directory
script_dir="${script_path%/*}"
echo "script_dir: ${script_dir}"

# full path to executing script
echo "script_path: ${script_path}"

export PYTHONPATH=$PYTHONPATH:$script_dir/product/



