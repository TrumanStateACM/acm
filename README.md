# Meeting Minutes notes

- file name should be in the format yyyy-mm-dd-string.md
- title tag will be what is actually displayed on the webpage, so it should be meaningful 
- place files in _posts folder

# Install jekyll windows
- install ruby-dev from [this](https://rubyinstaller.org/downloads/) website
- pull website to computer
- hold shift and right click in acm website directory and open cmd
- type 

``` 
gem install bundler
```

- while cmd prompt is in acm directory type

```
bundle update
```

- then you can run 

```
jekyll build
```

to build the website 

- if you get this error "You have already activated X, but your Gemfile requires Y" then you can do two things
```
gem uninstall x
```

with x being the version thats newer, or 

``` 
bundle exec jekyll build
```

which will force the use of the version you needed. This works with all the jekyll commands

All of the main pages are in _pages, except the front page which is just index.markdown in the root directory. They are markdown files that you edit so a minimal amount of html and css knowledge is necessary. 

The meeting minutes are saved in _posts. There is a template for those. just make sure to save it and rename it before you start editing it. 

# material-jekyll-theme
[Demo](http://alexcarpenter.github.io/material-jekyll-theme)

![Material Jekyll Theme](https://d13yacurqjgara.cloudfront.net/users/37718/screenshots/2430279/slice_1.jpg)

## Getting started
1. `git clone https://github.com/alexcarpenter/material-jekyll-theme.git`
2. `cd material-jekyll-theme`
3. Configure the `_config.yml` file as needed
4. `jekyll serve`

## Options
Customize your options within the `_config.yml` file.

+ Theme
  - Green
  - Blue
  - Orange
  - Purple
  - Grey
+ Fixed Navigation
  - True
  - False
