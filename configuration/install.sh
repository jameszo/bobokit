#!/bin/sh

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
git clone https://github.com/Kashomon/vimporter.git ~/.vim/plugin/vimporter
git clone git@github.com:jameszo/markdown-css.git ~/markdown-css
git clone git@github.com:jameszo/docs.git ~/code/docs

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew cask install osxfuse
brew install sshfs

brew install docker
brew install docker-machine
brew install docker-swarm
brew install docker-machine-driver-xhyve

brew install autojump
brew cask install dash
brew cask install iterm2

brew install openjdk@12
sudo ln -sfn /usr/local/opt/openjdk@12/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-12.jdk

brew install plantuml
brew install pandoc
brew install nmap

sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
