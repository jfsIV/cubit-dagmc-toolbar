#! /bin/bash

curr_dir=$(dirname "$(realpath "$0")")
echo "Generating toolbar file for directory: ${curr_dir}"
sed "s|@DAGMC_TOOLBAR_LOCATION@|${curr_dir}|g" "${curr_dir}/toolbars/template.ttb" > toolbars/dagmc_toolbar.ttb