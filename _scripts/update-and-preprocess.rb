# go through projects and clean and update

require 'yaml'

$basedir = Dir.pwd
config = YAML.load_file("_config.yml")

if !config["projects"].nil? then
    config["projects"].each do |repo|
        name = repo.split('/').drop(1).join('')
        Dir.chdir($basedir + "/projects")
        if !Dir.exist?(name)								# clone project repo
            `git clone https://github.com/#{repo}.git`
        end
        Dir.chdir($basedir + "/projects/" + name)			# drop into blotter dir
        `git clean -f`										# remove untracked files, but keep directories
        `git reset --hard HEAD`								# bring back to head state
        `git pull origin master`							# git pull
    end
end

Dir.chdir($basedir)
`ruby _scripts/generate-readmes.rb`
`ruby _scripts/preprocess-markdown.rb`
`ruby _scripts/generate-project-data.rb`
