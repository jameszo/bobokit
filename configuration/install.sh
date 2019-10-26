#!/bin/sh

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
git clone https://github.com/Kashomon/vimporter.git ~/.vim/plugin/vimporter
git clone git@github.com:jameszo/markdown-css.git ~

sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew cask install java
brew install plantuml
brew install telnet
brew install nmap
