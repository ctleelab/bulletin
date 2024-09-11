# frozen_string_literal: true

# The main script to update and preprocess github project data

require 'yaml'
require 'English'
# config = YAML.load_file('_config.yml')
return_code = 0

puts `ruby _scripts/generate-readmes.rb 2>&1`
return_code += $CHILD_STATUS.exitstatus
puts `ruby _scripts/preprocess-markdown.rb 2>&1`
return_code += $CHILD_STATUS.exitstatus
puts `ruby _scripts/generate-project-data.rb 2>&1`
return_code += $CHILD_STATUS.exitstatus
exit return_code
