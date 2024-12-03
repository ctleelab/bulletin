# frozen_string_literal: true

# Walk through config: readmes and grab associated README.md for each entry
# Write this readme out to projects/ directory
# Delete index.md if it already exists

require 'yaml'
require 'down'
require 'fileutils'

module Readmes
  def self.generate_readmes(config_file)
    return_code = 0
    project_data = {}

    config = YAML.load_file(config_file)
    projects_array = config['projects']

    puts 'DOWNLOADING READMEs...'

    if projects_array.length.positive?
      projects_array.each do |repometa|
        repo = repometa['repo']
        branch = repometa['branch']
        begin
          githubfile = Down.download(
            "https://raw.githubusercontent.com/#{repo}/#{branch}/README.md",
            max_redirects: 5
          )
        rescue Down::Error
          puts("\t\t#{repo}:#{branch} README.md file not found")
          return_code = 1
        else
          name = repo.split('/').drop(1).join('')
          dir = "projects/#{name}/"
          FileUtils.mkdir_p(dir)
          FileUtils.mv(githubfile.path, "#{dir}README.md")

          File.delete("#{dir}index.md") if File.exist?("#{dir}index.md")

          # Find image links to repository local files within readme
          if File.exist?("#{dir}README.md")
            contents = File.open("#{dir}README.md", 'r').read
            matchesHTML = contents.scan(/<img.+src="([^"]+)"/)
            matchesMD = contents.scan(/!\[[^\]]*\]\(([^)]+)\)/)
            matches = matchesHTML + matchesMD
            matches.each do |match|
              imagePath = match[0]
              http_present = imagePath.scan(%r{https*://})
              # if match does not start with http then assume it's a local file
              # try to download it copy to the static site
              next unless http_present.empty?

              imageUrl = "https://raw.githubusercontent.com/#{repo}/#{branch}/#{imagePath}"
              begin
                imageFile = Down.download(imageUrl, max_redirects: 5)
              rescue Down::Error
                puts "\t\tFile image not found #{imageUrl}"
                return_code = 1
              else
                FileUtils.mkdir_p(File.dirname(dir + imagePath))
                FileUtils.mv(imageFile.path, dir + imagePath)
              end
            end
          end
        end
      end
    end
    return_code
  end
end

return_code = Readmes.generate_readmes('_config.yml')
exit return_code
